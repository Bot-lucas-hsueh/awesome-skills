## § 6 · Domain Knowledge

### 6.1 Core Web Vitals Targets

| Metric | Target | Measurement |
|--------|--------|-------------|
| **LCP** (Largest Contentful Paint) | < 2.5s | Real user monitoring |
| **FID** (First Input Delay) | < 100ms | Real user monitoring |
| **CLS** (Cumulative Layout Shift) | < 0.1 | Real user monitoring |
| **TTFB** (Time to First Byte) | < 600ms | Server response |
| **FCP** (First Contentful Paint) | < 1.8s | Real user monitoring |

### 6.2 React Rendering Optimization

| Technique | When to Use | Impact |
|-----------|-------------|--------|
| **React.memo** | Pure components, expensive render | Prevents re-renders |
| **useMemo** | Expensive calculations | Caches computation |
| **useCallback** | Function props to children | Stable references |
| **Code splitting** | Large routes/components | Smaller initial bundle |
| **Virtualization** | Long lists (1000+ items) | Render only visible |

### 6.3 Accessibility Checklist

- [ ] Keyboard navigation works fully
- [ ] Focus indicators visible
- [ ] ARIA labels on interactive elements
- [ ] Alt text on images
- [ ] Color contrast 4.5:1 minimum
- [ ] Screen reader tested (VoiceOver/NVDA)
- [ ] Focus trap in modals
- [ ] Skip navigation link

---
