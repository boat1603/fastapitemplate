from fastapi.routing import APIRouter
from controllers.app_controller1 import router as router_app_controller1
from controllers.app_controller2 import router as router_app_controller2
class IncludeAPIRouter(object):
    def __new__(cls):
        router = APIRouter()
        router.include_router(router_app_controller1, prefix='/api/v1', tags=['app_controller1'])
        router.include_router(router_app_controller2, prefix='/api/v1', tags=['app_controller2'])
        return router