# Economic Graph Deep Dive

## Overview

The Economic Graph is LinkedIn's vision to create a digital map of the global economy, connecting every professional, company, job, skill, and school worldwide.

## Core Entities

### 1. Members (1.3B+)
- Professional profiles with skills, experience, education
- Connections forming the social graph
- Career trajectories and mobility patterns

### 2. Companies (67M+)
- Organization profiles with industry, size, location
- Job postings and hiring patterns
- Employee networks and alumni

### 3. Skills (41,000+)
- Standardized skill taxonomy
- Hierarchical relationships
- Emerging skill detection

### 4. Jobs (50M+)
- Active and historical job postings
- Skill requirements and salary data
- Application and hiring flows

### 5. Schools (36,000+)
- Educational institutions
- Alumni networks
- Degree and credential data

## Data Relationships

```
Member ──connects_to──> Member
Member ──works_at─────> Company
Member ──has_skill────> Skill
Member ──studied_at───> School
Company ──posts───────> Job
Job ──requires────────> Skill
```

## Applications

### Labor Market Insights
- Real-time hiring trends
- Skill demand forecasting
- Salary benchmarking
- Geographic mobility patterns

### Talent Matching
- Skills-based job recommendations
- Career path suggestions
- Talent pool analysis
- Diversity insights

### Economic Research
- Workforce transformation studies
- Industry trend analysis
- Policy impact assessment

## Technical Implementation

### Graph Database
- Custom LinkedIn Graph (built on top of distributed stores)
- Trillions of edges, billions of nodes
- Real-time traversal capabilities

### Analytics
- Apache Pinot for real-time OLAP
- Pre-aggregated metrics for common queries
- Sub-second query latency on billions of rows

## Key Insights

1. **Network Effects**: Value increases quadratically with connections
2. **Data Flywheel**: More data → Better recommendations → More engagement → More data
3. **Skill Adjacencies**: Understanding which skills lead to career mobility
4. **Temporal Dynamics**: Career changes, skill evolution, industry shifts
