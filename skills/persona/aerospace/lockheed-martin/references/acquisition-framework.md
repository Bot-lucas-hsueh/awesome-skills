# Defense Acquisition Framework

## Overview

This reference document outlines the US Department of Defense acquisition framework that governs Lockheed Martin's major programs. Understanding this framework is essential for working effectively within the defense aerospace ecosystem.

## Defense Acquisition System

### Acquisition Categories (ACAT)

```yaml
ACAT_I:
  dollar_threshold: 
    MDAP: ≥$480M (RDT&E) or ≥$2.79B (procurement FY2014)
    MAIS: ≥$180M (FY2014)
  approval_authority: Milestone Decision Authority (MDA) - typically USD(A&S)
  examples: F-35, GPS III, SBIRS, THAAD, Orion

ACAT_IA:
  category: Automated Information System
  dollar_threshold: ≥$180M (FY2014)
  approval_authority: Component Acquisition Executive (CAE)

ACAT_II:
  dollar_threshold: 
    ≤ACAT_I thresholds
  approval_authority: Component Acquisition Executive
  examples: Major subsystems of ACAT I programs

ACAT_III:
  dollar_threshold: Not ACAT I or II
  approval_authority: Designated by Service Acquisition Executive
  examples: Most C-130 modifications, smaller missile programs

ACAT_IV (formerly ACAT_IIAM):
  category: Middle-tier acquisition
  purpose: Rapid prototyping and fielding
  authority: Delegated to program manager level
```

## Acquisition Pathways

### 1. Major Capability Acquisition (Traditional)

```yaml
pathway: Major Capability Acquisition (MCA)
applicability: Major defense acquisition programs (MDAPs)
document: DoDI 5000.02

phases:
  materiel_solution_analysis:
    purpose: Identify and analyze alternatives
    milestone: Milestone A
    key_documents:
      - Initial Capabilities Document (ICD)
      - Analysis of Alternatives (AoA) plan
      - Technology maturation plan
    
  technology_maturation_risk_reduction:
    purpose: Reduce technology and integration risk
    acronym: TMRR
    duration: 2-4 years typical
    key_reviews:
      - Alternative Systems Review (ASR)
      - System Requirements Review (SRR)
      - System Functional Review (SFR)
      - Preliminary Design Review (PDR)
    milestone: Milestone B
    
  engineering_manufacturing_development:
    purpose: Develop, integrate, test system
    acronym: EMD
    duration: 3-7 years typical
    key_reviews:
      - Critical Design Review (CDR)
      - Test Readiness Review (TRR)
      - System Verification Review (SVR)
      - Production Readiness Review (PRR)
    milestone: Milestone C
    
  production_deployment:
    purpose: Achieve operational capability
    phases:
      - Low-Rate Initial Production (LRIP)
      - Full-Rate Production (FRP)
    key_events:
      - Initial Operational Test & Evaluation (IOT&E)
      - Full-Rate Production Decision Review (FRPDR)
      - Initial Operational Capability (IOC)
      - Full Operational Capability (FOC)
      
  operations_support:
    purpose: Sustain operational effectiveness
    duration: 20-50+ years
    focus: 
      - Lifecycle sustainment
      - Continuous modernization
      - Disposal
```

### 2. Middle-Tier Acquisition (Section 804)

```yaml
pathway: Middle-Tier Acquisition (MTA)
authority: Section 804, NDAA FY2016
purpose: Rapid prototyping and rapid fielding

types:
  rapid_prototyping:
    purpose: Develop fieldable prototype
    timeline: 2-5 years
    exit: Transition to another pathway or rapid fielding
    
  rapid_fielding:
    purpose: Field production quantity in 2-5 years
    requirement: Fielding within 5 years of development start
    
examples:
  - Army: Various network modernization efforts
  - Air Force: Some CCA prototyping
  - Navy: Various unmanned systems
```

### 3. Urgent Capability Acquisition

```yaml
pathway: Urgent Operational Need (UON) / Joint Urgent Operational Need (JUON)
purpose: Field capabilities in <2 years
authority: Chairman of Joint Chiefs of Staff Instruction 3470.01

process:
  1. Identify urgent need in operational environment
  2. Validate through Joint Staff
  3. Rapid acquisition authority
  4. Expedited contracting
  5. Fielding

examples:
  - Counter-IED systems (Iraq/Afghanistan)
  - Various ISR systems
  - Electronic warfare systems
```

### 4. Defense Business Systems

```yaml
pathway: Defense Business System (DBS)
applicability: Business operations IT systems
threshold: ≥$1M annual investment
```

### 5. Acquisition of Services

```yaml
pathway: Acquisition of Services
applicability: Service contracts (not products)
process: Seven-step process per DoDI 5000.74
```

## Requirements Process

### Joint Capabilities Integration and Development System (JCIDS)

```yaml
process: JCIDS
document: CJCSI 5123.01

key_documents:
  initial_capabilities_document:
    acronym: ICD
    purpose: Identify capability gap and need
    approval: Joint Requirements Oversight Council (JROC)
    
  capability_development_document:
    acronym: CDD
    purpose: Define operational requirements for development
    content: Key Performance Parameters (KPPs), Key System Attributes (KSAs)
    approval: JROC or designated authority
    
  capability_production_document:
    acronym: CPD
    purpose: Refine requirements for production
    timing: Before Milestone C
    approval: JROC or designated authority

analysis:
  analysis_of_alternatives:
    acronym: AoA
    purpose: Compare alternatives to meet capability need
    conduct: Independent analysis
    timing: Before Milestone A
    
  cost_analysis_requirements_description:
    acronym: CARD
    purpose: Document cost, schedule, performance estimates
```

## Key Performance Parameters (KPPs)

```yaml
kpp_definition: Minimum operational capability for effectiveness
cardinality: Typically 3-5 KPPs per program
threshold: Minimum acceptable value
objective: Desired value

mandatory_kpps:
  - Force protection (if applicable)
  - Net-ready (if applicable)
  - Energy (if applicable)
  - Survivability (if applicable)

examples_f35:
  - Mission radius
  - Logistics footprint
  - Sortie generation rate
  - Signature (stealth)
```

## Milestone Reviews

### Milestone A

```yaml
purpose: Entry into Technology Maturation & Risk Reduction
authorization: Milestone Decision Authority (MDA)

requirements:
  - Approved ICD
  - AoA completed
  - Technology readiness assessment
  - Cost estimate (Independent Cost Estimate - ICE)
  - Approved acquisition strategy
  
exit_criteria:
  - Technology maturation plan
  - Risk reduction activities defined
  - Demonstrated feasibility
```

### Milestone B

```yaml
purpose: Entry into Engineering & Manufacturing Development
authorization: MDA (typically USD(A&S) for ACAT I)

requirements:
  - Approved CDD
  - Technology Readiness Level (TRL) 6 demonstrated
  - Preliminary design review completed
  - Independent cost estimate
  - Systems engineering plan
  - Test & evaluation master plan
  
exit_criteria:
  - Critical technologies demonstrated in relevant environment
  - Design is technically sound
  - Manufacturing processes assessed
  - Cost estimate is reasonable
  - Program structure is executable
  
document: Acquisition Program Baseline (APB)
```

### Milestone C

```yaml
purpose: Entry into Production & Deployment
authorization: MDA

requirements:
  - Approved CPD
  - Critical Design Review completed
  - Developmental testing complete
  - Manufacturing processes demonstrated
  - Independent cost estimate
  
exit_criteria:
  - Design is stable
  - Manufacturing processes mature
  - Operational effectiveness demonstrated
  - Cost estimates valid
  
decisions:
  - Low-Rate Initial Production (LRIP) quantity
  - IOT&E plan
  - Full-Rate Production criteria
```

### Full-Rate Production Decision

```yaml
purpose: Commit to production at economical rates
authorization: MDA

requirements:
  - IOT&E completed (or waived)
  - Operational effectiveness confirmed
  - Production processes demonstrated
  - Cost estimates validated
  - Systems training established

f35_example:
  milestone_c: 2011
  frp_approval: March 2024
  gap_reasons:
    - Development delays
    - Testing requirements
    - Performance issues
    - Cost growth
```

## Technology Readiness Levels (TRL)

```yaml
source: NASA, adopted by DoD (DoD Technology Readiness Assessment Guide)

scale:
  trl_1: Basic principles observed and reported
  trl_2: Technology concept and/or application formulated
  trl_3: Analytical and experimental critical function and/or characteristic proof-of-concept
  trl_4: Component and/or breadboard validation in laboratory environment
  trl_5: Component and/or breadboard validation in relevant environment
  trl_6: System/subsystem model or prototype demonstration in relevant environment
  trl_7: System prototype demonstration in operational environment
  trl_8: Actual system completed and qualified through test and demonstration
  trl_9: Actual system proven in operational environment

milestone_requirements:
  milestone_a: TRL 4-5 (plan to reach TRL 6)
  milestone_b: TRL 6 (demonstrated in relevant environment)
  milestone_c: TRL 7-8
  
f35_tr3_example:
  component: Integrated Core Processor (ICP)
  milestone_b_trl: TRL 6 claimed
  actual_status: Delays due to integration complexity
  resolution: TRL 8 achieved 2025
```

## Test and Evaluation

### Developmental Test & Evaluation (DT&E)

```yaml
conducted_by: Contractor and government integrated test team
purpose: Verify system meets technical specifications
timing: Throughout development

phases:
  component_testing: Subsystem verification
  system_testing: Integrated system verification
  qualification_testing: Environmental, reliability
```

### Operational Test & Evaluation (OT&E)

```yaml
conducted_by: Independent Operational Test Agency
purpose: Verify operational effectiveness and suitability
timing: Late EMD / LRIP

types:
  iot&e: Initial Operational Test & Evaluation
  follow_on_ot&e: After FRP decision
  
measures:
  operational_effectiveness: Mission accomplishment
  operational_suitability: Availability, compatibility
  survivability: Force protection
  
key_outputs:
  - Beyond Low-Rate Initial Production (BLRIP) report
  - Full-Rate Production recommendation
```

### Live Fire Test & Evaluation (LFT&E)

```yaml
purpose: Evaluate survivability against threat weapons
conducted: Throughout development
products:
  - LFT&E strategy
  - LFT&E report
  - vulnerability assessments
```

## Contract Types

### Cost-Reimbursement Contracts

```yaml
types:
  cost_plus_fixed_fee:
    acronym: CPFF
    fee: Fixed amount
    risk: Government bears cost risk
    
  cost_plus_incentive_fee:
    acronym: CPIF
    fee: Adjustable based on performance
    common: Development programs
    
  cost_plus_award_fee:
    acronym: CPAF
    fee: Subjective award based on performance
    
applicability: Research, development, uncertain requirements
examples:
  - F-35 SDD: CPIF
  - Technology maturation: CPFF
```

### Fixed-Price Contracts

```yaml
types:
  firm_fixed_price:
    acronym: FFP
    price: Set, no adjustment
    risk: Contractor bears cost risk
    
  fixed_price_incentive:
    acronym: FPIF
    price: Adjustable within range
    common: Production programs
    
  fixed_price_economic_price_adjustment:
    acronym: FPEPA
    price: Adjusted for economic factors

applicability: Production, well-defined requirements
examples:
  - F-35 LRIP/FRP: FPIF
  - C-130 production: FFP
```

### Other Contract Types

```yaml
indefinite_delivery_indefinite_quantity:
  acronym: IDIQ
  purpose: Multiple delivery orders over time
  examples: THAAD interceptors, missile production

time_and_materials:
  acronym: T&M
  purpose: Services with uncertain scope
  limitation: Not for major acquisitions
```

## Cost Estimation

### Independent Cost Estimates

```yaml
ice: Independent Cost Estimate
conducted_by: Cost Assessment and Program Evaluation (CAPE)
timing: Major milestones
purpose: Validate program office estimates

vice: 
  name: Independent Cost Estimate / Cost Analysis Requirements Description
  timing: Milestone B and C
  
grassley_report:
  trigger: Nunn-McCurdy breach
  purpose: Root cause analysis
```

### Cost Growth Metrics

```yaml
nunn_mcurdy_breach:
  threshold:
    significant: ≥15% unit cost growth (current) or ≥25% (original)
    critical: ≥25% unit cost growth (current) or ≥50% (original)
  consequence:
    significant: Report to Congress, review
    critical: Certification required or termination

examples:
  f35: Multiple significant breaches (2000s-2010s)
  ch53k: Significant breach 2017
```

## Program Management

### Program Manager Authority

```yaml
document: DOD Directive 5000.01
key_principles:
  - Single point of accountability
  - Authority commensurate with responsibility
  - Programmatic decision-making at lowest level
  
PM_responsibilities:
  - Cost
  - Schedule
  - Performance
  - Sustainment
  - Risk management
```

### Systems Engineering

```yaml
standard: MIL-STD-881 (Work Breakdown Structure)
process: Technical reviews (ASR, SRR, PDR, CDR, etc.)
plan: Systems Engineering Plan (SEP)
traceability: Requirements flow-down and verification
```

### Risk Management

```yaml
process:
  - Risk identification
  - Risk assessment (probability/impact)
  - Risk mitigation planning
  - Risk monitoring

categories:
  - Technical/performance
  - Schedule
  - Cost
  - Programmatic
```

---

*Last Updated: March 2026 | Sources: DoDI 5000.02, DAU Gold Book, GAO reports*
