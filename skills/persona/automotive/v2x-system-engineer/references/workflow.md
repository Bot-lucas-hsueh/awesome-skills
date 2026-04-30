## § 8 Standard Workflow

### Phase 1: V2X System Requirements & Architecture
```
1.1 Application Use Case Analysis
  - [ ] Define V2X applications (PCW, EEBL, GLOSA, CPM, platooning)
  - [ ] Map each application to latency/range/reliability requirements (SAE J2945)
  - [ ] Identify which applications require direct (PC5/DSRC) vs. network (V2N) communication
  - [✓ Done] Output: V2X Application Requirements Document with performance targets
  - [✗ FAIL] If any safety application requires > 100ms latency via V2N → redesign for direct comm

1.2 Technology & Architecture Selection
  - [ ] Select communication technology (DSRC or C-V2X) based on region and infrastructure
  - [ ] Define OBU architecture (DSRC modem, C-V2X modem, GNSS, security module)
  - [ ] Define RSU infrastructure requirements (if V2I applications included)
  - [✓ Done] Output: V2X System Architecture Document with technology rationale
```

### Phase 2: Communication Stack Implementation
```
2.1 MAC/PHY Configuration
  - [ ] DSRC: configure 802.11p channel bandwidth (10 MHz), OFDM modulation, data rate (6-27 Mbps)
  - [ ] C-V2X: configure sidelink resource pool; Mode 4 (autonomous) vs. Mode 3 (scheduled)
  - [ ] DCC: configure CBR threshold (40% warning, 60% congestion), transmit power reduction
  - [✓ Done] Output: MAC/PHY Configuration Specification

2.2 Application Message Design
  - [ ] Implement BSM Part 1 (mandatory fields) and required Part 2 extensions
  - [ ] Implement SPAT + MAP messages for equipped intersections
  - [ ] Integrate GPS/IMU data pipeline to BSM with latency < 20ms
  - [ ] Implement ASN.1 UPER encoding for SAE J2735 message set
  - [✓ Done] Output: Message Implementation Specification with timing analysis
  - [✗ FAIL] If BSM generation latency > 30ms → optimize GPS-to-message pipeline

2.3 Security Integration
  - [ ] Integrate IEEE 1609.2 signing for all transmitted messages
  - [ ] Configure SCMS certificate enrollment and pseudonym refresh policy
  - [ ] Implement CRL (Certificate Revocation List) checking
  - [✓ Done] Output: V2X Security Architecture with certificate policy document
```

### Phase 3: Deployment Testing & Validation
```
3.1 OBU-RSU Interoperability Testing
  - [ ] Execute DSRC/C-V2X conformance test suite (OBU-to-OBU and OBU-to-RSU)
  - [ ] Verify BSM message reception and processing across vendor combinations
  - [✓ Done] Output: Interoperability test report with pass/fail by feature

3.2 Field Performance Testing
  - [ ] PDR vs. distance measurement (highway LOS, urban NLOS, intersection)
  - [ ] Latency measurement (GPS capture to application receipt, end-to-end)
  - [ ] Channel load measurement (CBR at peak traffic density)
  - [ ] Validate results against SAE J2945/1 requirements
  - [✓ Done] Output: Field Test Report with SAE J2945 compliance verification
```
