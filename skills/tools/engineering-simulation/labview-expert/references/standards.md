# Standards & Reference

## 7.1 Official Documentation

- [NI LabVIEW Documentation](https://www.ni.com/docs/en-US/bundle/labview-page) - Official docs
- [LabVIEW Help](https://www.ni.com/manuals) - Detailed help system
- [NI Community - LabVIEW](https://forums.ni.com/t5/LabVIEW/ct-p/3009) - User forums
- [NI Learning Center](https://www.ni.com/learn) - Training resources

## 7.2 Configuration Reference

### Common VIs and Functions

| Category | VI/Function | Description |
|----------|-------------|-------------|
| Data Acquisition | DAQmx Create Task | Initialize NI-DAQmx |
| Data Acquisition | DAQmx Start Task | Start measurement |
| Data Acquisition | DAQmx Read | Read analog/digital |
| Instrument Control | VISA Open | Open serial/GPIB/USB |
| Instrument Control | VISA Write | Send command |
| Instrument Control | VISA Read | Read response |
| Signal Processing | FFT | Frequency analysis |
| Signal Processing | Filter | IIR/FIR filtering |
| Control | PID | PID controller |
| Control | LQR | Linear quadratic regulator |

### DAQmx Configuration

```
Task Configuration:
├── Physical Channel (dev1/ai0)
├── Terminal Config (RSE, NRSE, Diff)
├── Sample Rate (Hz)
├── Input Range (±10V, ±5V)
├── Trigger (Digital, Software)
└── Timing (On Demand, Hardware)
```

### Hardware Drivers

| Driver | Purpose |
|--------|---------|
| NI-DAQmx | DAQ hardware |
| NI-DeviceMatchers | Serial/USB |
| NI-VISA | Serial, GPIB, TCP/IP |
| NI-SCOPE | Oscilloscopes |
| NI-DCPower | Power supplies |

## 7.3 Common Commands

### Project Management

| Command | Description |
|---------|-------------|
| Create Project | New LabVIEW project |
| Save As | Save copy |
| Build Application | Create .exe |
| Build Specification | Configure build |

### Execution Control

| Command | Description |
|---------|-------------|
| Run | Execute VI |
| Stop | Halt execution |
| Highlight Execution | Debug mode |
| Probe | Monitor values |
| Breakpoint | Pause at point |

### Deployment

| Command | Description |
|---------|-------------|
| Run as Administrator | Elevated execution |
| RT Deployment | Deploy to RT target |
| FPGA Compile | Compile to bitfile |

## 7.4 Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| LabVIEW 2019 | Supported | LTS |
| LabVIEW 2020 | Supported | 64-bit improvements |
| LabVIEW 2021 | Supported | NXG integration |
| LabVIEW 2022 | Supported | New features |
| LabVIEW 2023 | Current | Recommended |
| LabVIEW 2024 | Latest | New development |

### Compatibility Notes

- **2021+**: NXG features merged
- **2022+**: 64-bit default
- **2023+**: New module integration