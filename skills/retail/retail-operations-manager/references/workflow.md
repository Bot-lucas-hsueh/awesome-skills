# Troubleshooting Guide

## 8.1 Inventory Discrepancies & Shrink

### Unexpected Shrink Spike

**Symptoms:** Shrink rate exceeds historical baseline by >0.5% in a reporting period.

**Diagnosis:**
1. Pull exception reports from POS — look for unusual voids, refunds, no-sale transactions
2. Cross-reference inventory counts against receiving logs for the period
3. Check for compliance failures in EAS tag deactivation at checkout
4. Review security camera footage for high-theft areas (cosmetics, electronics, apparel)
5. Verify supplier packing slips match PO quantities received

**Solutions:**
- Conduct surprise spot counts in top shrink categories
- Reinforce deactivation protocol at registers — use test magnets to verify
- Increase theft-deterrent measures: spider wraps on high-value items, locked cases
- If internal theft suspected, implement stricter cash handling controls and discrete monitoring
- File police report for confirmed theft over threshold ($500+)

### Perpetual Inventory Accuracy Below 95%

**Symptoms:** System inventory doesn't match physical count. Frequent overselling or phantom stock.

**Diagnosis:**
1. Identify root cause: receiving errors, damage not written off, process deviations
2. Check receiving procedures — are POs being matched to shipment before shelving?
3. Review cycle count results by category — which SKUs consistently have large variances?
4. Audit stock room organization — is misplacement common?

**Solutions:**
- Implement mandatory cycle count schedule: A-class items weekly, B-class monthly, C-class quarterly
- Add barcode scanning at receiving to ensure PO-to-receipt matching
- Establish damage write-off procedure within 24 hours of discovery
- Use RFID for real-time inventory tracking in high-value sections
- Set inventory accuracy KPI and hold department leads accountable

## 8.2 Omnichannel Fulfillment Issues

### BOPIS (Buy Online Pick-Up In-Store) Delays

**Symptoms:** Customers reporting long wait times or "item not available" at pickup.

**Diagnosis:**
1. Check fulfillment queue age — are items being picked within SLA (typically 2-4 hours)?
2. Verify store associate picking productivity — is the task properly assigned and prioritized?
3. Review inventory allocation — is the BOPIS-allocated inventory actually available on shelf?
4. Check hold area organization — is the pickup zone clearly marked and staffed?

**Solutions:**
- Implement store associate picking app with prioritized queue and in-aisle navigation
- Set 2-hour hold expiration alerts to prevent customer no-shows
- Cross-train fulfillment associates and stagger shifts for peak hour coverage
- Add real-time inventory accuracy check before presenting BOPIS availability online
- If delay exceeds SLA, automatically notify customer via SMS with revised pickup time

### Ship-From-Store Order Errors

**Symptoms:** Orders shipped from store arrive wrong, damaged, or missing items.

**Diagnosis:**
1. Review packing slip accuracy — does the label match contents?
2. Check carrier scan events — was the package scanned at origin?
3. Audit packaging standards — are items adequately protected?
4. Verify store-to-DC transfer procedures for SFS-eligible items

**Solutions:**
- Require packing slip sign-off by a second associate before handoff to carrier
- Use standardized poly mailer sizes per item category to reduce movement in transit
- Implement pre-shipment photo capture of packed orders for dispute resolution
- Train all SFS stores on hazmat (cosmetic liquids) shipping compliance

## 8.3 Cash Handling & POS Issues

### Cash Shortage at End of Shift

**Symptoms:** Cash drawer totals are less than expected based on sales transactions.

**Diagnosis:**
1. Reconcile POS transaction log against cash drawer count by payment type
2. Look for unrecorded voids, discounts, or no-sale events
3. Check safe counts — was cash stored correctly at end of previous shift?
4. Review manager override log for suspicious activity

**Solutions:**
- Implement dual-control cash handling: two associates count and sign off on safe drops
- Install smart safes with auto-reconciliation to eliminate manual counting errors
- Require managers to review exception report (voids, no-sales, discounts) before shift close
- If pattern persists, conduct discrete investigation for potential internal theft

### POS System Offline

**Symptoms:** Registers unable to process transactions, system unresponsive.

**Diagnosis:**
1. Check network connectivity — is the store internet/WAN down?
2. Verify POS server status — has the back-office system crashed?
3. Check if it's a single register or all registers affected
4. Review recent IT changes or updates that may have caused the outage

**Solutions:**
- Activate manual backup procedures: paper slips with customer info, authorize cards via phone
- Switch to mobile POS (Square, Shopify POS) on backup iPad if available
- Contact IT support with error logs from affected registers
- Document downtime duration and transaction log for reconciliation once restored
- Review outage with IT to implement redundancy: backup ISP or local POS mode

## 8.4 Store Operations

### Opening Procedures Not Completed On Time

**Symptoms:** Store not ready by opening time — alarms still on, displays not set, POS not logged in.

**Diagnosis:**
1. Review opening checklist — is it realistic for the time allocated?
2. Check associate arrival times vs. scheduled times
3. Identify bottleneck tasks: alarm disarm, display setup, cashier login
4. Review previous week's opening times for patterns

**Solutions:**
- Assign clear roles at opening: one person on alarm/security, one on displays, one on POS
- Pre-stage the night before: displays partially set, POS logged in, till cash ready
- Stagger arrival times so key tasks can begin 30 minutes before official open
- Set opening readiness KPI and address chronic delays with the opening team lead

### Excessive Customer Wait Times

**Symptoms:** Customers leaving without purchasing due to long checkout or service queues.

**Diagnosis:**
1. Calculate transactions per labor hour (TPLH) — is labor aligned to traffic patterns?
2. Observe peak hours — when do queues form and how long do they last?
3. Check number of open registers vs. customer volume
4. Review associate checkout efficiency — are transaction times above benchmark (90 seconds)?

**Solutions:**
- Implement traffic-count scheduling: align labor to hourly customer traffic data
- Deploy queue management system with digital display showing estimated wait time
- Cross-train fitting room and floor associates to support checkout during peaks
- Implement mobile checkout (Shopify POS on iPad) to enable checkout anywhere in store
- Set maximum queue length trigger to call additional registers

## 8.5 Safety & Compliance

### Workplace Injury

**Symptoms:** Associate reports injury (slip, fall, lifting strain, equipment-related).

**Diagnosis:**
1. Secure the scene — don't move equipment causing hazard
2. Administer first aid / call for medical assistance as needed
3. Document immediately: what happened, where, when, witnesses
4. Preserve any equipment, flooring, or conditions involved

**Solutions:**
- Complete OSHA Form 301 (Incident Report) within 24 hours
- Notify HR and safety manager immediately
- Investigate root cause within 48 hours — was it procedure, equipment, or environment?
- Implement corrective action: equipment repair/replacement, procedure update, retraining
- Review OSHA recordability criteria to determine if incident must be logged on OSHA 300

### Fire Safety System Malfunction

**Symptoms:** Fire alarm sounds without fire, sprinkler activation, or fire extinguisher missing/discharged.

**Diagnosis:**
1. Evacuate and call fire department if genuine alarm or smoke detected
2. If false alarm: check sprinkler heads for accidental activation, pull station tampering
3. Verify fire panel zone and which devices triggered the alarm
4. Check recent construction or maintenance that may have damaged wiring

**Solutions:**
- Test fire alarm system monthly — document results
- Recharge/replace discharged extinguishers within 24 hours
- Seal and lock pull stations to prevent tampering
- Schedule annual inspection by certified fire safety contractor
- Maintain fire extinguisher inspection logs per NFPA 10 requirements
