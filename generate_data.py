import json
from datetime import datetime, timedelta

records = []

# -----------------------------
# ERP - 40 Purchase Orders
# -----------------------------
for i in range(1, 41):
    records.append({
        "source": "ERP",
        "purchase_order_id": f"PO{1000 + i}",
        "supplier_id": f"SUP{((i - 1) % 10) + 1:03d}",
        "product_id": f"PROD{((i - 1) % 20) + 1:03d}",
        "quantity": 50 + (i * 5),
        "unit_price": round(10.00 + (i * 1.25), 2),
        "order_date": "2026-09-01",
        "supplier_status": ["CONFIRMED", "PENDING", "SHIPPED"][i % 3]
    })


# -----------------------------
# OMS - 40 Customer Orders
# -----------------------------
destinations = [
    "Delhi",
    "Mumbai",
    "Bangalore",
    "Chennai",
    "Hyderabad",
    "Pune",
    "Kolkata",
    "Jaipur"
]

for i in range(1, 41):
    records.append({
        "source": "OMS",
        "order_id": f"ORD{1000 + i}",
        "customer_id": f"CUST{((i - 1) % 20) + 1:03d}",
        "product_id": f"PROD{((i - 1) % 20) + 1:03d}",
        "quantity": 5 + (i % 25),
        "order_date": "2026-09-01",
        "destination": destinations[(i - 1) % len(destinations)],
        "order_status": ["PROCESSING", "CONFIRMED", "SHIPPED"][i % 3]
    })


# -----------------------------
# IMS - 40 Inventory Records
# -----------------------------
start_time = datetime(2026, 9, 1, 14, 0, 0)

for i in range(1, 41):
    available = 10 + (i * 4)
    reserved = 5 + (i % 15)
    reorder_level = 30 + (i % 5) * 10

    if available <= reorder_level:
        inventory_status = "LOW_STOCK"
    else:
        inventory_status = "AVAILABLE"

    timestamp = start_time + timedelta(minutes=i - 1)

    records.append({
        "source": "IMS",
        "inventory_id": f"INV{1000 + i}",
        "product_id": f"PROD{((i - 1) % 20) + 1:03d}",
        "warehouse_id": f"WH{((i - 1) % 5) + 1:03d}",
        "available_quantity": available,
        "reserved_quantity": reserved,
        "reorder_level": reorder_level,
        "inventory_status": inventory_status,
        "timestamp": timestamp.isoformat()
    })


# -----------------------------
# Write records to JSON file
# -----------------------------
with open("sample_data.json", "w", encoding="utf-8") as file:
    json.dump(records, file, indent=2)

print(f"Successfully generated {len(records)} records.")
print("ERP records: 40")
print("OMS records: 40")
print("IMS records: 40")
print("Output file: sample_data.json")