from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class ShopperBase(BaseModel):
    username: str


class ShopperCreate(ShopperBase):
    password: str


class Shopper(ShopperBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True