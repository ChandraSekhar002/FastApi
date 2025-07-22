# app/api/v1/endpoints/receive_sale_orders.py

from fastapi import APIRouter
from app.services.sync_orders_service import fetch_and_forward_orders
from app.services.send_to_odoo import post_orders_to_odoo 

from typing import List
from app.schemas.sale_order import SaleOrder
from typing import Any

router = APIRouter()


@router.get("/sync_orders", response_model=dict)
async def sync_orders() -> Any:
    """
    Fetch orders from external API and forward them to Odoo/FastAPI in a single call.
    """
    return await fetch_and_forward_orders()

@router.get("/test_orders")
async def get_test_orders():
    return {
        "status": "received",
        "orders_count": 1,
        "orders": [
            {
                "order_id": "box123",
                "partner": "Sreekanth Valmiki",
                "partner_city": "Hyderabad",
                "date_order": "2025-07-17 10:30:00",
                "name":"S00003",
                "amount_total": 50200,
                "order_lines": [
                    {
                        "product": "Sport Shoes",
                        "quantity": 1,
                        "price_unit": 50000.0,
                        "price_subtotal": 50000.0
                    },
                    {
                        "product": "NOtebook",
                        "quantity": 2,
                        "price_unit": 100.0,
                        "price_subtotal": 200.0
                    }
                    
                ]
            }
        ]
    }