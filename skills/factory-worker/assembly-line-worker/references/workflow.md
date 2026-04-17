# Assembly Line Worker — Troubleshooting Guide

## Common Problems & Solutions

### Quality Defects

**Problem: Recurring defect at a specific station**
- Diagnosis: Isolate whether defect originates at your station or propagates from upstream
- Check: Verify you are following current revision work instructions
- Check: Inspect incoming components for damage or defects
- Check: Tool condition (worn fixtures, loose torque wrench)
- Escalation: Pull Andon, quarantine affected units, notify supervisor and quality

**Problem: Defective component from supplier**
- Diagnosis: Verify against part number on work instruction vs. actual component
- Check: Check bin label vs. physical part
- Check: Look for lot code or date code variations
- Action: Do not assemble; reject to quarantine bin; notify quality
- Prevention: Report pattern to supervisor (multiple defects from same lot)

**Problem: Missing fastener, part, or connector**
- Diagnosis: Confirm what is missing by comparing to work instruction
- Check: Was component included in kit?
- Check: Did previous station complete their work?
- Action: Do not continue assembly without required component; escalate via Andon
- Prevention: Verify kit completeness at station startup

### Takt Time Problems

**Problem: Consistently exceeding takt time**
- Diagnosis: Measure actual cycle time with stopwatch
- Check: Is there an unnecessary motion or step?
- Check: Are tools properly positioned at workstation?
- Check: Is ergonomic issue slowing you down?
- Escalation: Pull Andon; do not rush and risk quality
- Prevention: Report to supervisor for time study and line rebalancing

**Problem: Line stoppage at upstream station causing WIP buildup**
- Diagnosis: Confirm if problem is upstream (materials) or your station
- Action: If WIP is accumulating, communicate to supervisor
- Prevention: Good Andon practice upstream reduces downstream impact

**Problem: Material shortage at station**
- Diagnosis: Check bin level and kanban signal
- Action: Trigger kanban for restock; if no stock available, escalate via Andon
- Prevention: Monitor bin levels proactively; signal restock before empty

### Equipment Problems

**Problem: Torque wrench not achieving specified torque**
- Diagnosis: Check torque wrench calibration date sticker
- Action: Do not use out-of-calibration tool; return to tool crib
- Prevention: Verify calibration before each use; never bypass

**Problem: Poka-yoke fixture not engaging correctly**
- Diagnosis: Inspect fixture for wear, damage, or contamination
- Action: Do not bypass fixture; notify supervisor
- Prevention: Report fixture wear before it causes defects

**Problem: Conveyor malfunction**
- Diagnosis: Check for jam, sensor obstruction, or mechanical failure
- Action: Press emergency stop if safety risk; notify maintenance immediately
- Prevention: Clear debris from conveyor path during shift

### Communication Problems

**Problem: Shift handoff with incomplete work**
- Action: Complete current unit to safe stopping point
- Document: Write down exact status for incoming shift
- Communicate: Face-to-face handoff with incoming worker
- Prevention: Follow handoff checklist every shift

**Problem: Engineering change (ECN) affecting your station**
- Action: Stop using old work instructions immediately
- Source: Get new revision from supervisor or document control
- Verify: Confirm revision number matches what you received
- Prevention: Check for ECN notifications at every shift start
