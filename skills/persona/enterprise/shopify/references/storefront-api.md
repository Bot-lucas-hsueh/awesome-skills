# Storefront API Reference

## Overview

The Storefront API provides unauthenticated access to Shopify store data, enabling custom storefronts, mobile apps, and headless commerce experiences.

## Authentication

### Public Access Token
```javascript
const client = createStorefrontApiClient({
  storeDomain: 'your-store.myshopify.com',
  apiVersion: '2025-01',
  publicAccessToken: 'your-public-access-token',
});
```

### Private Access (Server-side)
```javascript
const client = createStorefrontApiClient({
  storeDomain: 'your-store.myshopify.com',
  apiVersion: '2025-01',
  privateAccessToken: process.env.SHOPIFY_STOREFRONT_ACCESS_TOKEN,
});
```

## Core Queries

### Product Query
```graphql
query getProduct($handle: String!) {
  product(handle: $handle) {
    id
    title
    descriptionHtml
    handle
    tags
    productType
    vendor
    featuredImage {
      url(transform: {maxWidth: 800})
      altText
      width
      height
    }
    images(first: 10) {
      nodes {
        url(transform: {maxWidth: 1200})
        altText
      }
    }
    variants(first: 50) {
      nodes {
        id
        title
        sku
        availableForSale
        price {
          amount
          currencyCode
        }
        compareAtPrice {
          amount
          currencyCode
        }
        selectedOptions {
          name
          value
        }
        image {
          url
          altText
        }
      }
    }
    options {
      name
      values
    }
    metafield(namespace: "custom", key: "specifications") {
      value
      type
    }
  }
}
```

### Collection Query
```graphql
query getCollection($handle: String!, $first: Int!, $after: String) {
  collection(handle: $handle) {
    id
    title
    descriptionHtml
    handle
    image {
      url(transform: {maxWidth: 1600})
      altText
    }
    products(first: $first, after: $after) {
      pageInfo {
        hasNextPage
        endCursor
      }
      nodes {
        id
        title
        handle
        featuredImage {
          url(transform: {maxWidth: 600})
          altText
        }
        priceRange {
          minVariantPrice {
            amount
            currencyCode
          }
        }
        variants(first: 1) {
          nodes {
            availableForSale
          }
        }
      }
    }
  }
}
```

### Cart Operations

#### Create Cart
```graphql
mutation cartCreate($input: CartInput!) {
  cartCreate(input: $input) {
    cart {
      id
      checkoutUrl
      lines(first: 100) {
        nodes {
          id
          quantity
          merchandise {
            ... on ProductVariant {
              id
              title
              product {
                title
                handle
              }
            }
          }
        }
      }
      cost {
        totalAmount {
          amount
          currencyCode
        }
        subtotalAmount {
          amount
          currencyCode
        }
        taxAmount {
          amount
          currencyCode
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

#### Add Line Items
```graphql
mutation cartLinesAdd($cartId: ID!, $lines: [CartLineInput!]!) {
  cartLinesAdd(cartId: $cartId, lines: $lines) {
    cart {
      id
      lines(first: 100) {
        nodes {
          id
          quantity
        }
      }
    }
    userErrors {
      field
      message
    }
  }
}
```

### Customer Operations

#### Customer Access Token Create
```graphql
mutation customerAccessTokenCreate($input: CustomerAccessTokenCreateInput!) {
  customerAccessTokenCreate(input: $input) {
    customerAccessToken {
      accessToken
      expiresAt
    }
    customerUserErrors {
      code
      field
      message
    }
  }
}
```

#### Get Customer
```graphql
query getCustomer($customerAccessToken: String!) {
  customer(customerAccessToken: $customerAccessToken) {
    id
    firstName
    lastName
    email
    phone
    defaultAddress {
      id
      address1
      city
      country
      zip
    }
    orders(first: 10) {
      nodes {
        id
        orderNumber
        totalPrice {
          amount
          currencyCode
        }
        fulfillmentStatus
        financialStatus
        processedAt
      }
    }
  }
}
```

## Localization

### Buyer Identity for Market-Specific Pricing
```graphql
query getProductLocalized($handle: String!, $country: CountryCode!) {
  product(handle: $handle) {
    title
    variants(first: 1) {
      nodes {
        price {
          amount
          currencyCode
        }
        # Localized price
        priceV2: price(buyerIdentity: {countryCode: $country}) {
          amount
          currencyCode
        }
      }
    }
  }
}
```

### Language Localization
```graphql
query getShopInfo($language: LanguageCode!) {
  shop {
    name
    description
    primaryDomain {
      url
    }
  }
  localization {
    language {
      isoCode
      endonymName
    }
    availableLanguages {
      isoCode
      endonymName
    }
    country {
      isoCode
      name
    }
    availableCountries {
      isoCode
      name
      currency {
        isoCode
      }
    }
  }
}
```

## Pagination

### Cursor-Based Pagination
```graphql
query getProductsPaginated($first: Int!, $after: String) {
  products(first: $first, after: $after) {
    pageInfo {
      hasNextPage
      hasPreviousPage
      startCursor
      endCursor
    }
    edges {
      cursor
      node {
        id
        title
        handle
      }
    }
  }
}
```

## Rate Limits

| Plan | Points per minute |
|------|-------------------|
| All plans | 500 |
| With Shopify Plus (increased limit) | 2,000 |

Calculate query cost:
```
Cost = Base (10) + Object count fields (nodes, edges) × Complexity
```

## Best Practices

1. **Use Fragments** for reusable field sets
2. **Request only needed fields** to reduce payload size
3. **Implement caching** with appropriate cache policies
4. **Handle errors gracefully** with userErrors
5. **Use @inContext directive** for localization
