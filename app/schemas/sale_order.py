from pydantic import BaseModel
from typing import List

class OrderLine(BaseModel):
    product: str
    quantity: float
    price_unit: float
    subtotal: float

class SaleOrder(BaseModel):
    order_id:int
    name: str
    partner: str
    date_order: str
    amount_total: float
    box_order_id:str
    order_lines: List[OrderLine]
