# Hydrogen Framework Reference

## Overview

Hydrogen is Shopify's React-based framework for building custom storefronts. It provides:
- Pre-built commerce components
- Optimized data fetching with caching
- Server-side rendering (SSR)
- Shopify Storefront API integration

## Project Structure

```
my-hydrogen-store/
├── app/
│   ├── components/       # React components
│   ├── lib/             # Utilities, helpers
│   ├── routes/          # Remix route files
│   ├── styles/          # Global styles
│   └── entry.server.tsx # Server entry
├── public/              # Static assets
├── storefrontapi.generated.d.ts
├── remix.config.js
└── package.json
```

## Setup

### Create New Project
```bash
npm create @shopify/hydrogen@latest
# or
npx create-remix@latest --template shopify/hydrogen
```

### Environment Configuration
```bash
# .env
SESSION_SECRET="your-secret-key"
PUBLIC_STOREFRONT_API_TOKEN="your-storefront-token"
PUBLIC_STOREFRONT_API_VERSION="2025-01"
PUBLIC_STORE_DOMAIN="your-store.myshopify.com"
```

## Data Fetching

### Loader Function
```typescript
// app/routes/products.$handle.tsx
import {json, type LoaderFunctionArgs} from '@shopify/remix-oxygen';
import {useLoaderData} from '@remix-run/react';

export async function loader({params, context}: LoaderFunctionArgs) {
  const {handle} = params;
  
  const {product} = await context.storefront.query(PRODUCT_QUERY, {
    variables: {handle},
    // Caching strategies
    cache: context.storefront.CacheShort(),
  });

  if (!product) {
    throw new Response('Product not found', {status: 404});
  }

  return json({product});
}

export default function Product() {
  const {product} = useLoaderData<typeof loader>();
  return <ProductDetails product={product} />;
}
```

### Cache Strategies
```typescript
// Available cache strategies
CacheNone()        // No caching, always fetch fresh
CacheShort()       // 1 second stale-while-revalidate
CacheLong()        // 1 hour stale-while-revalidate
CacheCustom({
  maxAge: 3600,           // 1 hour fresh
  staleWhileRevalidate: 86400,  // 24 hours stale
})
```

### GraphQL Query
```typescript
const PRODUCT_QUERY = `#graphql
  query Product($handle: String!, $selectedOptions: [SelectedOptionInput!]!) {
    product(handle: $handle) {
      id
      title
      handle
      descriptionHtml
      media(first: 7) {
        nodes {
          ... on MediaImage {
            mediaContentType
            image {
              id
              url
              altText
              width
              height
            }
          }
          ... on Video {
            mediaContentType
            sources {
              mimeType
              url
            }
          }
        }
      }
      variants(first: 100) {
        nodes {
          id
          availableForSale
          selectedOptions {
            name
            value
          }
          image {
            id
            url
            altText
            width
            height
          }
          price {
            amount
            currencyCode
          }
          compareAtPrice {
            amount
            currencyCode
          }
          sku
          title
          unitPrice {
            amount
            currencyCode
          }
        }
      }
      selectedVariant: variantBySelectedOptions(
        selectedOptions: $selectedOptions
      ) {
        id
        availableForSale
        selectedOptions {
          name
          value
        }
        image {
          id
          url
          altText
          width
          height
        }
        price {
          amount
          currencyCode
        }
        compareAtPrice {
          amount
          currencyCode
        }
        sku
        title
        unitPrice {
          amount
          currencyCode
        }
      }
      seo {
        description
        title
      }
    }
  }
`;
```

## Cart Management

### Cart Provider Setup
```tsx
// app/root.tsx
import {CartProvider} from '@shopify/hydrogen-react';

export default function App() {
  return (
    <CartProvider
      onLineAdd={() => {/* Analytics */}}
      onLineRemove={() => {/* Analytics */}}
    >
      <Outlet />
    </CartProvider>
  );
}
```

### Using Cart Hook
```tsx
import {useCart} from '@shopify/hydrogen-react';

function AddToCartButton({variantId}) {
  const {status, linesAdd} = useCart();

  const handleAdd = () => {
    linesAdd([{
      merchandiseId: variantId,
      quantity: 1,
    }]);
  };

  return (
    <button 
      onClick={handleAdd}
      disabled={status === 'updating'}
    >
      {status === 'updating' ? 'Adding...' : 'Add to Cart'}
    </button>
  );
}
```

### Server Cart Action
```typescript
// app/routes/cart.tsx
import {ActionFunctionArgs} from '@shopify/remix-oxygen';

export async function action({request, context}: ActionFunctionArgs) {
  const {cart} = context;
  const formData = await request.formData();
  const action = formData.get('action');

  switch (action) {
    case 'add': {
      const variantId = formData.get('variantId') as string;
      const quantity = parseInt(formData.get('quantity') as string, 10);
      
      const {cart: updatedCart} = await cart.addLines([
        {merchandiseId: variantId, quantity},
      ]);
      
      return json({cart: updatedCart});
    }
    
    case 'remove': {
      const lineIds = formData.getAll('lineId') as string[];
      
      const {cart: updatedCart} = await cart.removeLines(lineIds);
      
      return json({cart: updatedCart});
    }
    
    case 'update': {
      const lineId = formData.get('lineId') as string;
      const quantity = parseInt(formData.get('quantity') as string, 10);
      
      const {cart: updatedCart} = await cart.updateLines([
        {id: lineId, quantity},
      ]);
      
      return json({cart: updatedCart});
    }
    
    default:
      return json({error: 'Invalid action'}, {status: 400});
  }
}
```

## SEO

### Route Meta
```tsx
// app/routes/products.$handle.tsx
export const meta: MetaFunction<typeof loader> = ({data}) => {
  return [
    {title: data?.product?.seo?.title || data?.product?.title},
    {
      name: 'description',
      content: data?.product?.seo?.description || data?.product?.description,
    },
    {
      property: 'og:title',
      content: data?.product?.title,
    },
    {
      property: 'og:description',
      content: data?.product?.description,
    },
    {
      property: 'og:image',
      content: data?.product?.featuredImage?.url,
    },
    {
      property: 'og:type',
      content: 'product',
    },
    {
      name: 'twitter:card',
      content: 'summary_large_image',
    },
  ];
};
```

### Structured Data
```tsx
function ProductJsonLd({product}) {
  const jsonLd = {
    '@context': 'https://schema.org',
    '@type': 'Product',
    name: product.title,
    description: product.description,
    image: product.featuredImage?.url,
    brand: {
      '@type': 'Brand',
      name: product.vendor,
    },
    offers: product.variants.nodes.map(variant => ({
      '@type': 'Offer',
      price: variant.price.amount,
      priceCurrency: variant.price.currencyCode,
      availability: variant.availableForSale
        ? 'https://schema.org/InStock'
        : 'https://schema.org/OutOfStock',
      sku: variant.sku,
    })),
  };

  return (
    <script
      type="application/ld+json"
      dangerouslySetInnerHTML={{__html: JSON.stringify(jsonLd)}}
    />
  );
}
```

## Analytics

### Setup
```tsx
// app/root.tsx
import {ShopifyAnalytics} from '@shopify/hydrogen';
import {useEffect} from 'react';

export default function App() {
  useAnalytics();

  return (
    <html>
      <head>
        <ShopifyAnalytics />
      </head>
      <body>
        <Outlet />
      </body>
    </html>
  );
}

function useAnalytics() {
  const location = useLocation();
  const analytics = useMemo(() => ({pageViewed: () => {
    // Send to your analytics service
    gtag('event', 'page_view', {
      page_location: location.pathname,
    });
  }}), [location]);

  useEffect(() => {
    analytics.pageViewed();
  }, [location, analytics]);
}
```

## Deployment

### Oxygen (Shopify Hosting)
```bash
# Deploy to Oxygen
shopify hydrogen deploy
```

### Custom Hosting
```bash
# Build for production
npm run build

# Start production server
npm start
```

### Environment Variables for Production
```bash
# Required
SESSION_SECRET=
PUBLIC_STOREFRONT_API_TOKEN=
PUBLIC_STORE_DOMAIN=

# Optional
PUBLIC_STOREFRONT_ID=
PUBLIC_CUSTOMER_ACCOUNT_API_CLIENT_ID=
PUBLIC_CUSTOMER_ACCOUNT_API_URL=
```

## Best Practices

1. **Performance**
   - Use appropriate cache strategies
   - Lazy load below-fold components
   - Optimize images with proper sizing
   - Minimize JavaScript bundle size

2. **SEO**
   - Implement proper meta tags
   - Add structured data (JSON-LD)
   - Use semantic HTML
   - Create sitemap.xml

3. **Accessibility**
   - Use ARIA labels
   - Ensure keyboard navigation
   - Test with screen readers
   - Follow WCAG guidelines

4. **State Management**
   - Use Remix's built-in data handling
   - Leverage URL state for filters
   - Implement optimistic UI updates
   - Handle loading and error states
