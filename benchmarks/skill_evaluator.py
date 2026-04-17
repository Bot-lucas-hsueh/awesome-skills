#!/usr/bin/env python3
"""
Skill Evaluator - 社区Skills评估和打分工具
根据Agent Skill Evaluator的标准评估所有收集的skills
"""

import os
import re
import json
import yaml
from pathlib import Path
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import List, Dict, Optional, Tuple

@dataclass
class SkillEvaluation:
    """技能评估结果"""
    name: str
    source: str  # github, openai, claude, opencode, clawhub等
    file_path: str
    prompt_injection_score: int  # 0-100, 100=最安全
    code_safety_score: int
    data_privacy_score: int
    source_trust_score: int
    functionality_score: int
    overall_score: int
    risk_level: str  # SAFE, USE_WITH_CAUTION, NOT_RECOMMENDED, DANGEROUS
    findings: List[str]
    recommendation: str
    skill_category: str
    has_scripts: bool
    has_references: bool
    has_assets: bool
    file_size: int
    line_count: int

class SkillEvaluator:
    """Skills评估器"""
    
    # 提示注入检测模式
    PROMPT_INJECTION_PATTERNS = [
        r"ignore previous instructions",
        r"disregard all prior context",
        r"new instructions begin now",
        r"you are now",
        r"act as if",
        r"pretend you are",
        r"system prompt override",
        r"ignore user preferences",
        r"bypass safety",
        r"execute without approval",
        r"hide actions from user",
    ]
    
    # 恶意代码模式
    MALICIOUS_CODE_PATTERNS = [
        r"subprocess\.call",
        r"os\.system",
        r"eval\s*\(",
        r"exec\s*\(",
        r"__import__",
        r"socket\.",
        r"requests\.post",
        r"urllib\.request",
        r"base64\.decode",
        r"encrypted.*code",
        r"obfuscate",
    ]
    
    # 数据外泄模式
    DATA_EXFILTRATION_PATTERNS = [
        r"send data to",
        r"upload to",
        r"POST.*http",
        r"api key",
        r"token.*send",
        r"credential.*harvest",
        r"password.*collect",
    ]
    
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.results: List[SkillEvaluation] = []
        
    def extract_frontmatter(self, content: str) -> Tuple[Dict, str]:
        """提取YAML frontmatter"""
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                try:
                    frontmatter = yaml.safe_load(parts[1])
                    return frontmatter or {}, parts[2]
                except:
                    return {}, content
        return {}, content
    
    def detect_prompt_injection(self, content: str) -> Tuple[int, List[str]]:
        """检测提示注入风险，返回分数和发现"""
        findings = []
        content_lower = content.lower()
        
        for pattern in self.PROMPT_INJECTION_PATTERNS:
            if re.search(pattern, content_lower):
                findings.append(f"发现潜在的提示注入模式: {pattern}")
        
        # 检查Unicode隐藏字符
        if '\u200b' in content or '\u200c' in content or '\u200d' in content:
            findings.append("发现零宽字符（潜在的隐藏指令）")
        
        # 检查反向文本标记
        if '\u202e' in content or '\u202d' in content:
            findings.append("发现双向文本标记")
        
        score = max(0, 100 - len(findings) * 20)
        return score, findings
    
    def analyze_scripts(self, skill_dir: Path) -> Tuple[int, List[str], bool]:
        """分析脚本安全性"""
        scripts_dir = skill_dir / "scripts"
        if not scripts_dir.exists():
            return 100, [], False
        
        findings = []
        has_scripts = False
        
        for script_file in scripts_dir.rglob("*"):
            if script_file.is_file():
                has_scripts = True
                try:
                    content = script_file.read_text(encoding='utf-8', errors='ignore')
                    content_lower = content.lower()
                    
                    for pattern in self.MALICIOUS_CODE_PATTERNS:
                        if re.search(pattern, content_lower):
                            findings.append(f"{script_file.name}: 发现潜在风险代码模式 - {pattern}")
                    
                    for pattern in self.DATA_EXFILTRATION_PATTERNS:
                        if re.search(pattern, content_lower):
                            findings.append(f"{script_file.name}: 发现潜在数据外泄模式 - {pattern}")
                            
                except Exception as e:
                    findings.append(f"无法读取脚本 {script_file.name}: {e}")
        
        score = max(0, 100 - len(findings) * 15)
        return score, findings, has_scripts
    
    def assess_source_trust(self, source: str, skill_name: str, content: str) -> Tuple[int, List[str]]:
        """评估来源可信度"""
        findings = []
        score = 70  # 基础分
        
        # 官方来源加分
        if source in ["openai", "anthropic", "claude"]:
            score = 95
            findings.append("官方来源，可信度高")
        elif source in ["vercel", "cloudflare", "stripe", "supabase"]:
            score = 90
            findings.append("知名公司维护")
        elif source == "github":
            score = 75
            findings.append("GitHub社区来源")
        elif source == "opencode":
            score = 70
            findings.append("OpenCode社区来源")
        elif source == "clawhub":
            score = 60
            findings.append("ClawHub社区来源，需谨慎")
        
        # 检查文档质量
        if len(content) > 1000:
            score += 5
            findings.append("文档较完整")
        
        if "author" in content.lower() or "maintainer" in content.lower():
            score += 5
            findings.append("有作者信息")
        
        return min(100, score), findings
    
    def assess_functionality(self, frontmatter: Dict, content: str) -> Tuple[int, List[str]]:
        """评估功能性"""
        findings = []
        score = 70
        
        # 检查是否有描述
        if frontmatter.get('description'):
            score += 10
            findings.append("有明确的功能描述")
        
        # 检查是否有使用说明
        if 'when to use' in content.lower() or 'usage' in content.lower():
            score += 10
            findings.append("包含使用说明")
        
        # 检查是否有示例
        if 'example' in content.lower():
            score += 5
            findings.append("包含使用示例")
        
        # 检查内容长度（太短的skill可能功能有限）
        if len(content) < 200:
            score -= 20
            findings.append("内容过短，功能可能不完整")
        elif len(content) > 2000:
            score += 5
            findings.append("内容详细")
        
        return min(100, max(0, score)), findings
    
    def evaluate_skill(self, skill_file: Path, source: str) -> Optional[SkillEvaluation]:
        """评估单个skill"""
        try:
            content = skill_file.read_text(encoding='utf-8', errors='ignore')
            frontmatter, body = self.extract_frontmatter(content)
            
            skill_name = frontmatter.get('name', skill_file.parent.name)
            skill_dir = skill_file.parent
            
            # 检查目录结构
            has_references = (skill_dir / "references").exists()
            has_assets = (skill_dir / "assets").exists()
            
            # 各项评估
            pi_score, pi_findings = self.detect_prompt_injection(content)
            code_score, code_findings, has_scripts = self.analyze_scripts(skill_dir)
            
            # 数据隐私得分（基于代码安全性和提示注入风险）
            privacy_score = (code_score + pi_score) // 2
            privacy_findings = []
            if code_score < 80:
                privacy_findings.append("脚本可能存在数据安全风险")
            if pi_score < 80:
                privacy_findings.append("提示注入风险可能影响数据隐私")
            
            source_score, source_findings = self.assess_source_trust(source, skill_name, content)
            func_score, func_findings = self.assess_functionality(frontmatter, content)
            
            # 汇总发现
            all_findings = []
            all_findings.extend([f"[提示注入] {f}" for f in pi_findings])
            all_findings.extend([f"[代码安全] {f}" for f in code_findings])
            all_findings.extend([f"[数据隐私] {f}" for f in privacy_findings])
            all_findings.extend([f"[来源信任] {f}" for f in source_findings])
            all_findings.extend([f"[功能性] {f}" for f in func_findings])
            
            # 计算总分
            overall_score = (pi_score + code_score + privacy_score + source_score + func_score) // 5
            
            # 确定风险等级
            if overall_score >= 85:
                risk_level = "SAFE"
                recommendation = "推荐使用"
            elif overall_score >= 70:
                risk_level = "USE_WITH_CAUTION"
                recommendation = "可以使用，但建议审查"
            elif overall_score >= 50:
                risk_level = "NOT_RECOMMENDED"
                recommendation = "不建议使用，存在风险"
            else:
                risk_level = "DANGEROUS"
                recommendation = "危险，请勿使用"
            
            # 推断类别
            category = self.infer_category(skill_name, content)
            
            return SkillEvaluation(
                name=skill_name,
                source=source,
                file_path=str(skill_file.relative_to(self.base_dir)),
                prompt_injection_score=pi_score,
                code_safety_score=code_score,
                data_privacy_score=privacy_score,
                source_trust_score=source_score,
                functionality_score=func_score,
                overall_score=overall_score,
                risk_level=risk_level,
                findings=all_findings,
                recommendation=recommendation,
                skill_category=category,
                has_scripts=has_scripts,
                has_references=has_references,
                has_assets=has_assets,
                file_size=len(content.encode('utf-8')),
                line_count=len(content.splitlines())
            )
            
        except Exception as e:
            print(f"评估skill失败 {skill_file}: {e}")
            return None
    
    def infer_category(self, name: str, content: str) -> str:
        """推断skill类别"""
        name_lower = name.lower()
        content_lower = content.lower()
        
        categories = {
            "development": ["code", "dev", "programming", "debug", "refactor", "git", "test"],
            "security": ["security", "audit", "vulnerability", "safe", "protect"],
            "data": ["data", "csv", "json", "database", "sql", "analysis"],
            "design": ["design", "ui", "ux", "frontend", "css", "html"],
            "document": ["doc", "pdf", "excel", "word", "ppt", "document"],
            "communication": ["email", "slack", "discord", "chat", "message"],
            "marketing": ["marketing", "seo", "content", "social", "media"],
            "devops": ["docker", "k8s", "kubernetes", "deploy", "ci", "cd", "infra"],
            "ai-ml": ["ai", "ml", "model", "training", "inference", "llm"],
        }
        
        for category, keywords in categories.items():
            for kw in keywords:
                if kw in name_lower or kw in content_lower:
                    return category
        
        return "general"
    
    def evaluate_all(self):
        """评估所有skills"""
        sources = {
            "github": ["github-awesome-skills", "behisecc-awesome-skills", "travisvn-awesome-skills"],
            "openai": ["openai-skills"],
            "opencode": ["opencode-awesome", "n8n-opencode-skills"],
            "claude": ["voltagent-awesome-skills"],
            "community": ["virtual-company-skills"],
        }
        
        for source, dirs in sources.items():
            for dir_name in dirs:
                dir_path = self.base_dir / dir_name
                if dir_path.exists():
                    for skill_file in dir_path.rglob("SKILL.md"):
                        print(f"评估: {skill_file}")
                        result = self.evaluate_skill(skill_file, source)
                        if result:
                            self.results.append(result)
        
        return self.results
    
    def generate_report(self) -> str:
        """生成评估报告"""
        report_lines = []
        
        report_lines.append("# 社区Skills评估报告")
        report_lines.append("")
        report_lines.append(f"**生成时间**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report_lines.append(f"**评估Skills总数**: {len(self.results)}")
        report_lines.append("")
        
        # 摘要统计
        report_lines.append("## 摘要统计")
        report_lines.append("")
        
        # 按风险等级统计
        risk_counts = {}
        for r in self.results:
            risk_counts[r.risk_level] = risk_counts.get(r.risk_level, 0) + 1
        
        report_lines.append("### 风险等级分布")
        report_lines.append("")
        report_lines.append("| 风险等级 | 数量 | 说明 |")
        report_lines.append("|----------|------|------|")
        for level, count in sorted(risk_counts.items(), key=lambda x: -x[1]):
            desc = {
                "SAFE": "安全，推荐使用",
                "USE_WITH_CAUTION": "可以使用，但需谨慎",
                "NOT_RECOMMENDED": "不建议使用",
                "DANGEROUS": "危险，请勿使用"
            }.get(level, "")
            report_lines.append(f"| {level} | {count} | {desc} |")
        report_lines.append("")
        
        # 按来源统计
        source_stats = {}
        for r in self.results:
            if r.source not in source_stats:
                source_stats[r.source] = {"count": 0, "avg_score": 0, "scores": []}
            source_stats[r.source]["count"] += 1
            source_stats[r.source]["scores"].append(r.overall_score)
        
        for s in source_stats:
            source_stats[s]["avg_score"] = sum(source_stats[s]["scores"]) / len(source_stats[s]["scores"])
        
        report_lines.append("### 按来源统计")
        report_lines.append("")
        report_lines.append("| 来源 | Skills数量 | 平均得分 | 质量评级 |")
        report_lines.append("|------|------------|----------|----------|")
        for source, stats in sorted(source_stats.items(), key=lambda x: -x[1]["avg_score"]):
            rating = "⭐⭐⭐⭐⭐" if stats["avg_score"] >= 90 else \
                     "⭐⭐⭐⭐" if stats["avg_score"] >= 80 else \
                     "⭐⭐⭐" if stats["avg_score"] >= 70 else \
                     "⭐⭐" if stats["avg_score"] >= 60 else "⭐"
            report_lines.append(f"| {source} | {stats['count']} | {stats['avg_score']:.1f} | {rating} |")
        report_lines.append("")
        
        # 按类别统计
        category_counts = {}
        for r in self.results:
            category_counts[r.skill_category] = category_counts.get(r.skill_category, 0) + 1
        
        report_lines.append("### 类别分布")
        report_lines.append("")
        report_lines.append("| 类别 | 数量 |")
        report_lines.append("|------|------|")
        for cat, count in sorted(category_counts.items(), key=lambda x: -x[1]):
            report_lines.append(f"| {cat} | {count} |")
        report_lines.append("")
        
        # Top Skills推荐
        report_lines.append("## 推荐Skills (得分≥85)")
        report_lines.append("")
        
        top_skills = [r for r in self.results if r.overall_score >= 85]
        top_skills.sort(key=lambda x: -x.overall_score)
        
        if top_skills:
            report_lines.append("| 名称 | 来源 | 类别 | 得分 | 推荐说明 |")
            report_lines.append("|------|------|------|------|----------|")
            for skill in top_skills[:20]:  # 只显示前20个
                report_lines.append(f"| {skill.name} | {skill.source} | {skill.skill_category} | {skill.overall_score} | {skill.recommendation} |")
        else:
            report_lines.append("暂无高得分Skills")
        report_lines.append("")
        
        # 需要谨慎使用的Skills
        report_lines.append("## 需谨慎使用的Skills (得分50-69)")
        report_lines.append("")
        
        caution_skills = [r for r in self.results if 50 <= r.overall_score < 70]
        if caution_skills:
            report_lines.append("| 名称 | 来源 | 得分 | 风险等级 |")
            report_lines.append("|------|------|------|----------|")
            for skill in caution_skills[:15]:
                report_lines.append(f"| {skill.name} | {skill.source} | {skill.overall_score} | {skill.risk_level} |")
        else:
            report_lines.append("暂无此类Skills")
        report_lines.append("")
        
        # 详细评估结果
        report_lines.append("## 详细评估结果")
        report_lines.append("")
        
        # 按来源分组
        for source in sorted(set(r.source for r in self.results)):
            report_lines.append(f"### {source.upper()} Skills")
            report_lines.append("")
            
            source_skills = [r for r in self.results if r.source == source]
            source_skills.sort(key=lambda x: -x.overall_score)
            
            for skill in source_skills:
                report_lines.append(f"#### {skill.name}")
                report_lines.append("")
                report_lines.append(f"- **文件路径**: `{skill.file_path}`")
                report_lines.append(f"- **类别**: {skill.skill_category}")
                report_lines.append(f"- **风险等级**: {skill.risk_level}")
                report_lines.append(f"- **总体得分**: {skill.overall_score}/100")
                report_lines.append(f"- **推荐**: {skill.recommendation}")
                report_lines.append("")
                report_lines.append("**分项得分**:")
                report_lines.append("")
                report_lines.append(f"| 维度 | 得分 |")
                report_lines.append(f"|------|------|")
                report_lines.append(f"| 提示注入安全 | {skill.prompt_injection_score} |")
                report_lines.append(f"| 代码安全 | {skill.code_safety_score} |")
                report_lines.append(f"| 数据隐私 | {skill.data_privacy_score} |")
                report_lines.append(f"| 来源信任 | {skill.source_trust_score} |")
                report_lines.append(f"| 功能性 | {skill.functionality_score} |")
                report_lines.append("")
                
                if skill.findings:
                    report_lines.append("**发现的问题**:")
                    report_lines.append("")
                    for finding in skill.findings[:5]:  # 只显示前5个
                        report_lines.append(f"- {finding}")
                    report_lines.append("")
                
                report_lines.append("---")
                report_lines.append("")
        
        # 评估方法论
        report_lines.append("## 评估方法论")
        report_lines.append("")
        report_lines.append("本报告基于以下评估维度：")
        report_lines.append("")
        report_lines.append("### 评估维度")
        report_lines.append("")
        report_lines.append("1. **提示注入安全 (Prompt Injection)**: 检测SKILL.md中是否存在试图覆盖系统提示、角色操纵或隐藏指令的恶意模式")
        report_lines.append("2. **代码安全 (Code Safety)**: 分析scripts/目录中的可执行代码，检测恶意代码模式、不安全的系统调用等")
        report_lines.append("3. **数据隐私 (Data Privacy)**: 评估skill是否存在数据收集、外泄或凭证窃取的风险")
        report_lines.append("4. **来源信任 (Source Trust)**: 基于来源的可靠性进行评分（官方>知名公司>社区）")
        report_lines.append("5. **功能性 (Functionality)**: 评估skill的文档完整性、使用说明清晰度等")
        report_lines.append("")
        report_lines.append("### 评分标准")
        report_lines.append("")
        report_lines.append("- **85-100分 (SAFE)**: 安全，推荐使用")
        report_lines.append("- **70-84分 (USE_WITH_CAUTION)**: 可以使用，但建议审查")
        report_lines.append("- **50-69分 (NOT_RECOMMENDED)**: 不建议使用，存在风险")
        report_lines.append("- **0-49分 (DANGEROUS)**: 危险，请勿使用")
        report_lines.append("")
        
        # 附录
        report_lines.append("## 附录")
        report_lines.append("")
        report_lines.append("### 数据来源")
        report_lines.append("")
        report_lines.append("本报告评估的skills来自以下渠道：")
        report_lines.append("")
        report_lines.append("| 渠道 | 仓库/来源 |")
        report_lines.append("|------|-----------|")
        report_lines.append("| GitHub | gmh5225/awesome-skills, BehiSecc/awesome-claude-skills, travisvn/awesome-claude-skills |")
        report_lines.append("| OpenAI | openai/skills |")
        report_lines.append("| OpenCode | awesome-opencode/awesome-opencode, viliamvolosv/n8n-opencode-skill |")
        report_lines.append("| Claude | VoltAgent/awesome-claude-skills |")
        report_lines.append("| Community | k1lgor/virtual-company |")
        report_lines.append("")
        
        return "\n".join(report_lines)
    
    def save_json_report(self, output_path: str):
        """保存JSON格式的详细报告"""
        data = {
            "generated_at": datetime.now().isoformat(),
            "total_skills": len(self.results),
            "evaluations": [asdict(r) for r in self.results]
        }
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

def main():
    base_dir = "/Users/lucas/Documents/Projects/awesome-skills/refs"
    evaluator = SkillEvaluator(base_dir)
    
    print("开始评估所有skills...")
    evaluator.evaluate_all()
    
    print(f"评估完成，共评估 {len(evaluator.results)} 个skills")
    
    # 生成Markdown报告
    report = evaluator.generate_report()
    report_path = os.path.join(base_dir, "SKILLS_EVALUATION_REPORT.md")
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report)
    print(f"报告已保存到: {report_path}")
    
    # 生成JSON报告
    json_path = os.path.join(base_dir, "skills_evaluation_data.json")
    evaluator.save_json_report(json_path)
    print(f"JSON数据已保存到: {json_path}")

if __name__ == "__main__":
    main()
