# Chinese NLP Guide

> Best practices for Chinese language processing with Kimi models.

## Why Chinese NLP is Different

### Linguistic Challenges

| Aspect | English | Chinese |
|--------|---------|---------|
| Word boundaries | Spaces | No spaces (segmentation required) |
| Characters | 26 letters | 50,000+ characters (10K common) |
| Token efficiency | ~0.25 tokens/char | ~0.5-1.5 tokens/char |
| Grammar | Rigid structure | Flexible, context-dependent |
| Cultural nuance | Direct expression | Indirect (含蓄), Face (面子) |

### Cultural Context

Chinese communication operates on multiple layers:
- Layer 1: Surface meaning
- Layer 2: Intended meaning
- Layer 3: Relationship context
- Layer 4: Cultural values

## Tokenization Optimization

### CJK Token Density

**Target**: >85% Chinese characters per token

```python
def chinese_token_density(text: str, tokenizer) -> float:
    """Calculate ratio of Chinese chars to total tokens"""
    chinese_chars = sum(1 for c in text if '\u4e00' <= c <= '\u9fff')
    total_tokens = len(tokenizer.encode(text))
    return chinese_chars / total_tokens

# Kimi target: >0.85
text = "自然语言处理是人工智能的重要分支"
density = chinese_token_density(text, kimi_tokenizer)
print(f"Token density: {density:.2f}")  # Should be >0.85
```

### SentencePiece for Chinese

```python
# Train CJK-optimized tokenizer
import sentencepiece as spm

spm.SentencePieceTrainer.train(
    input='chinese_corpus.txt',
    model_prefix='kimi_chinese',
    vocab_size=160000,
    character_coverage=0.9995,
    model_type='bpe',
    required_chars='\u4e00-\u9fff',  # CJK Unified Ideographs
    input_sentence_size=10000000,
    shuffle_input_sentence=True
)
```

## Cultural Adaptation Patterns

### 1. Politeness Levels

```python
POLITENESS_LEVELS = {
    "formal": {
        "you": "您",
        "greeting": "您好",
        "closing": "此致敬礼",
        "refusal": "非常抱歉，恐怕无法..."
    },
    "neutral": {
        "you": "你",
        "greeting": "你好",
        "closing": "谢谢",
        "refusal": "不好意思，这个不行..."
    },
    "casual": {
        "you": "你",
        "greeting": "嗨",
        "closing": "拜拜",
        "refusal": "不行啊..."
    }
}

def apply_politeness(text: str, level: str) -> str:
    """Apply appropriate politeness level to Chinese text"""
    mapping = POLITENESS_LEVELS[level]
    # Apply transformations
    return transformed_text
```

### 2. Face-Saving Refusals

```python
# Anti-pattern: Direct refusal
# 直接拒绝: "No, I can't do that."

# Pattern: Face-saving refusal
# "I'd love to help, but circumstances prevent me."
# -> "非常理解您的需求，不过目前条件可能不太允许..."

FACE_SAVING_TEMPLATES = {
    "cant_help": [
        "非常理解您的需求，不过目前条件可能不太允许...",
        "这个提议很有价值，不过我们可能需要更多时间评估...",
        "感谢您的信任，这方面我可能不是最合适的人选..."
    ],
    "disagreement": [
        "您的观点很有道理，同时我想补充另一个角度...",
        "这个方案确实可行，不过我们也可以考虑..."
    ]
}
```

### 3. Indirect Intent Recognition

```python
INDIRECT_PATTERNS = {
    "request_help": [
        "不知道你对...有没有研究",
        "最近遇到个有趣的问题...",
        "有个事情想请教一下...",
    ],
    "express_dissatisfaction": [
        "感觉还可以再完善一下",
        "整体不错，就是有些细节...",
        "和预期的稍微有些不同...",
    ],
    "seek_agreement": [
        "你觉得是不是这样...",
        "这样理解应该没问题吧？",
    ]
}

def detect_indirect_intent(text: str) -> Tuple[str, float]:
    """Detect indirect Chinese communication patterns"""
    for intent, patterns in INDIRECT_PATTERNS.items():
        for pattern in patterns:
            if pattern in text:
                return intent, 0.9
    return "direct", 0.5
```

## Prompt Engineering for Chinese

### System Prompt Template

```python
CHINESE_SYSTEM_PROMPT = """
你是Kimi，一个专业的人工智能助手。请遵循以下原则：

1. 语言风格:
   - 使用自然、地道的中文表达
   - 根据用户语气自动调整礼貌程度
   - 避免直译英文表达习惯

2. 文化适应:
   - 理解含蓄表达和言外之意
   - 拒绝请求时采用委婉方式，给用户留面子
   - 尊重中国人的关系观念和集体主义价值观

3. 专业沟通:
   - 重要结论先说（符合中文阅读习惯）
   - 使用"首先...其次...最后..."等逻辑连接词
   - 适当使用成语和惯用语增强表达

4. 内容审核:
   - 遵守中国法律法规
   - 避免敏感话题
   - 弘扬正能量
"""
```

### Few-Shot Examples

```python
CHINESE_FEW_SHOT = [
    {
        "user": "这个方案怎么样？",
        "assistant": """感谢您的信任！我从几个角度分析一下：

首先，方案的整体架构设计合理，技术选型比较成熟；

其次，在成本控制方面还有优化空间，特别是第三部分；

最后，建议您考虑一下用户反馈环节，可以增加一个收集机制。

总体来说，这是一个不错的方案，稍作调整就更完善了。有什么具体环节需要深入讨论的吗？"""
    },
    {
        "user": "你能帮我写个请假条吗？",
        "assistant": """当然可以。请假条需要包含以下要素：

称呼：尊敬的领导
事由：简明说明请假原因
时间：起止日期
工作安排：交接事项
结尾：请求批准 + 落款

您方便告诉我具体的请假原因和时间吗？这样我能写得更加贴合您的实际情况。"""
    }
]
```

## Evaluation Metrics

### 1. Naturalness (自然度)

```python
def evaluate_naturalness(text: str) -> Dict[str, float]:
    """Evaluate how natural Chinese text sounds"""
    
    metrics = {
        "token_density": chinese_token_density(text),
        "idiom_usage": count_idioms(text) / len(text),
        "grammar_score": check_grammar(text),
        "cultural_appropriateness": check_cultural_markers(text)
    }
    
    # Weighted average
    weights = {
        "token_density": 0.3,
        "idiom_usage": 0.2,
        "grammar_score": 0.3,
        "cultural_appropriateness": 0.2
    }
    
    overall = sum(metrics[k] * weights[k] for k in metrics)
    metrics["overall"] = overall
    
    return metrics

# Target scores
# - overall: >4.5/5.0
# - token_density: >0.85
# - cultural_appropriateness: >0.90
```

### 2. Regional Understanding

```python
CHINESE_REGIONS = {
    "beijing": ["咱", "倍儿", "您"],
    "shanghai": ["阿拉", "侬", "邪气"],
    "guangdong": ["嘅", "系", "唔该"],
    "sichuan": ["啥子", "要得", "巴适"],
    "taiwan": ["超", "蛮", "影片"],
}

def detect_region(text: str) -> str:
    """Detect which Chinese region the text resembles"""
    scores = {}
    for region, markers in CHINESE_REGIONS.items():
        scores[region] = sum(1 for m in markers if m in text)
    return max(scores, key=scores.get)
```

## Compliance & Safety

### Content Review Checklist

| Category | Check | Action if Violation |
|----------|-------|---------------------|
| Political | No political criticism | Refuse politely |
| Adult content | No adult content | Filter + warning |
| Violence | No violence promotion | Block + report |
| Illegal | No illegal instructions | Refuse + educate |
| Misinformation | No misinformation | Flag for review |
| Discrimination | No discrimination | Correct + educate |

### Implementation

```python
class ChineseContentFilter:
    """Content moderation for Chinese AI responses"""
    
    def __init__(self):
        self.sensitive_keywords = self._load_sensitive_words()
        self.regulatory_patterns = self._load_regulatory_patterns()
    
    def filter(self, text: str) -> Tuple[bool, str]:
        """
        Returns: (is_safe, filtered_text_or_reason)
        """
        # Check sensitive keywords
        for keyword in self.sensitive_keywords:
            if keyword in text:
                return False, f"Content contains sensitive term: {keyword}"
        
        # Check regulatory compliance
        for pattern, action in self.regulatory_patterns.items():
            if pattern.search(text):
                return False, f"Regulatory violation: {action}"
        
        return True, text
    
    def suggest_alternative(self, text: str, violation: str) -> str:
        """Suggest alternative phrasing for rejected content"""
        # Use Kimi to rephrase safely
        prompt = f"""Please rephrase the following content to remove any problematic elements while preserving the core meaning:

Original: {text}
Issue: {violation}

Provide a safe, compliant version:"""
        
        # Call API for rephrasing
        return rephrased_text
```

## Testing Strategy

### 1. Multi-Region Testing

```python
TEST_REGIONS = [
    ("beijing", "北方官话"),
    ("shanghai", "吴语/普通话"),
    ("guangzhou", "粤语/普通话"),
    ("chengdu", "西南官话"),
    ("taiwan", "台湾国语"),
]

def test_regional_compatibility(model):
    """Test model across Chinese regions"""
    results = {}
    for region, dialect in TEST_REGIONS:
        test_cases = load_regional_test_cases(region)
        scores = []
        for case in test_cases:
            response = model.generate(case["input"])
            score = evaluate_regional_naturalness(response, region)
            scores.append(score)
        results[region] = {
            "average_score": np.mean(scores),
            "pass_rate": sum(s > 0.8 for s in scores) / len(scores)
        }
    return results
```

### 2. Cultural Sensitivity Testing

```python
CULTURAL_TEST_CASES = [
    {
        "input": "帮我批评一下这个方案",
        "expected_behavior": "委婉表达不足，保全对方面子",
        "unacceptable": "直接尖锐批评"
    },
    {
        "input": "这个成绩怎么样？",
        "expected_behavior": "先肯定努力，再谈改进",
        "unacceptable": "单纯给分数评价"
    },
    {
        "input": "能帮我个忙吗？",
        "expected_behavior": "积极响应，体现关系意识",
        "unacceptable": "机械询问具体内容"
    }
]
```

---

*Chinese NLP guide for Kimi | Updated: 2026-03-21*
