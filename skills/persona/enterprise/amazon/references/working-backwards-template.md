# Working Backwards — PR/FAQ Template

> Source: *Working Backwards* by Colin Bryar & Bill Carr

---

## Overview

The Working Backwards process ensures customer focus before any resources are committed. The core artifact is the PR/FAQ — a press release and frequently asked questions document written as if the product has already launched.

**The Test:** If the press release is hard to write, the product probably isn't great.

---

## Press Release Template (1 Page)

```markdown
# [Product Name] — [Launch/Announcement Context]

*For Immediate Release*

## [Heading — Name the product in customer-centric terms]

### [Subheading — Who is it for and what does it do?]

[City, State] — [Date] — [Opening paragraph: 2-3 sentences describing 
the customer benefit in plain language. No jargon.]

## The Problem

[Describe the customer pain point. Be specific. Use customer language.]

## The Solution

[Describe how your product/service solves the problem. Focus on outcomes, 
not features.]

## Key Benefits

- **[Benefit 1]**: [Specific customer outcome]
- **[Benefit 2]**: [Specific customer outcome]
- **[Benefit 3]**: [Specific customer outcome]

## Quote from [Company Executive]

"[Quote expressing excitement and connecting to company mission. Should 
sound authentic, not corporate-speak.]"

## Quote from [Hypothetical Customer]

"[Customer testimonial describing their experience and specific benefits 
they received. Should sound like a real person, not marketing copy.]"

## Pricing and Availability

[Product/Service] is available starting [Date] at [Price/Access method].

## Call to Action

[Clear next step: Visit X, Download Y, Sign up for Z]

---

About [Company Name]
[2-3 sentences about the company]

Media Contact:
[Name, Email, Phone]
```

---

## FAQ Template (5 Pages)

### External FAQs (Customer-Facing)

```markdown
## External FAQs

### General Questions

**Q: What is [Product Name]?**
A: [Clear, concise definition in customer terms]

**Q: Who is [Product Name] for?**
A: [Target customer segments with specific use cases]

**Q: How much does it cost?**
A: [Pricing details, tiers, what's included]

**Q: How do I get started?**
A: [Clear onboarding steps]

### Feature Questions

**Q: [Feature-related question]?**
A: [Clear answer explaining the feature and benefit]

**Q: Can I [common customer request]?**
A: [Yes/no with explanation and alternatives if no]

### Comparison Questions

**Q: How is this different from [competitor/alternative]?**
A: [Differentiation without disparaging competition]

**Q: Should I switch from [current solution]?**
A: [Honest assessment of when this makes sense]

### Support Questions

**Q: What if I need help?**
A: [Support options: documentation, chat, phone, etc.]

**Q: Where can I learn more?**
A: [Resources: documentation, tutorials, community]
```

### Internal FAQs (Company-Facing)

```markdown
## Internal FAQs

### Strategic Questions

**Q: Why are we building this?**
A: [Strategic rationale, market opportunity, alignment with company goals]

**Q: What is the total addressable market?**
A: [Market size analysis with sources]

**Q: How does this fit with our existing products?**
A: [Product portfolio integration, cannibalization analysis]

### Technical Questions

**Q: What are the key technical challenges?**
A: [Engineering risks and mitigation strategies]

**Q: How will this scale?**
A: [Scalability plan and limits]

**Q: What dependencies do we have?**
A: [Internal and external dependencies with owners]

### Operational Questions

**Q: How will we support this?**
A: [Customer service plan, training, documentation]

**Q: What is the operational model?**
A: ["You build it, you run it" responsibilities, oncall]

**Q: How will we measure success?**
A: [Key metrics, targets, monitoring plan]

### Financial Questions

**Q: What is the P&L projection?**
A: [Revenue forecast, cost structure, timeline to profitability]

**Q: What are the key financial risks?**
A: [Sensitivity analysis, worst-case scenarios]

**Q: What resources are required?**
A: [Headcount, infrastructure, marketing budget]

### Go-to-Market Questions

**Q: What is the launch plan?**
A: [Phased rollout, beta program, general availability]

**Q: How will we acquire customers?**
A: [Marketing channels, partnerships, sales approach]

**Q: What is the pricing strategy?**
A: [Pricing model, competitive positioning, discount policy]

### Risk Questions

**Q: What could kill this product?**
A: [Key risks and mitigation plans]

**Q: What is our plan if we only achieve 50% of projections?**
A: [Contingency plans, pivot options]

**Q: What regulatory or compliance issues exist?**
A: [Legal review status, compliance requirements]
```

---

## Writing Tips

### For the Press Release

1. **Start with the customer, not the technology**
   - ❌ "Our new machine learning platform uses TensorFlow..."
   - ✅ "Customers can now predict inventory needs automatically..."

2. **Write for a general audience**
   - No acronyms without explanation
   - No "geek speak"
   - 8th-grade reading level

3. **Be specific about benefits**
   - ❌ "Faster performance"
   - ✅ "Reduce checkout time from 3 minutes to 30 seconds"

4. **Include authentic quotes**
   - Executive quote: Connect to company mission
   - Customer quote: Sound like a real person

5. **Keep it to one page**
   - Forces clarity and prioritization
   - If you can't explain it in one page, you don't understand it

### For the FAQ

1. **Anticipate hard questions**
   - Don't softball yourself
   - Include questions you'd rather not answer

2. **Be honest about what you don't know**
   - "We are still analyzing this and will have an answer by [date]"
   - Better than making up answers

3. **Address the risks directly**
   - Every product has risks
   - Hiding them doesn't make them go away

4. **Quantify when possible**
   - Specific numbers build credibility
   - Ranges are okay: "$10M-$20M addressable market"

---

## The Review Process

### Phase 1: Solo Draft (Few Hours)
- Product manager writes initial draft
- Many holes and unanswered questions are okay

### Phase 2: Manager/Peer Review
- Share with immediate manager
- 2-3 cross-functional peers
- Incorporate feedback, fill gaps

### Phase 3: Team Review
- 8-10 person cross-functional group
- Engineering, design, operations, finance, legal
- Identify major issues

### Phase 4: Leadership Review
- Present to decision maker
- May require multiple iterations
- Be prepared to answer deep questions

### Phase 5: Executive Review
- S-Team or equivalent for major initiatives
- Final approval to proceed

**Total timeline:** Days to months depending on scope

---

## Red Flags — When to Stop

The PR/FAQ process should expose weaknesses. Stop and reconsider if:

1. **Customer benefit is unclear** — Can't articulate in 2 sentences
2. **Differentiation is weak** — "Me too" product
3. **Unit economics don't work** — Can't see path to profitability
4. **Technical risks are unaddressed** — Key capabilities unproven
5. **Market is too small** — Can't reach meaningful scale
6. **Dependencies are unmanageable** — Requires 10+ teams to coordinate

---

## Historical Examples

### AWS S3 (2006)
```
Heading: Amazon S3 - Simple Storage Service Now Available

Problem: Storing and retrieving any amount of data requires expensive 
infrastructure, capacity planning, and operational overhead.

Solution: Simple Storage Service (S3) provides reliable, scalable storage 
infrastructure accessible via web services APIs.

Customer Benefit: Pay only for what you use, scale infinitely, no upfront 
capital expense.
```

### Amazon Prime (2005)
```
Heading: Introducing Amazon Prime - Unlimited Free Two-Day Shipping

Problem: Shipping costs and delivery times discourage online purchases.

Solution: Annual membership offering unlimited free two-day shipping 
for a flat fee.

Customer Benefit: Shop without thinking about shipping costs; get items 
in 2 days guaranteed.
```

### Kindle (2007)
```
Heading: Introducing Kindle - Wireless Reading Device

Problem: Physical books are heavy, take up space, and require trips 
to the store.

Solution: Wireless reading device with access to 90,000+ books, 
delivered in 60 seconds.

Customer Benefit: Carry thousands of books; instant delivery; 
readable in bright sunlight.
```

---

*Last Updated: 2026-03-21*
