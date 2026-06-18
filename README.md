# Gpu Profiling Tools

GPU profiling and performance analysis tools for ROCm/HIP.

## Tools
- **Kernel Profiler**: Per-kernel timing, occupancy, memory throughput
- **Memory Analyzer**: Allocation patterns, peak usage, fragmentation
- **Timeline Visualizer**: Chrome trace export for async ops
- **Bottleneck Detector**: Compute vs memory bound classification

## Usage
```bash
python profile.py --app ./train.py --output trace.json
```

## License
MIT
