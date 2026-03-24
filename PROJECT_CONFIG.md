# Project Configuration Guide

This document describes the GitHub Actions workflows and project configuration for Awesome Skills.

## 🔄 CI/CD Pipeline (3-Step Process)

### Step 1: Evaluate & Generate Report
**Workflow:** `comprehensive-evaluation.yml` → `step1-evaluate`

- Runs comprehensive skill evaluation using skill-evaluator methodology
- Generates JSON and HTML reports
- Displays summary in Actions output
- Uploads artifacts for subsequent steps

**Triggers:**
- Daily at 4 AM UTC (scheduled)
- Push to main (when skills or workflows change)
- Manual dispatch

### Step 2: Update GitHub Pages
**Workflow:** `pages-deploy.yml`

- Deploys website to GitHub Pages
- Includes evaluation reports
- Makes reports accessible via web URL

**URL:** `https://theneoai.github.io/awesome-skills/reports/evaluation_report.html`

### Step 3: Update README & Project Config
**Workflow:** `comprehensive-evaluation.yml` → `step3-update-config`

- Updates README.md with latest statistics
- Updates index.html with current counts
- Creates/updates `assets/js/skill-stats.js`
- Commits and pushes changes

## ⚙️ Required GitHub Settings

### 1. Enable GitHub Pages

1. Go to **Settings** → **Pages**
2. Set **Source** to "GitHub Actions"
3. Save

### 2. Configure Workflow Permissions

1. Go to **Settings** → **Actions** → **General**
2. Under **Workflow permissions**, select:
   - ✅ Read and write permissions
   - ✅ Allow GitHub Actions to create and approve pull requests

### 3. Set Up GitHub Token (if needed)

The workflows use `secrets.GITHUB_TOKEN` which is automatically provided. No additional setup needed.

## 📊 Workflow Status Badges

Add these badges to README.md:

```markdown
[![Evaluation](https://github.com/theneoai/awesome-skills/actions/workflows/comprehensive-evaluation.yml/badge.svg)](https://github.com/theneoai/awesome-skills/actions/workflows/comprehensive-evaluation.yml)
[![Pages](https://github.com/theneoai/awesome-skills/actions/workflows/pages-deploy.yml/badge.svg)](https://github.com/theneoai/awesome-skills/actions/workflows/pages-deploy.yml)
```

## 🏗️ Workflow Dependencies

```
Step 1: Evaluate
    ↓ (artifacts)
Step 2: Deploy Pages
    ↓ (after Pages deploy)
Step 3: Update Config
```

## 📁 Generated Artifacts

| Artifact | Location | Description |
|----------|----------|-------------|
| `evaluation_report.json` | `reports/` | Raw evaluation data |
| `evaluation_report.html` | `reports/` | Human-readable HTML report |
| `skill-stats.js` | `assets/js/` | JavaScript data for website |

## 🚀 Manual Trigger

You can manually trigger the workflows from the **Actions** tab:

1. Select the workflow
2. Click "Run workflow"
3. Choose branch (usually `main`)
4. Click "Run workflow"

## 📝 Environment Variables

None required. All configuration is in the workflow files.

## 🐛 Troubleshooting

### Pages not deploying
- Check that Pages is enabled in Settings → Pages
- Ensure source is set to "GitHub Actions"
- Check `pages-deploy.yml` workflow permissions

### README not updating
- Check that workflow has write permissions
- Verify `GITHUB_TOKEN` has correct permissions
- Look for "[ci skip]" in commit messages (prevents recursive runs)

### Evaluation failing
- Check Python dependencies are installed
- Verify `scripts/comprehensive_skill_evaluation.py` exists
- Check for syntax errors in skill files

## 📈 Monitoring

View workflow status at:
- **Actions tab:** `https://github.com/theneoai/awesome-skills/actions`
- **Pages status:** Settings → Pages

## 🔄 Update Frequency

| Workflow | Frequency | Notes |
|----------|-----------|-------|
| Comprehensive Evaluation | Daily 4 AM UTC | Also runs on skill changes |
| Pages Deploy | On demand | Triggered after evaluation |
| Skill Quality Gate (quality.yml) | On PR + push | Quality checks and validation |

## 📞 Support

For issues with the CI/CD pipeline:
1. Check the Actions logs for error messages
2. Verify GitHub settings match this guide
3. Open an issue with the workflow run link
