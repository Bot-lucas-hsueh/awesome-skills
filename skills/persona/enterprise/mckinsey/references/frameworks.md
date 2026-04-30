# McKinsey Frameworks Reference

Complete library of McKinsey problem-solving and communication frameworks.

## Table of Contents
1. [Problem-Solving Frameworks](#problem-solving-frameworks)
2. [Communication Frameworks](#communication-frameworks)
3. [Strategy Frameworks](#strategy-frameworks)
4. [Operational Frameworks](#operational-frameworks)
5. [Organizational Frameworks](#organizational-frameworks)

---

## Problem-Solving Frameworks

### MECE (Mutually Exclusive, Collectively Exhaustive)

**Definition**: A principle for organizing information where categories don't overlap and cover all possibilities.

**Why It Matters**:
- Ensures complete analysis without duplication
- Enables efficient work allocation
- Builds client confidence in thoroughness

**Common MECE Structures**:

```
1. Revenue Breakdown
   Revenue = Price × Volume
   Volume = Market Size × Market Share

2. Cost Breakdown
   Costs = Fixed Costs + Variable Costs
   Variable Costs = Unit Cost × Units

3. Customer Segmentation
   Customers = Enterprise + SMB + Consumer
   
4. Geographic Breakdown
   Global = North America + Europe + Asia + RoW

5. Time-Based
   Total = Year 1 + Year 2 + Year 3 + ...
```

**MECE Testing Questions**:
- Are any items in more than one category? (Mutual exclusivity)
- If I add up all categories, do I get the total? (Collective exhaustiveness)

---

### Issue Trees

**Purpose**: Break complex problems into manageable components.

**Structure**:
```
                    [PROBLEM STATEMENT]
                           |
        ┌─────────────────┼─────────────────┐
        |                 |                 |
   [Branch 1]        [Branch 2]        [Branch 3]
        |                 |                 |
   ┌────┴────┐      ┌────┴────┐      ┌────┴────┐
   |         |      |         |      |         |
[Sub]     [Sub]  [Sub]     [Sub]  [Sub]     [Sub]
```

**Types of Issue Trees**:

**1. Diagnostic (Problem-Based)**
```
"Why are profits declining?"
Profit = Revenue - Costs
├── Revenue Problems
│   ├── Price issues
│   │   └── Competition, elasticity
│   └── Volume issues
│       ├── Market share loss
│       └── Market decline
└── Cost Problems
    ├── Fixed cost increases
    └── Variable cost increases
```

**2. Prescriptive (Solution-Based)**
```
"How to increase profits?"
Increase Profit
├── Increase Revenue
│   ├── Raise prices
│   ├── Increase volume
│   │   ├── Acquire new customers
│   │   └── Increase purchase frequency
│   └── Improve product mix
└── Decrease Costs
    ├── Reduce fixed costs
    │   ├── Headcount optimization
    │   └── Asset efficiency
    └── Reduce variable costs
        ├── Procurement savings
        └── Process efficiency
```

---

### Hypothesis-Driven Problem Solving

**The McKinsey Approach**:
```
Day 1 Hypothesis → Data Gathering → Test/Refine → Solution
```

**Characteristics of Good Hypotheses**:
1. **Testable**: Can be proven true or false with data
2. **Specific**: Not vague generalizations
3. **Actionable**: Leads to clear next steps
4. **Non-obvious**: Adds value beyond common knowledge

**Hypothesis Template**:
> "We believe [specific outcome] is caused by [specific driver], 
> which can be tested by [data source/method]."

**Example**:
> "We believe the 15% profit decline is driven by a 20% price 
> reduction in the European market (not volume decline), which 
> can be tested by analyzing regional P&L data and competitor 
> pricing moves."

---

## Communication Frameworks

### The Pyramid Principle (Barbara Minto)

**Core Concept**: Start with the answer, then support with logic.

**Structure**:
```
                    [ANSWER]
                       |
      ┌───────────────┼───────────────┐
      |               |               |
[ARGUMENT 1]    [ARGUMENT 2]    [ARGUMENT 3]
      |               |               |
  [EVIDENCE]      [EVIDENCE]      [EVIDENCE]
```

**Rules**:
1. **Vertical Logic**: Ideas at one level answer questions raised at the level above
2. **Horizontal Logic**: Arguments at same level are MECE and ordered logically
3. **Top-Down Flow**: Main point first, then supporting details

**SCQA Framework**:

| Element | Purpose | Example |
|---------|---------|---------|
| **S**ituation | Establish context | "Our client is a market leader with strong margins" |
| **C**omplication | Describe the problem | "However, new entrants are gaining share with lower prices" |
| **Q**uestion | State the question | "How should we respond to protect market position?" |
| **A**nswer | Provide recommendation | "We recommend launching a fighter brand while premiumizing core offering" |

---

### The 80/20 Rule (Pareto Principle)

**Concept**: 80% of effects come from 20% of causes.

**Applications**:
- Prioritizing analysis focus
- Identifying key drivers
- Resource allocation
- Time management

**Example**:
```
Profit decline analysis:
- 80% of profit decline comes from 20% of product lines
- Focus deep-dive on those key products first
```

---

## Strategy Frameworks

### Porter's Five Forces

**Purpose**: Analyze industry competitive dynamics.

```
           [RIVALRY AMONG EXISTING COMPETITORS]
                         |
    ┌────────────┬───────┴───────┬────────────┐
    |            |               |            |
[THREAT OF   [BARGAINING    [BARGAINING   [THREAT OF
NEW ENTRANTS]  POWER OF      POWER OF      SUBSTITUTE
               SUPPLIERS]    BUYERS]       PRODUCTS]
```

**Force 1: Threat of New Entrants**
- Barriers to entry (capital, regulation, brand)
- Economies of scale
- Switching costs

**Force 2: Bargaining Power of Suppliers**
- Supplier concentration
- Differentiation of inputs
- Switching costs

**Force 3: Bargaining Power of Buyers**
- Buyer concentration
- Price sensitivity
- Switching costs

**Force 4: Threat of Substitutes**
- Availability of alternatives
- Price-performance trade-off
- Switching costs

**Force 5: Rivalry Among Existing Competitors**
- Number and balance of competitors
- Industry growth rate
- Exit barriers

---

### BCG Growth-Share Matrix

**Purpose**: Portfolio analysis and resource allocation.

```
          MARKET GROWTH RATE
          
          HIGH              LOW
      ┌──────────┬──────────┐
HIGH  │   STAR   │  CASH    │
      │          │   COW    │
RELATIVE     ├──────────┼──────────┤
MARKET  LOW   │ QUESTION │   DOG    │
SHARE         │   MARK   │          │
      └──────────┴──────────┘
```

| Category | Characteristics | Strategy |
|----------|-----------------|----------|
| **Stars** | High growth, high share | Invest for growth |
| **Cash Cows** | Low growth, high share | Harvest, maintain |
| **Question Marks** | High growth, low share | Selective investment |
| **Dogs** | Low growth, low share | Divest/exit |

---

### Ansoff Matrix

**Purpose**: Growth strategy options.

```
               PRODUCTS
          
          EXISTING        NEW
      ┌──────────┬──────────┐
EXIST │ MARKET   │ PRODUCT  │
ING   │PENETRATION|DEVELOPMENT│
      ├──────────┼──────────┤
NEW   │ MARKET   │DIVERSIFI-│
      │DEVELOPMENT│ CATION  │
      └──────────┴──────────┘
```

| Strategy | Description | Risk Level |
|----------|-------------|------------|
| Market Penetration | Sell more to existing customers | Low |
| Product Development | New products to existing markets | Medium |
| Market Development | Existing products to new markets | Medium |
| Diversification | New products to new markets | High |

---

## Operational Frameworks

### Value Chain Analysis

**Purpose**: Identify sources of competitive advantage in operations.

```
PRIMARY ACTIVITIES:
Inbound → Operations → Outbound → Marketing → Service
Logistics          Logistics    & Sales
    
SUPPORT ACTIVITIES:
Firm Infrastructure
Human Resource Management
Technology Development
Procurement
```

**Margin**: Value created minus cost of creating value

---

### Profitability Tree

**Purpose**: Decompose profit drivers.

```
                    PROFIT
                       |
        ┌──────────────┴──────────────┐
        |                             |
    REVENUE                        COSTS
        |                             |
   ┌────┴────┐                  ┌─────┴──────┐
   |         |                  |            |
 Price    Volume            Fixed      Variable
           |                Costs       Costs
      ┌────┴────┐             |            |
      |         |         ┌───┴───┐    ┌───┴───┐
   Market   Market        Labor  Overhead  COGS  Other
   Share    Size          Costs           (per unit × volume)
```

---

## Organizational Frameworks

### McKinsey 7S Framework

**Purpose**: Assess organizational effectiveness and alignment.

```
            [SHARED VALUES]
                 |
    ┌────────────┼────────────┐
    |            |            |
[STRATEGY]  [STRUCTURE]  [SYSTEMS]
    |            |            |
┌───┴───┐   ┌───┴───┐   ┌───┴───┐
|       |   |       |   |       |
[SKILLS]    [STAFF]    [STYLE]
```

**Hard S's** (Easier to change):
- Strategy
- Structure
- Systems

**Soft S's** (Harder to change):
- Shared Values
- Skills
- Staff
- Style

---

### Change Management Framework

**McKinsey's Four Building Blocks of Change**:

1. **Role Modeling**
   - Leaders demonstrate desired behaviors
   - Visible commitment from top

2. **Fostering Understanding and Conviction**
   - Clear communication of why
   - Address concerns and resistance

3. **Reinforcing with Formal Mechanisms**
   - Align incentives and rewards
   - Update processes and systems

4. **Developing Talent and Skills**
   - Training and capability building
   - Support during transition

---

## Framework Selection Guide

| Situation | Recommended Framework |
|-----------|----------------------|
| Profit decline | Profitability Tree + Issue Tree |
| New market entry | Porter's 5 Forces + Market Sizing |
| Growth strategy | Ansoff Matrix + BCG Matrix |
| Operational improvement | Value Chain + Cost Curve |
| Organizational transformation | 7S Framework + Change Management |
| Merger integration | 7S + Integration Checklist |
| Cost reduction | Zero-based Budgeting + Activity Analysis |
| Pricing strategy | Elasticity Analysis + Competitive Positioning |

---

*Reference: Compiled from McKinsey training materials and published frameworks*
