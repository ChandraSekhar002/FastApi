import os
import requests
from fastapi import HTTPException
from dotenv import load_dotenv
from app.schemas.send_sale_order import SaleOrderSend
import traceback
import httpx
from app.services.login import get_login_token

load_dotenv()

async def handle_sale_order(order: SaleOrderSend):
    try:
        print("✅ Received sale order:", order)

        # Step 1: Login and get token
        
        
        token = get_login_token()
        print("🔑 Token received:", token)
        if not token:
            raise Exception("No token received")

        # Step 2: Prepare order payload
        order_payload = {
            "clientId": 1043,
            "clientName": "BENCHMASTER FURNITURE",
            "custOrderId":str(order.order_id) ,
            "salesChannelId": 1009,
            "orderType": "B2B",
            "shipCustomerName": order.partner,
            "shipCompanyName": "eArBOr",
            "shipAddress1": "1234 Elm St",
            "shipCity":"USA",
            "shipState": "New York",
            "shipPostalCode": "10001",
            "shipCountry": "USA",
            "carrierService": "FedEx 2Day",
            "carrierServiceId": 3154,
            "Carrier":"FedEx",
            "storeid": "1001",
            "WhId":"9001",
            "SalesChannelName": "Inventory",
            "orderItems": [
                {
                    "sku": "4147WA-001 ARM SET",
                    "orderqty":int(line.quantity),
                    "sequenceNumber": str(index + 1)
                } for index, line in enumerate(order.order_lines)
            ]
        }

        # Step 3: Send Order to API
        order_url = os.getenv("CREATEORDER")
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "accept": "*/*"
        }
        print("📤 Sending order to:", order_url)
        # print("Order Payload",order_payload)
        async with httpx.AsyncClient() as client:
            response = await client.post(order_url, json=order_payload, headers=headers)

        # order_response = requests.post(order_url, json=order_payload, headers=headers)
        if response.status_code not in [200, 201]:
            try:
                error_data = response.json()
            except Exception:
                error_data = {"error": "Invalid response format", "raw": response.text}
        
    # Return detailed message to client
            raise HTTPException(
        status_code=response.status_code,
        detail={
            "status": "failed",
            "message": "Order post failed",
            "api_error": error_data,
        }
    )
        response_data=response.json()
        box_order_id=response_data.get("data")
        return {
            "status": "success",
            "message": f"Order {order.custOrderId if hasattr(order, 'custOrderId') else 'created'} sent successfully",
            "api_response": response.json(),
            "Box_order_id": box_order_id
        }


    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))
