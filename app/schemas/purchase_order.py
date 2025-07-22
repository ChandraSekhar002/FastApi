from pydantic import BaseModel
from typing import List

class OrderLine(BaseModel):
    product: str
    quantity: float
    price_unit: float
    subtotal: float

class PurchaseOrder(BaseModel):
    name: str
    partner: str
    date_order: str
    amount_total: float
    order_lines: List[OrderLine]
