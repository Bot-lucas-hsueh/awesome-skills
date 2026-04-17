# Standards & Reference

## 7.1 Official Documentation

- [Vercel Documentation](https://vercel.com/docs) — Full documentation for all Vercel features
- [Vercel CLI Reference](https://vercel.com/docs/cli) — All Vercel CLI commands
- [Next.js Documentation](https://nextjs.org/docs) — Full Next.js documentation
- [Vercel Deployment](https://vercel.com/docs/deployments/overview) — Deployment configuration
- [Vercel Edge Functions](https://vercel.com/docs/functions/edge-functions) — Edge runtime
- [Vercel Serverless Functions](https://vercel.com/docs/functions) — Serverless function config
- [Vercel Environment Variables](https://vercel.com/docs/environment-variables) — Managing secrets
- [Vercel Analytics](https://vercel.com/docs/concepts/analytics) — Performance analytics

## 7.2 Framework Support

### 7.2.1 Supported Frameworks

| Framework | Supported Versions | Notes |
|-----------|------------------|-------|
| **Next.js** | 13, 14, 15 | First-class support, SSR/SSG/ISR |
| **React** | 18, 19 | Client-side rendering |
| **Vite** | 5.x | SPA and static sites |
| **Astro** | 4.x | Static and Islands architecture |
| **Svelte** | 4.x, 5.x | SvelteKit supported |
| **Nuxt** | 3.x | Vue.js framework |
| **Remix** | 2.x | Full-stack React framework |
| **SvelteKit** | Latest | Svelte's meta-framework |
| **Gatsby** | 5.x | Static site generator |
| **Eleventy** | Latest | Static site generator |

### 7.2.2 Node.js Versions

| Version | Status | Notes |
|---------|--------|-------|
| 18.x | Supported | Recommended |
| 20.x | Supported | Latest LTS |
| 22.x | Supported | Current |
| 16.x | Deprecated | Migrate recommended |

## 7.3 Project Configuration

### 7.3.1 vercel.json Schema

```json
{
  "version": 2,
  "buildCommand": "npm run build",
  "outputDirectory": "dist",
  "installCommand": "npm install --legacy-peer-deps",
  "framework": "nextjs",
  "regions": ["iad1", "sfo1"],
  "routes": [
    {
      "src": "/api/users",
      "dest": "/api/users.ts"
    },
    {
      "src": "/old-page",
      "status": 301,
      "headers": {
        "Location": "/new-page"
      }
    }
  ],
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-Frame-Options",
          "value": "DENY"
        }
      ]
    }
  ],
  "env": {
    "NEXT_PUBLIC_API_URL": "@api-url"
  },
  "regions": ["iad1"],
  "functions": {
    "src/api/*.ts": {
      "memory": 1024,
      "maxDuration": 10
    }
  }
}
```

### 7.3.2 Route Configuration

| Pattern | Behavior |
|---------|----------|
| `/api/*` | Serverless function |
| `/static/*` | Static file |
| `/[slug]` | Dynamic route (SSG) |
| `/[slug]/**` | Nested dynamic route |
| `(marketing)/*` | Route group (no URL impact) |

### 7.3.3 Headers for Security

```json
{
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        {
          "key": "X-DNS-Prefetch-Control",
          "value": "on"
        },
        {
          "key": "Strict-Transport-Security",
          "value": "max-age=63072000; includeSubDomains; preload"
        },
        {
          "key": "X-Content-Type-Options",
          "value": "nosniff"
        },
        {
          "key": "X-Frame-Options",
          "value": "SAMEORIGIN"
        },
        {
          "key": "X-XSS-Protection",
          "value": "1; mode=block"
        },
        {
          "key": "Referrer-Policy",
          "value": "strict-origin-when-cross-origin"
        }
      ]
    }
  ]
}
```

## 7.4 Environment Variables

### 7.4.1 Variable Scopes

| Scope | Access | Use Case |
|-------|--------|----------|
| **Production** | Production builds only | Secrets, API keys |
| **Preview** | Preview deployments | Test APIs |
| **Development** | Local development | Local config |
| **Secret** | Encrypted at rest | Sensitive data |

### 7.4.2 Variable Naming Convention

| Pattern | Example | Usage |
|---------|---------|-------|
| `PUBLIC_*` | `PUBLIC_API_URL` | Client-accessible |
| `NEXT_PUBLIC_*` | `NEXT_PUBLIC_STRIPE_KEY` | Client-accessible in Next.js |
| Standard | `DATABASE_URL` | Server-side only |

### 7.4.3 CLI Environment Commands

```bash
# Set environment variable
vercel env add API_SECRET production

# Pull environment variables
vercel env pull .env.local

# List environment variables
vercel env ls

# Remove environment variable
vercel env rm API_SECRET production
```

## 7.5 Deployment Configuration

### 7.5.1 Build Commands

| Framework | Default Build Command |
|-----------|----------------------|
| Next.js | `next build` |
| Vite | `vite build` |
| Astro | `astro build` |
| Nuxt | `nuxt build` |
| SvelteKit | `vite build` |
| Remix | `remix vite:build` |

### 7.5.2 Output Directories

| Framework | Default Output |
|-----------|---------------|
| Next.js | `.next` |
| Vite | `dist` |
| Astro | `dist` |
| Nuxt | `.output` |
| SvelteKit | `.svelte-kit/output` |

### 7.5.3 Region Selection

| Region Code | Location | Latency (ms) |
|-------------|----------|--------------|
| iad1 | Virginia, USA | ~50 |
| sfo1 | California, USA | ~80 |
| gru1 | Sao Paulo, Brazil | ~150 |
| lhr1 | London, UK | ~100 |
| fra1 | Frankfurt, Germany | ~110 |
| hnd1 | Tokyo, Japan | ~180 |
| sin1 | Singapore | ~200 |
| syd1 | Sydney, Australia | ~200 |

## 7.6 Performance Optimization

### 7.6.1 Image Optimization

```javascript
// next.config.js
module.exports = {
  images: {
    formats: ['image/avif', 'image/webp'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
    minimumCacheTTL: 60 * 60 * 24 * 30, // 30 days
  }
}
```

### 7.6.2 Bundle Optimization

```javascript
// next.config.js
module.exports = {
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  experimental: {
    optimizeCss: true,
  },
}
```
