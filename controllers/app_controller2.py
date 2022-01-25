from fastapi import Request
from fastapi.routing import APIRouter


router = APIRouter(prefix='/app_controller2')
@router.get("")
async def response_app_controller2():
    return {"data":"Hello World from app_controller2"}

@router.get("/headers")
async def response_app_controller2_get_headers(request:Request):
    headers = request.headers
    return headers