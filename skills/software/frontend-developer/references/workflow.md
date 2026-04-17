## 8. Standard Workflow

### 8.1 New Feature Development

```
Phase 1: Design & Architecture (Day 1)
├── Identify rendering strategy (CSR vs. SSR vs. SSG for this feature)
├── Design component tree: container → presentational hierarchy
├── Define TypeScript interfaces for props, API responses, store state
├── Confirm accessibility requirements (keyboard, ARIA, contrast, screen reader)
└── [✓ Done]: Component diagram + TypeScript types reviewed; accessibility plan documented
    [✗ FAIL]: No TypeScript types defined → STOP, define interfaces before implementation

Phase 2: Implementation (Day 2-3)
├── Implement smallest unit first (pure functions → hooks → components)
├── Add Vitest unit tests for business logic before moving to next component
├── Run axe DevTools on every interactive component before integration
├── Profile with React DevTools Profiler: no unexpected re-renders
└── [✓ Done]: Component renders correctly; unit tests pass; axe reports 0 violations
    [✗ FAIL]: axe violations present → fix before declaring feature "done"

Phase 3: Performance & Polish (Day 4-5)
├── Run Lighthouse audit: validate LCP ≤ 2.5s, CLS ≤ 0.1, INP ≤ 200ms
├── Run webpack-bundle-analyzer
├── Add route-level code splitting for all new pages (React.lazy + Suspense)
├── Test keyboard navigation end-to-end (Tab, Arrow keys, Enter, Escape)
└── [✓ Done]: Lighthouse score ≥ 90; bundle delta < 50KB; keyboard nav works
    [✗ FAIL]: LCP > 4s → profile critical path, add preload, optimize images
```

### 8.2 Performance Optimization

```
Step 1: Measure First
  → Run Lighthouse (mobile, throttled) to get Core Web Vitals baseline
  → Chrome DevTools → Performance tab: identify Long Tasks (>50ms)
  → React DevTools Profiler: find components re-rendering unnecessarily
  → Bundle analyzer: identify unexpected large dependencies

Step 2: Identify Root Cause
  → LCP too slow → Hero image not preloaded / TTFB too high
  → CLS > 0.1 → Images without dimensions
  → INP > 200ms → Long main thread tasks
  → Bundle too large → Unshaken imports / duplicate packages

Step 3: Apply Targeted Fix
  → LCP: add <link rel="preload"> for hero image; use next/image with priority
  → CLS: add explicit width/height to all images; skeleton screens
  → INP: React.startTransition for non-urgent updates; defer non-critical JS
  → Bundle: dynamic import(); check package alternatives; tree-shake

[✓ Done]: All Core Web Vitals "Good" in Lighthouse; real-user RUM confirms improvement
```

---

