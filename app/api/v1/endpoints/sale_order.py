from fastapi import APIRouter
from app.schemas.send_sale_order import SaleOrderSend
from app.services.sale_order_service import handle_sale_order
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/sale_order")
async def receive_sale_order(order: SaleOrderSend):
    print("Received Sale Order:", order)
    result = await handle_sale_order(order)  # ✅ Must use await here

    print("Sale Order Processed:", result)
    return JSONResponse(content=result)
