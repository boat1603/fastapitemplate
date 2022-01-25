import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import IncludeAPIRouter

import config

def create_application():
    app = FastAPI(docs_url=config.application_config.docs_url, redoc_url=config.application_config.redoc_url)
    app.include_router(IncludeAPIRouter())
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=config.application_config.allow_credentials,
        allow_methods=config.application_config.allow_methods,
        allow_headers=config.application_config.allow_headers,
    )
    return app

app = create_application()

@app.on_event("shutdown")
async def app_shutdown():
    print("On App Shutdown i will be called.")

# uvicorn.run("main:app", host=config.application_config.HOST, port=config.application_config.PORT, use_colors=True,reload=False)
# OR Run: uvicorn main:app --host 0.0.0.0 --port 8000
# Should add --reload (Or set reload=True) in Dev Environment