from fastapi import APIRouter, HTTPException, Request
from typing import List
from app.schemas.sale_order import SaleOrder  # You'll define this schema
import logging

router = APIRouter()
logger = logging.getLogger(__name__)

buffered_orders: List[SaleOrder] = []
@router.post("/post_orders_to_odoo")
async def post_orders_to_odoo(orders: List[SaleOrder]):
     try:
        buffered_orders.clear()  # Optional: clear old orders on each post
        buffered_orders.extend(orders)
        logger.info(f"📥 Received and buffered {len(orders)} orders")
        return {"status": "success", "received": len(orders)}
     except Exception as e:
        logger.exception("Error buffering orders")
        raise HTTPException(status_code=500, detail="Failed to buffer orders")
     
@router.get("/get_orders", response_model=List[SaleOrder])
async def get_buffered_orders():
    return buffered_orders
