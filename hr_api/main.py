from fastapi import FastAPI
from hr_api.routes.employee_route import router as employee_router

app = FastAPI()

app = FastAPI(
    title="HR API",
    version="1.0.0"
)
app.include_router(employee_router)

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}