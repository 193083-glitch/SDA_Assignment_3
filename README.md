# SDA Assignment 2 - Sample Data & Kafka Producer

## Student Information

Name: Krati  
Roll Number: 193083

## Industry

Logistics / Supply Chain

This assignment builds on Assignment 1, which identified three operational data sources for a supply-chain pipeline:

1. ERP System - Procurement and Purchase Orders
2. Order Management System (OMS)
3. Inventory Management System (IMS)

## Data Sources

### 1. ERP System - Procurement and Purchase Orders

The ERP source provides procurement and purchase-order information, including suppliers, products, quantities, prices, order dates, and supplier status.

Example fields:

- `purchase_order_id`
- `supplier_id`
- `product_id`
- `quantity`
- `unit_price`
- `order_date`
- `supplier_status`

### 2. Order Management System (OMS)

The OMS source provides customer-order and fulfillment information.

Example fields:

- `order_id`
- `customer_id`
- `product_id`
- `quantity`
- `order_date`
- `destination`
- `order_status`

### 3. Inventory Management System (IMS)

The IMS source provides current inventory information used to compare supply with demand and identify products requiring replenishment.

Example fields:

- `inventory_id`
- `product_id`
- `warehouse_id`
- `available_quantity`
- `reserved_quantity`
- `reorder_level`
- `inventory_status`
- `timestamp`

## Sample Data

The sample data is stored in:

sample_data.json