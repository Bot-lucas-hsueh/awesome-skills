# Liquid Templating Reference

## Overview

Liquid is an open-source templating language created by Shopify. It serves as the bridge between Shopify store data and the HTML rendered on storefronts.

## Core Syntax

### Output Tags
Display dynamic content using double curly braces:

```liquid
{{ product.title }}
{{ cart.total_price | money }}
{{ shop.name | upcase }}
```

### Logic Tags
Control flow and logic using curly braces with percent signs:

```liquid
{% if product.available %}
  <button>Add to Cart</button>
{% else %}
  <span>Sold Out</span>
{% endif %}

{% for variant in product.variants %}
  <option value="{{ variant.id }}">{{ variant.title }}</option>
{% endfor %}

{% assign discount = 0.2 %}
{% capture message %}Save {{ discount | times: 100 }}%!{% endcapture %}
```

### Filters
Modify output values using the pipe character:

```liquid
{{ product.price | money }}
{{ product.title | upcase | truncate: 20 }}
{{ 'now' | date: '%B %d, %Y' }}
{{ collection.products | where: 'available', true | sort: 'price' }}
```

## Global Objects

### Product
```liquid
{{ product.title }}
{{ product.description }}
{{ product.price | money }}
{{ product.compare_at_price | money }}
{{ product.featured_image | image_url: width: 600 }}
{{ product.variants.size }}
{{ product.tags }}
{{ product.metafields.custom.field_name }}
```

### Collection
```liquid
{{ collection.title }}
{{ collection.products_count }}
{{ collection.all_products | size }}
{{ collection.image | image_url: width: 800 }}
{{ collection.description }}
{{ collection.url }}
```

### Cart
```liquid
{{ cart.item_count }}
{{ cart.total_price | money }}
{{ cart.currency.iso_code }}
{% for item in cart.items %}
  {{ item.quantity }} x {{ item.product.title }}
{% endfor %}
```

### Shop
```liquid
{{ shop.name }}
{{ shop.email }}
{{ shop.domain }}
{{ shop.currency }}
{{ shop.description }}
{{ shop.secure_url }}
{{ shop.money_format }}
```

### Customer
```liquid
{% if customer %}
  {{ customer.first_name }}
  {{ customer.email }}
  {{ customer.orders.size }}
  {{ customer.total_spent | money }}
{% endif %}
```

## JSON Templates (Online Store 2.0)

Modern Shopify themes use JSON templates that define sections:

```json
{
  "sections": {
    "hero": {
      "type": "hero-banner",
      "settings": {
        "heading": "Welcome",
        "image": "shopify://shop_images/hero.jpg"
      }
    },
    "featured": {
      "type": "featured-collection",
      "settings": {
        "collection": "frontpage"
      }
    }
  },
  "order": ["hero", "featured"]
}
```

## Section Schema

Define configurable sections with the schema tag:

```liquid
{% schema %}
{
  "name": "Product Highlights",
  "tag": "section",
  "class": "product-highlights",
  "settings": [
    {
      "type": "text",
      "id": "heading",
      "label": "Heading",
      "default": "Why Choose Us"
    },
    {
      "type": "image_picker",
      "id": "background_image",
      "label": "Background Image"
    },
    {
      "type": "range",
      "id": "padding_top",
      "min": 0,
      "max": 100,
      "step": 4,
      "unit": "px",
      "label": "Padding Top",
      "default": 36
    },
    {
      "type": "select",
      "id": "text_alignment",
      "label": "Text Alignment",
      "options": [
        {"value": "left", "label": "Left"},
        {"value": "center", "label": "Center"},
        {"value": "right", "label": "Right"}
      ],
      "default": "center"
    },
    {
      "type": "collection",
      "id": "featured_collection",
      "label": "Featured Collection"
    }
  ],
  "blocks": [
    {
      "type": "highlight",
      "name": "Highlight",
      "settings": [
        {
          "type": "text",
          "id": "title",
          "label": "Title"
        },
        {
          "type": "textarea",
          "id": "description",
          "label": "Description"
        }
      ]
    }
  ],
  "presets": [
    {
      "name": "Product Highlights",
      "blocks": {
        "highlight-1": {
          "type": "highlight"
        }
      }
    }
  ]
}
{% endschema %}
```

## Best Practices

### Performance
- Use `image_url` filter with specific widths
- Minimize nested loops
- Cache expensive operations
- Lazy load below-fold images

```liquid
{% comment %} Good {% endcomment %}
<img 
  src="{{ image | image_url: width: 400 }}"
  srcset="{{ image | image_url: width: 400 }} 400w,
          {{ image | image_url: width: 800 }} 800w"
  loading="lazy"
>

{% comment %} Avoid {% endcomment %}
<img src="{{ image | img_url: 'master' }}">
```

### Security
- Always escape user input
- Use `| escape` filter for HTML content
- Validate external links

### Maintainability
- Use snippets for reusable code
- Comment complex logic
- Follow naming conventions
- Group related sections
