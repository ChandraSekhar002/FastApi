

from fastapi import APIRouter
from app.services.send_to_odoo import post_orders_to_odoo  # create this if not exists
   
from typing import List
from app.schemas.sale_order import SaleOrder
from typing import Any
router = APIRouter()
@router.post("/test_orders", response_model=dict)
async def test_orders(orders: List[SaleOrder]) -> Any:
     result= await post_orders_to_odoo(orders)
     print("Orders sent to Odoo:", result)

   
