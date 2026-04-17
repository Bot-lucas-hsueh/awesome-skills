# Scenario Examples

## 9.1 Engineering Scenarios

### Data Acquisition System

**User:** "How to acquire temperature from a thermocouple?"

**Expert:**
> **DAQmx Setup:**
>
> 1. Create *DAQmx Task*
> 2. Add *TC Read* VI (Thermocouple Type J/K)
> 3. Configure: dev1/ai0, 100 Hz, ±1V range
> 4. Use *DAQmx Start* → *DAQmx Read* → *DAQmx Stop*
> 5. Wire to indicator or file

### Instrument Control

**User:** "How to read data from an oscilloscope?"

**Expert:**
> **VISA Setup:**
>
> 1. Use *VISA Find Resource* to locate instrument
> 2. *VISA Open* the session
> 3. *VISA Write*: `*IDN?` query
> 4. *VISA Read* response
> 5. Parse using *Scan From String*
> 6. Close VISA session

### Real-Time Control

**User:** "How to implement PID control?"

**Expert:**
> **PID Implementation:**
>
> 1. Use *PID VI* from Control palette
> 2. Configure: Kp, Ki, Kd parameters
> 3. Set output limits (0-100%)
> 4. Connect: Setpoint → PID → DAQ AO
> 5. Add feedback: AI → PID
> 6. Consider: Anti-windup, derivative filter

## 9.2 Industry Applications

| Industry | Application | Typical VIs |
|----------|-------------|-------------|
| Test & Measurement | Automated test | DAQmx, VISA |
| Process Control | PLC replacement | PID, State Machine |
| Monitoring | Structural health | Signal Processing |
| Research | Lab automation | File I/O, Network |
| Manufacturing | QC testing | Queue, Events |

## 9.3 Automation

### Python Integration

```python
# Use LabVIEW gRPC interface
import grpc
import labview_pb2
import labview_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = labview_pb2_grpc.LabVIEWStub(channel)

# Run VI
request = labview_pb2.RunVIRequest(vi_path='test.vi')
response = stub.RunVI(request)
```

### Command Line

```bash
# Run VI from command line
"C:\Program Files\National Instruments\LabVIEW 2023\LabVIEW.exe" 
  -p "C:\projects\test.vi"

# Run executable
"C:\projects\build\test.exe" argument
```

### Batch Processing

```batch
@echo off
for %%f in (data*.csv) do (
    labview -p process.vi %%f
)
```