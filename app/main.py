from fastapi import FastAPI
from app.api.routes import router as items_router

app = FastAPI(
    title="Cloud Native App",
    description="A cloud-native application built with FastAPI",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {"message": "Hello Cloud Native World!"}

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Include the routes
app.include_router(items_router)
