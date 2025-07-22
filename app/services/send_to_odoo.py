import httpx
import logging
from typing import List
from app.schemas.sale_order import SaleOrder
import os
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)

ODOO_API_URL = os.getenv("ODOO_API_URL")

async def post_orders_to_odoo(orders: List[SaleOrder]) -> dict:
    try:
        async with httpx.AsyncClient() as client:
            logger.info(f"Sending {len(orders)} orders to Odoo at {ODOO_API_URL}")
            response = await client.post(ODOO_API_URL, json=[order.dict() for order in orders])
            response.raise_for_status()

            return {
                "status": "success",
                "orders_sent": len(orders),
                "response": response.json()
            }

    except httpx.HTTPStatusError as e:
        logger.error(f"Error from Odoo API: {e.response.status_code} - {e.response.text}")
        raise HTTPException(status_code=500, detail=f"Odoo API error: {e.response.text}")

    except Exception as e:
        logger.exception("Unexpected error while posting to Odoo")
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")
