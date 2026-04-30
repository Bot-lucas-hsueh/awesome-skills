# Performance Optimization Reference

## Overview

Shopify store performance directly impacts conversion rates. Studies show:
- 1 second delay = 7% reduction in conversions
- 3 second load time = 40% bounce rate
- Core Web Vitals affect SEO rankings

## Core Web Vitals Targets

| Metric | Target | Shopify Average |
|--------|--------|-----------------|
| LCP (Largest Contentful Paint) | < 2.5s | ~2.1s |
| INP (Interaction to Next Paint) | < 200ms | ~120ms |
| CLS (Cumulative Layout Shift) | < 0.1 | ~0.05 |
| TTFB (Time to First Byte) | < 600ms | ~300ms |
| FCP (First Contentful Paint) | < 1.8s | ~1.2s |

## Image Optimization

### Liquid Image Filters
```liquid
{% comment %} Basic image with width constraint {% endcomment %}
<img src="{{ image | image_url: width: 600 }}" 
     alt="{{ image.alt | escape }}"
     width="600"
     height="{{ 600 | divided_by: image.aspect_ratio | round }}">

{% comment %} Responsive images with srcset {% endcomment %}
<img src="{{ image | image_url: width: 400 }}"
     srcset="{{ image | image_url: width: 400 }} 400w,
             {{ image | image_url: width: 800 }} 800w,
             {{ image | image_url: width: 1200 }} 1200w"
     sizes="(max-width: 749px) 100vw, 50vw"
     alt="{{ image.alt | escape }}"
     loading="lazy"
     width="400"
     height="{{ 400 | divided_by: image.aspect_ratio | round }}">

{% comment %} Preload critical hero image {% endcomment %}
<link rel="preload" as="image" 
      href="{{ hero_image | image_url: width: 1600 }}"
      imagesrcset="{{ hero_image | image_url: width: 800 }} 800w,
                   {{ hero_image | image_url: width: 1600 }} 1600w"
      imagesizes="100vw">
```

### Image Format Optimization
- **WebP**: Use for all photographic images
- **AVIF**: Best compression, use for hero images
- **JPEG**: Fallback for older browsers
- **PNG**: Only for images requiring transparency
- **SVG**: Use for logos, icons, simple graphics

## Code Optimization

### CSS
```liquid
{% comment %} Critical CSS inline {% endcomment %}
<style>
  /* Critical above-fold styles */
  .hero { /* ... */ }
  .header { /* ... */ }
</style>

{% comment %} Async load non-critical CSS {% endcomment %}
<link rel="preload" href="{{ 'theme.css' | asset_url }}" as="style" onload="this.onload=null;this.rel='stylesheet'">
<noscript><link rel="stylesheet" href="{{ 'theme.css' | asset_url }}"></noscript>
```

### JavaScript
```liquid
{% comment %} Defer non-critical scripts {% endcomment %}
<script src="{{ 'theme.js' | asset_url }}" defer></script>

{% comment %} Async for independent scripts {% endcomment %}
<script src="{{ 'analytics.js' | asset_url }}" async></script>

{% comment %} Module for modern browsers {% endcomment %}
<script type="module" src="{{ 'app.mjs' | asset_url }}"></script>
```

### Liquid Optimization
```liquid
{% comment %} Avoid nested loops where possible {% endcomment %}
{% comment %} Bad: O(n²) complexity {% endcomment %}
{% for product in collection.products %}
  {% for tag in product.tags %}
    {% if tag == 'sale' %}
      {{ product.title }}
    {% endif %}
  {% endfor %}
{% endfor %}

{% comment %} Better: Pre-filter in query or use where filter {% endcomment %}
{% assign sale_products = collection.products | where: 'tags', 'sale' %}
{% for product in sale_products %}
  {{ product.title }}
{% endfor %}

{% comment %} Cache expensive operations {% endcomment %}
{% capture cache_key %}featured-products-{{ collection.id }}{% endcapture %}
{% assign cached = cache[cache_key] %}
{% if cached %}
  {{ cached }}
{% else %}
  {% capture products_html %}
    {% for product in collection.products limit: 8 %}
      {% render 'product-card', product: product %}
    {% endfor %}
  {% endcapture %}
  {% assign cache[cache_key] = products_html %}
  {{ products_html }}
{% endif %}
```

## Font Optimization

### Font Loading Strategy
```html
<!-- Preconnect to font CDN -->
<link rel="preconnect" href="https://fonts.shopifycdn.com" crossorigin>

<!-- Preload critical fonts -->
<link rel="preload" href="{{ 'font-bold.woff2' | asset_url }}" as="font" type="font/woff2" crossorigin>

<!-- Font face with font-display -->
<style>
@font-face {
  font-family: 'Brand Font';
  src: url('{{ 'font-regular.woff2' | asset_url }}') format('woff2');
  font-weight: 400;
  font-style: normal;
  font-display: swap; /* Prevents invisible text during load */
}

@font-face {
  font-family: 'Brand Font';
  src: url('{{ 'font-bold.woff2' | asset_url }}') format('woff2');
  font-weight: 700;
  font-style: normal;
  font-display: swap;
}
</style>
```

## Lazy Loading

### Native Lazy Loading
```liquid
{% comment %} Images below the fold {% endcomment %}
<img src="{{ image | image_url: width: 600 }}"
     loading="lazy"
     alt="{{ image.alt | escape }}"
     width="600"
     height="400">

{% comment %} Iframes (YouTube, maps) {% endcomment %}
<iframe src="{{ video_url }}"
        loading="lazy"
        title="Product video">
</iframe>
```

### Intersection Observer for Complex Content
```javascript
// Lazy load product recommendations
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      loadRecommendations(entry.target);
      observer.unobserve(entry.target);
    }
  });
}, {
  rootMargin: '100px', // Start loading 100px before visible
});

document.querySelectorAll('[data-lazy-recommendations]').forEach(el => {
  observer.observe(el);
});
```

## Third-Party Scripts

### Load Conditionally
```javascript
// Only load chat widget on product pages
if (window.location.pathname.includes('/products/')) {
  const script = document.createElement('script');
  script.src = 'https://chat-widget.com/script.js';
  script.async = true;
  script.defer = true;
  document.body.appendChild(script);
}

// Load after user interaction (idle time)
if ('requestIdleCallback' in window) {
  requestIdleCallback(() => {
    loadAnalytics();
  }, { timeout: 2000 });
} else {
  setTimeout(loadAnalytics, 2000);
}
```

### Partytown for Heavy Scripts
```html
<!-- Move third-party scripts to web worker -->
<script>
  partytown = {
    lib: '/~partytown/',
    forward: ['gtag', 'fbq', 'dataLayer.push'],
  };
</script>
<script src="/~partytown/partytown.js"></script>

<script type="text/partytown">
  // Analytics code runs in web worker
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## Server-Side Optimization

### Cache Headers
```javascript
// Hydrogen/Remix cache headers
export const headers = () => ({
  'Cache-Control': 'public, max-age=60, stale-while-revalidate=3600',
  'CDN-Cache-Control': 'public, max-age=3600',
  'Vary': 'Accept-Encoding',
});
```

### Preconnect and DNS-Prefetch
```html
<head>
  <!-- Preconnect to critical origins -->
  <link rel="preconnect" href="https://cdn.shopify.com">
  <link rel="preconnect" href="https://fonts.shopifycdn.com">
  
  <!-- DNS prefetch for third-party resources -->
  <link rel="dns-prefetch" href="https://analytics.google.com">
  <link rel="dns-prefetch" href="https://connect.facebook.net">
</head>
```

## Monitoring

### Performance Marks
```javascript
// Mark key moments in page lifecycle
performance.mark('hero-visible');
performance.mark('products-loaded');

// Measure between marks
performance.measure('time-to-products', 'navigationStart', 'products-loaded');

// Log to analytics
const measure = performance.getEntriesByName('time-to-products')[0];
analytics.track('Performance', {
  metric: 'time-to-products',
  duration: measure.duration,
});
```

### Shopify Web Vitals
```javascript
import {getCLS, getFID, getFCP, getLCP, getTTFB} from 'web-vitals';

function sendToAnalytics(metric) {
  const body = JSON.stringify(metric);
  // Send to your analytics endpoint
  (navigator.sendBeacon && navigator.sendBeacon('/analytics', body)) ||
    fetch('/analytics', {body, method: 'POST', keepalive: true});
}

getCLS(sendToAnalytics);
getFID(sendToAnalytics);
getFCP(sendToAnalytics);
getLCP(sendToAnalytics);
getTTFB(sendToAnalytics);
```

## Performance Checklist

### Pre-Launch
- [ ] Images optimized and properly sized
- [ ] Critical CSS inlined
- [ ] JavaScript deferred/async where possible
- [ ] Fonts preloaded with font-display: swap
- [ ] Lazy loading on below-fold images
- [ ] Third-party scripts minimized and deferred
- [ ] Compression enabled (Brotli/Gzip)

### Post-Launch Monitoring
- [ ] LCP under 2.5s
- [ ] INP under 200ms
- [ ] CLS under 0.1
- [ ] Mobile performance score > 90
- [ ] Desktop performance score > 95
- [ ] No render-blocking resources
- [ ] Proper cache headers configured
