from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float
    description: str | None = None

class ProductUpdate(ProductCreate):
    pass