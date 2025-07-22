
#app/main.py
from fastapi import FastAPI
from app.api.v1.endpoints import sale_order
from app.api.v1.endpoints import purchase_order
from app.api.v1.endpoints import sync_orders
from app.api.v1.endpoints import post_orders_to_odoo

app = FastAPI(title="FastAPI Sales Order API")

app.include_router(sale_order.router, prefix="/api/v1", tags=["Sale Orders"])
app.include_router(purchase_order.router,prefix="/api/v1",tags=["Purchase Orders"])
app.include_router(sync_orders.router,prefix="/api/v1",tags=["Receive Sale Orders"])
app.include_router(post_orders_to_odoo.router, prefix="/api/v1", tags=["Post Orders to Odoo"])






















# from fastapi import FastAPI, Request
# from pydantic import BaseModel
# from typing import List, Optional
# import requests

# app = FastAPI()

# # Define schema for order lines
# class OrderLine(BaseModel):
#     product: str
#     quantity: float
#     price_unit: float
#     subtotal: float

# # Define schema for incoming sale order
# class SaleOrder(BaseModel):
#     name: str
#     partner: str
#     date_order: str
#     amount_total: float
#     order_lines: List[OrderLine]

# @app.post("/api/sale-order/")
# async def receive_sale_order(order: SaleOrder):
#     print("✅ Sale Order Received from Odoo:")
#     print(order)

#     # Example: Forward to another service (Box or another API)
#     # try:
#     #     # Replace with your actual target URL
#     #     forward_url = "http://external-api-or-box.com/webhook/"
#     #     response = requests.post(forward_url, json=order.dict())
#     #     print("📤 Forwarded to Box/another API:", response.status_code)
#     # except Exception as e:
#     #     print("❌ Failed to forward to external API:", str(e))

#     return {"message": "Sale order received", "order_id": order.name}
