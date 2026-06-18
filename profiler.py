import time

class GPUProfiler:
    def __init__(self): self.r = {}
    def start(self, n): self.r[n] = {"t": time.perf_counter()}
    def stop(self, n): self.r[n]["ms"] = (time.perf_counter()-self.r[n]["t"])*1000
    def report(self):
        for n,m in sorted(self.r.items(), key=lambda x: x[1].get("ms",0), reverse=True):
            print(f"  {n}: {m.get('ms',0):.2f} ms")
