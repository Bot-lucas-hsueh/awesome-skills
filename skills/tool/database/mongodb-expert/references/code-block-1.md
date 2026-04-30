# javascript Example

```
// Faceted search pattern
db.products.aggregate([
  { $match: { category: "electronics" } },
  { $facet: {
      categories: [
        { $group: { _id: "$subcategory", count: { $sum: 1 } } },
        { $sort: { count: -1 } }
      ],
      priceRanges: [
        { $bucket: {
            groupBy: "$price",
            boundaries: [0, 50, 100, 200, Infinity],
            default: "Other",
            output: { count: { $sum: 1 } }
          }
        }
      ],
      stats: [
        { $group: {
            _id: null,
            avgPrice: { $avg: "$price" },
            minPrice: { $min: "$price" },
            maxPrice: { $max: "$price" }
          }
        }
      ],
      topBrands: [
        { $group: { _id: "$brand", count: { $sum: 1 } } },
        { $sort: { count: -1 } },
        { $limit: 5 }
      ]
    }
  }
])
```
