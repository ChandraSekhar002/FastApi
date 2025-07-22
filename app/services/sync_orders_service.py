import httpx
import logging
from fastapi import HTTPException
import os
from dotenv import load_dotenv
from app.services.login import get_login_token

load_dotenv()
logger = logging.getLogger(__name__)

async def fetch_and_forward_orders():
    try:
        # Load config from environment
        EXTERNAL_API_URL = os.getenv("EXTERNAL_API_URL")
       
        ODOO_API_URL = os.getenv("ODOO_API_URL")
        

        async with httpx.AsyncClient() as client:
          
            token =  get_login_token()
            if not token:
                raise HTTPException(status_code=401, detail="No token received from login")

            print("✅ Token received:", token)

            # Step 2: Fetch sale orders using token
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
                "accept": "*/*"
            }

            print(f"📦 Fetching orders from {EXTERNAL_API_URL}...")
            response = await client.get(EXTERNAL_API_URL, headers=headers)
            response.raise_for_status()
            print("📦 Orders fetched successfully:", response.status_code,response)
            orders = response.json()

            print(f"📦 Orders received: {len(orders)} orders",orders)

            for order in orders:
                order["order_id"] = str(order.get("order_id", ""))

            # Step 3: Forward to Odoo internal API
            print(f"➡️ Forwarding orders to {ODOO_API_URL}...")
            post_response = await client.post(ODOO_API_URL, json=orders)
            post_response.raise_for_status()

            return {
                "status": "success",
                "orders_fetched": len(orders),
                "odoo_response": post_response.json()
            }

    except httpx.RequestError as e:
        logger.error(f"HTTPX error occurred: {e}")
        raise HTTPException(status_code=500, detail=f"HTTPX error: {str(e)}")

    except Exception as e:
        logger.exception("Unexpected error during fetch and forward")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
