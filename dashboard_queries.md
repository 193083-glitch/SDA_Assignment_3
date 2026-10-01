# MongoDB Atlas Charts Dashboard Queries

The dashboard uses MongoDB Atlas Charts with the `supply_chain_db.events`
collection.

## 1. Customer Demand vs Available Inventory

```json
[
  {
    "$group": {
      "_id": "$product_id",
      "customer_demand": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "OMS"] },
            "$quantity",
            0
          ]
        }
      },
      "available_inventory": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$available_quantity",
            0
          ]
        }
      }
    }
  },
  {
    "$sort": {
      "customer_demand": -1
    }
  }
]
[
  {
    "$group": {
      "_id": "$product_id",
      "customer_demand": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "OMS"] },
            "$quantity",
            0
          ]
        }
      },
      "available_inventory": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$available_quantity",
            0
          ]
        }
      },
      "reserved_inventory": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$reserved_quantity",
            0
          ]
        }
      },
      "reorder_level": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$reorder_level",
            0
          ]
        }
      }
    }
  },
  {
    "$addFields": {
      "inventory_risk": {
        "$subtract": [
          {
            "$add": [
              "$customer_demand",
              "$reserved_inventory",
              "$reorder_level"
            ]
          },
          "$available_inventory"
        ]
      }
    }
  },
  {
    "$sort": {
      "inventory_risk": -1
    }
  }
]

[
  {
    "$group": {
      "_id": "$product_id",
      "suppliers": {
        "$addToSet": {
          "$cond": [
            { "$eq": ["$source", "ERP"] },
            "$supplier_id",
            null
          ]
        }
      },
      "procurement_value": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "ERP"] },
            {
              "$multiply": [
                "$quantity",
                "$unit_price"
              ]
            },
            0
          ]
        }
      },
      "customer_demand": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "OMS"] },
            "$quantity",
            0
          ]
        }
      },
      "available_inventory": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$available_quantity",
            0
          ]
        }
      },
      "reserved_inventory": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$reserved_quantity",
            0
          ]
        }
      },
      "reorder_level": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$reorder_level",
            0
          ]
        }
      }
    }
  },
  {
    "$unwind": "$suppliers"
  },
  {
    "$match": {
      "suppliers": {
        "$ne": null
      }
    }
  },
  {
    "$addFields": {
      "inventory_pressure": {
        "$subtract": [
          {
            "$add": [
              "$customer_demand",
              "$reserved_inventory",
              "$reorder_level"
            ]
          },
          "$available_inventory"
        ]
      }
    }
  },
  {
    "$group": {
      "_id": "$suppliers",
      "procurement_value": {
        "$sum": "$procurement_value"
      },
      "inventory_pressure": {
        "$sum": "$inventory_pressure"
      }
    }
  },
  {
    "$sort": {
      "procurement_value": -1
    }
  }
]

[
  {
    "$match": {
      "source": "OMS"
    }
  },
  {
    "$group": {
      "_id": {
        "destination": "$destination",
        "product_id": "$product_id"
      },
      "order_quantity": {
        "$sum": "$quantity"
      }
    }
  }
]

[
  {
    "$group": {
      "_id": "$product_id",
      "procurement_quantity": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "ERP"] },
            "$quantity",
            0
          ]
        }
      },
      "customer_demand": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "OMS"] },
            "$quantity",
            0
          ]
        }
      },
      "available_inventory": {
        "$sum": {
          "$cond": [
            { "$eq": ["$source", "IMS"] },
            "$available_quantity",
            0
          ]
        }
      }
    }
  },
  {
    "$addFields": {
      "product_number": {
        "$toInt": {
          "$substrBytes": ["$_id", 4, -1]
        }
      }
    }
  },
  {
    "$sort": {
      "product_number": 1
    }
  }
]
