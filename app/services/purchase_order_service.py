from fastapi import HTTPException
def handle_purchase_order(order):
    try:
        print("✅ Received Purchase order:", order)
        # process / store / log
        return {"status": "success", "message": f"Order {order.name} received"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))