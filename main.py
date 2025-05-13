from fastapi import FastAPI
from routes.routes import router as crawler_router

app = FastAPI()

app.include_router(crawler_router, prefix="")

@app.get("/")
async def root():
    return {"message": "Crawler de guayos"}
