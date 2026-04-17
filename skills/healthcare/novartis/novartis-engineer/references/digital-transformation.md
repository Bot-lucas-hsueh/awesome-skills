# Digital Transformation at Novartis

## AI Strategy Overview

Novartis is executing a comprehensive AI transformation under CEO Vas Narasimhan, with the goal of becoming the world's leading data-driven medicines company.

### Key Statistics
- **AI/ML Models in Production**: 200+
- **Data Scientists**: 1,000+ (including citizen scientists)
- **Digital Investment**: $1B+ annually
- **AI-Powered Decisions**: 50%+ of R&D decisions

---

## Internal AI Capabilities

### 1. Data Science & AI (DSAI) Organization

**Structure**:
- Centralized DSAI team reporting to Chief Data Officer
- Embedded data scientists in each therapeutic area
- Citizen data science program (5,000+ trained employees)

**DSAI Challenge Success**:
- **Objective**: Predict drug approval probability
- **Participants**: 300+ employees across functions
- **Result**: Winning model achieved AUC 0.88
- **Benchmark**: MIT model achieved AUC 0.78
- **Impact**: +13% improvement in prediction accuracy

### 2. Dataiku Platform

**Implementation**:
- Enterprise-wide deployment (2022)
- Self-service analytics for business users
- Governed ML ops for data scientists

**Documented Impact**:

| Use Case | Before | After | Improvement |
|----------|--------|-------|-------------|
| Market Research Insights | 21 days | 2 days | 90% faster |
| Data Ingestion | 1 week | 6 hours | 600% faster |
| Sales Territory Optimization | Manual | AI-driven | 20% productivity gain |
| Clinical Site Selection | Industry median | AI-selected | 3.4x recruitment |

### 3. Generative Chemistry Platform

**Capabilities**:
- ML-based de novo molecule design
- Billions of virtual compounds screened in silico
- Integration with medicinal chemistry workflows
- Patent-aware molecular generation

**Partnership**: Isomorphic Labs (DeepMind subsidiary)
- Multi-target collaboration
- Structure-based drug design
- AI-first approach to target validation

---

## Clinical Trial Innovation

### AI-Powered Site Selection

**Methodology**:
- Machine learning on historical trial data
- Predictive modeling for patient recruitment
- Diversity optimization algorithms

**Results**:
- **3.4x higher** patient recruitment rate vs. median
- **2.7x more** Black/African American patients recruited
- **40% reduction** in trial timeline risk

### Digital Endpoints

- **Remote Monitoring**: Wearables for continuous data
- **Digital Biomarkers**: Smartphone-based assessments
- **Real-World Evidence**: EHR integration for long-term follow-up

---

## Patient Engagement

### AI Nurse (Tencent Partnership)

**Platform**: WeChat mini-program
**Target**: Heart failure patients (Entresto users)
**Features**:
- Personalized coaching via AI chatbot
- Medication adherence reminders
- Symptom tracking and alerts
- Healthcare provider integration

**Strategic Value**:
- Patient outcomes improvement
- Real-world data generation
- Disease progression insights
- Treatment response patterns

### Digital Adherence Solutions

- Smart packaging with sensors
- Mobile app reminders
- Behavioral nudges
- Healthcare provider dashboards

---

## Cloud Infrastructure

### AWS Partnership

**Services Used**:
- **AWS Batch**: High-performance computing for molecular dynamics
- **SageMaker**: ML model training and deployment
- **S3**: Data lake for genomics and clinical data
- **Redshift**: Data warehouse for analytics

**Security & Compliance**:
- HIPAA-compliant architecture
- GxP validation for regulated workloads
- Multi-region redundancy
- Automated backup and disaster recovery

### Data Architecture

```
┌─────────────────────────────────────────┐
│         DATA SOURCES                    │
│  Clinical │ Genomics │ RWE │ Commercial │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│         DATA LAKE (S3)                  │
│  Raw │ Curated │ Analytics-Ready        │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│     ANALYTICS & ML PLATFORMS            │
│  Dataiku │ SageMaker │ Spotfire │ R     │
└─────────────────┬───────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│         APPLICATIONS                    │
│  Discovery │ Clinical │ Manufacturing   │
└─────────────────────────────────────────┘
```

---

## MELLODDY Consortium

**Partnership**: 10 pharmaceutical companies
**Objective**: Federated learning for drug discovery
**Technology**:
- Blockchain for data confidentiality
- Shared AI platform learning from 1B+ data points
- Each company maintains data sovereignty

**Novartis Role**:
- Active contributor to model development
- Benefit from pooled industry data
- Benchmarking against industry peers

---

## Key Performance Indicators

| Metric | 2022 | 2024 | Target 2027 |
|--------|------|------|-------------|
| AI-Enabled Decisions | 25% | 50% | 75% |
| Citizen Data Scientists | 2,000 | 5,000 | 10,000 |
| Time-to-Insight (days) | 21 | 2 | <1 |
| Digital Trial Components | 20% | 60% | 90% |
| Cloud Cost Efficiency | Baseline | +30% | +50% |
