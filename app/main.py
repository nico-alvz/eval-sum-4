from fastapi import FastAPI
from app.routers import auth, products
from app.database import Base, engine

app = FastAPI()

app.include_router(auth.router)
app.include_router(products.router)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)