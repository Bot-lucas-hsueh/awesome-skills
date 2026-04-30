# Stripe Product Changelog 2025

## February 2026

### Company Updates
- **$159B Valuation** — New tender offer for employee liquidity
- Backed by Thrive Capital, Coatue, a16z
- Stripe also repurchasing shares with company capital
- "Remained robustly profitable" — Collison brothers

## 2025 Annual Highlights

### Financial Milestones
- **$1.9T Payment Volume** — 34% YoY growth
- **1.6% of Global GDP** — Equivalent economic output
- **Revenue Suite** — On track for $1B annual run rate
- **90% Dow Jones** — Companies using Stripe
- **80% Nasdaq 100** — Companies using Stripe
- **5M+ Businesses** — Served directly or via platforms

### Product Launches (350+ updates in 2025)

## Q4 2025 Updates

### Billing
- **Test Clock Support** — Added to existing test mode subscriptions via Dashboard
- **Credit Grant Rules** — Apply credits to specific prices, define priority
- **Usage Event Aggregation** — Reduced from 3 minutes to 30 seconds
- **Meter Data Export** — Export via SDP and Sigma

### Tax
- **Product Tax Code Search** — For Connect users (preview)
- **US Import Tax** — Tax collection for physical goods from outside US

### Issuing
- **Fraud Signals** — Better fraud decisions for Issuing programs

### Terminal
- **Poland Availability** — Terminal now available in Poland

### Capital
- **Embedded Components** — Customize and embed financing programs (preview)

## Q3 2025 Updates

### Stripe Tour New York (September)

#### Billing & AI
- **LLM Token Billing** (preview) — Bill for AI model usage
- **Hybrid Pricing Models** — Rate cards, license fees, credits
- **Dimensional Pricing** — Bill by model type, request size, speed
- **Real-time Credit Burning** — Live consumption with alerts
- **Meter Usage Analytics API** — Real-time aggregated data

#### Invoicing
- **Partial Payments** — Accept partial payments via Dashboard and API

#### Sigma & Data Pipeline
- **Export Customizations** — Select data and reports needed
- **Subscription Pricing** — Purchase via subscription for cost predictability

#### Tax
- **102 Countries** — Expanding support for physical goods (early 2026)
- **Mexico Support** — Now available
- **Events & Ticketing** — New vertical support (preview)

#### AI Development
- **Embedded Sandboxes** — Stripe sandboxes inside AI platforms

## Q2 2025 Updates

### Billing
- **S3 Usage Events** — Record usage via Amazon S3 bucket, no code required
- **CSV Upload** — Record usage via Dashboard CSV upload
- **Void Invoice Restatement** — Credit grants restated when invoice voided

### Tax
- **Retail Delivery Fee** — Collection support added

### Capital
- **Platform Customization** — Embedded components for financing programs

## Q1 2025 Updates

### Major Product Themes

#### Revenue and Finance Automation
- **$500M+ Run Rate** — Passed milestone in February
- **300K+ Companies** — Using Stripe Billing
- **200M+ Subscriptions** — Active subscriptions managed

#### Global Expansion
- Terminal in Poland
- Tax in Mexico
- 102-country expansion announced

#### AI Integration
- Smart Retries improvements
- AI-powered revenue recovery
- LLM billing infrastructure

### Company Metrics
- **500M+ Daily API Requests**
- **$6.5B Revenue Recovered** — Via recovery tools in 2024
- **75% Top Marketplaces** — Using Stripe Connect

## 2024 Major Updates (Context)

### Bridge Acquisition (October 2024)
- **$1.1B** — Stripe's largest acquisition
- Stablecoin infrastructure for cross-border payments
- Accelerating crypto payment adoption

### USDC Reintroduction (April 2024)
- Crypto payments reintroduced after 2018 discontinuation
- Focus on USDC stablecoin
- Circle partnership

### Sessions 2024 (April)

#### Organizations
- Scaled businesses can manage multiple Stripe accounts
- Cross-account Sigma queries

#### Billing Enhancements
- Meters API for usage-based billing
- Automations for revenue recovery
- Entitlements API for feature access control
- Migration toolkit for subscription imports
- Advanced discounting logic
- Invoice Preview API

#### Tax Expansion
- 57 countries supported
- Tax overrides for custom rules
- Platform data import (Amazon, Shopify, eBay)

#### Reporting
- Google Play and App Store transaction import
- Revenue recognition consolidation

## Product Metrics Evolution

| Metric | 2024 | 2025 |
|--------|------|------|
| Payment Volume | $1.4T | $1.9T |
| Growth Rate | 38% | 34% |
| Countries | 46+ | 50+ |
| Billing Companies | N/A | 300K+ |
| Active Subscriptions | N/A | 200M+ |
| Revenue Suite ARR | $500M+ | ~$1B (projected) |

## API Changes

### Deprecations
- Legacy Charges API still supported but PaymentIntents preferred
- Some older webhook event formats (check docs)

### New Endpoints
- `/v1/billing/meters` — Usage-based billing
- `/v1/billing/meters/{id}/events` — Usage events
- Enhanced Connect endpoints for embedded components

### Version Updates
- API version 2024-XX and 2025-XX releases
- Check Stripe changelog for breaking changes

## Security Updates

### Dashboard
- **Passkeys** — Faster, more secure login (May 2024)

### Radar
- **Radar Assistant** — AI chatbot for rule creation (March 2024)

## Regional Expansion

### 2025 New Markets
- Poland (Terminal)
- Mexico (Tax)
- Gibraltar, Liechtenstein, Malaysia (Tax — coming soon)

### 2026 Announced
- 102 countries for physical goods tax

## Developer Experience

### SDK Updates
- Mobile SDK improvements
- React Native updates
- Python, Ruby, Node.js library updates

### Documentation
- Enhanced API reference
- More interactive examples
- AI-assisted docs (experimental)

---

*Last Updated: March 2026*
*Sources: stripe.com/changelog, stripe.com/blog, press releases*
