# Regulatory Landscape

## Overview

Uber operates in a complex regulatory environment across 70+ countries. The primary regulatory challenges center on:
- Worker classification (independent contractor vs. employee)
- Market competition and antitrust
- Data privacy and security
- Local transportation regulations

---

## Worker Classification

### United States

#### California AB5 (Assembly Bill 5) - 2019

| Aspect | Detail |
|--------|--------|
| **Enacted** | September 2019 |
| **Test** | ABC Test (strict three-part standard) |
| **Impact** | Would classify gig workers as employees |

**ABC Test Requirements:**
To classify as independent contractor, company must prove:
- **(A)** Worker is free from company control
- **(B)** Worker performs work outside company's usual business
- **(C)** Worker has independently established trade

#### California Proposition 22 - 2020

| Aspect | Detail |
|--------|--------|
| **Passed** | November 2020 (58% approval) |
| **Backed by** | Uber, Lyft, DoorDash, Instacart |
| **Effect** | Exempts app-based drivers from AB5 |

**Prop 22 Requirements:**
- Drivers remain independent contractors
- Minimum earnings guarantee (120% of minimum wage for "engaged time")
- Healthcare subsidies for qualifying drivers
- Accident insurance coverage
- Rest period requirements

**Legal Challenges:**
- 2021: CA Superior Court ruled Prop 22 unconstitutional
- 2023: Appeals court reversed, upheld Prop 22
- 2024: California Supreme Court upheld Prop 22 as constitutional

#### Federal Developments (2024-2025)

| Regulation | Detail |
|------------|--------|
| **DOL Rule (2024)** | Revised "economic reality" test |
| **Factors** | Six equally-weighted factors |
| **Effect** | Makes classification as employee more likely |

### United Kingdom

#### Uber BV v. Aslam (2021)

| Aspect | Detail |
|--------|--------|
| **Date** | February 19, 2021 |
| **Court** | UK Supreme Court |
| **Ruling** | Drivers are "workers" (intermediate category) |

**Implications:**
- 70,000+ UK drivers entitled to:
  - National Minimum Wage
  - Paid holiday (5.6 weeks/year)
  - Rest breaks
  - Pension auto-enrollment
  - Whistleblower protections

**Key Court Findings:**
1. Uber sets fares (controls earnings)
2. Uber sets contract terms unilaterally
3. Uber constrains ride requests
4. Uber monitors service via ratings
5. Uber can terminate drivers

**Working Time Definition:**
Drivers are "working" when:
- Logged into app
- Within authorized territory
- Ready and willing to accept assignments

### European Union

#### Platform Work Directive - 2023

| Aspect | Detail |
|--------|--------|
| **Adopted** | 2023 |
| **Implementation** | 2024-2026 (member states) |
| **Goal** | Improve working conditions for platform workers |

**Key Provisions:**
- Presumption of employment relationship
- Algorithm transparency requirements
- Human review of automated decisions
- Data protection for workers
- Portability of ratings

### Other Jurisdictions

| Country | Status |
|---------|--------|
| **Australia** | Fair Work Commission reviewing classification |
| **Canada** | Provincial variations; Ontario has minimum wage for drivers |
| **India** | Social security extended to gig workers (2020) |
| **Brazil** | Labor rights extended to app-based drivers |

---

## Data Privacy

### GDPR (European Union)

| Requirement | Uber Implementation |
|-------------|---------------------|
| **Lawful basis** | Contract performance, legitimate interest |
| **Data minimization** | Collect only necessary data |
| **Transparency** | Privacy policy, in-app disclosures |
| **User rights** | Access, deletion, portability |
| **Breach notification** | 72-hour reporting requirement |

### CCPA/CPRA (California)

| Right | Description |
|-------|-------------|
| **Know** | What personal information is collected |
| **Delete** | Request deletion of personal information |
| **Opt-out** | Sale/sharing of personal information |
| **Non-discrimination** | Equal service regardless of privacy choices |

### Notable Data Incidents

| Incident | Date | Impact |
|----------|------|--------|
| **2016 Breach** | 2016 (disclosed 2017) | 57M users and drivers affected |
| **Fine (UK)** | 2018 | £385,000 penalty |
| **Fine (EU)** | 2022 | €10M fine for data protection violations |

---

## Competition and Antitrust

### Key Cases

| Jurisdiction | Issue | Outcome |
|--------------|-------|---------|
| **Singapore (2018)** | Collusion with Grab | $4.86M fine |
| **Philippines** | Anti-competitive practices | Fines imposed |
| **Colombia** | Unfair competition | Ordered to cease operations (later reversed) |
| **France** | Unfair competition (taxis) | €180,000+ damages |

### London License Battles

| Year | Issue | Outcome |
|------|-------|---------|
| 2017 | Operating license renewal denied | 15-month probationary license |
| 2019 | License renewal denied | Restored on appeal |
| 2022 | License extended | 30-month extension with conditions |

---

## Insurance and Safety

### Insurance Model

| Scenario | Coverage |
|----------|----------|
| **App off** | Driver's personal insurance |
| **App on, no trip** | Uber contingent liability coverage |
| **En route to pickup** | Uber commercial coverage |
| **Trip in progress** | Uber commercial coverage ($1M liability) |

### Safety Features

| Feature | Description |
|---------|-------------|
| **Share My Trip** | Real-time location sharing |
| **Emergency Button** | Direct 911 contact |
| **Driver Screening** | Background checks |
| **PIN Verification** | Confirm correct driver |
| **Audio Recording** | Optional trip recording |

---

## Compliance Best Practices

### For Engineering

1. **Privacy by Design**
   - Data minimization in feature engineering
   - Anonymization where possible
   - Access controls and audit logging

2. **Algorithm Transparency**
   - Document decision logic
   - Enable human review
   - Avoid discriminatory outcomes

3. **Regulatory Monitoring**
   - Track local law changes
   - Engage legal early in design
   - Build flexibility for compliance changes

---

## References

- [UK Supreme Court Ruling](https://www.supremecourt.uk/cases/uksc-2019-0029.html)
- [California AB5 Text](https://leginfo.legislature.ca.gov/)
- [EU Platform Work Directive](https://eur-lex.europa.eu/)
