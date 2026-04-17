## 7. Standards & Reference

### 7.1 Frontend Architecture Frameworks

| Framework / 框架 | When to Use / 使用场景 | Key Steps
|-----------------|----------------------|-------------------|
| **CSR (Create React App
| **SSR (Next.js App Router)** | SEO-critical pages; authenticated content with personalization | 1. Server renders HTML → 2. Stream to client → 3. Hydrate React → 4. Client takes over |
| **SSG (Next.js
| **ISR (Next.js)** | E-commerce catalogs; content updated hourly, not per-request | 1. SSG + revalidate window → 2. Serve cached → 3. Rebuild in background |

### 7.2 Core Web Vitals Metrics

| Metric / 指标 | Formula / 公式 | Good / 良好 | Poor
|--------------|--------------|------------|---------|
| **LCP (Largest Contentful Paint)** | Time until largest visible element renders | ≤ 2.5s | > 4.0s |
| **INP (Interaction to Next Paint)** | Time from user interaction to visual response | ≤ 200ms | > 500ms |
| **CLS (Cumulative Layout Shift)** | Sum of all unexpected layout shift scores | ≤ 0.1 | > 0.25 |
| **Initial JS Bundle** | Gzip-compressed JavaScript on critical path | < 200KB | > 500KB |
| **Time to Interactive** | Time until page responds reliably to input | < 3.8s on 4G | > 7s |

### 7.3 State Management Decision Guide

| State Type / 状态类型 | Tool / 工具 | When
|----------------------|------------|---------------|
| Server
| Local UI state | useState / useReducer | Form values, open/close, current tab, local toggles |
| Shareable URL state | URLSearchParams
| Scoped shared state | React Context | Theme, locale, auth context (low-frequency updates only) |
| Global client state | Zustand | Cart, notifications, cross-feature state (high-frequency ok) |

---

