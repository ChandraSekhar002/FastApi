from fastapi import APIRouter
from app.schemas.purchase_order import PurchaseOrder
from app.services.purchase_order_service import handle_purchase_order
router=APIRouter()
@router.post("/purchase_order")
def receive_purchase_order(order:PurchaseOrder):
    return handle_purchase_order(order)