## § 6 · Professional Toolkit

| Tool | Purpose |
|------|---------|
| **MNE-Python** | EEG/MEG/ECoG signal processing: filtering, epoching, ICA artifact rejection, time-frequency analysis, source localization |
| **Kilosort3** | GPU-accelerated automated spike sorting for high-density probes (Neuropixels, Utah array); drift-corrected template matching |
| **MountainSort4** | CPU-based spike sorting with isosplit clustering; preferred for smaller channel counts (<64ch) |
| **Open Ephys** | Open-source neural acquisition system; supports Intan RHD, IMEC Neuropixels, real-time plugin API for closed-loop |
| **BrainFlow** | Unified API for non-invasive BCI hardware (OpenBCI Cyton/Ganglion, Muse, Neurosity); Pythonic streaming interface |
| **FieldTrip** | MATLAB-based neural data analysis toolkit; strong for M/EEG source analysis and connectivity |
| **LFADS (Latent Factor Analysis via Dynamical Systems)** | Gaussian process + RNN latent variable model for denoising population spiking; JAX/TF implementations |
| **Elephant** | Electrophysiology analysis: spike train statistics, Granger causality, SPADE motif detection |
| **SpikeInterface** | Unified Python framework for spike sorting with Kilosort, MountainSort, Phy; standardized comparison across sorters |
| **Neo** | Python package for reading/writing electrophysiology file formats (Blackrock NSx/NEV, Plexon, Intan RHD) |

---
