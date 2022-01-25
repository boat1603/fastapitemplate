from fastapi import Request
from fastapi.routing import APIRouter

import json


router = APIRouter(prefix='/app_controller1')
@router.get("")
async def response_app_controller1():
    return {"data":"Hello World from app_controller1"}

@router.post("")
async def response_app_controller1_post(request: Request):
    # headers = request.headers
    data = await request.body()
    data = data.decode()
    data = json.loads(data)
    # Do Something
    return data