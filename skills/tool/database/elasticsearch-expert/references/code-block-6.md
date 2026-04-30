# Geo-location Search

Complete example for finding nearby restaurants with geo queries.

## Geo Search Query

```json
GET /restaurants/_search
{
  "query": {
    "bool": {
      "must": [
        { "match": { "name": "sushi" } }
      ],
      "filter": [
        {
          "geo_distance": {
            "distance": "5km",
            "location": { "lat": 40.7128, "lon": -74.0060 }
          }
        }
      ]
    }
  },
  "sort": [
    {
      "_geo_distance": {
        "location": { "lat": 40.7128, "lon": -74.0060 },
        "order": "asc",
        "unit": "km"
      }
    }
  ],
  "aggs": {
    "distance_ranges": {
      "geo_distance": {
        "field": "location",
        "origin": { "lat": 40.7128, "lon": -74.0060 },
        "ranges": [
          { "to": 1 },
          { "from": 1, "to": 5 },
          { "from": 5, "to": 10 },
          { "from": 10 }
        ]
      }
    }
  }
}
```

## Key Points

- geo_point field type required for location
- geo_distance filter finds items within radius
- _geo_distance sort orders by distance from origin
- geo_distance aggregation groups results by distance ranges
