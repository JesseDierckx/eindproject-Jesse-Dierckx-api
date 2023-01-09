from sqlalchemy.orm import Session

import models
import auth
import schemas


def get_shopper(db: Session, shopper_id: int):
    return db.query(models.Shopper).filter(models.Shopper.id == shopper_id).first()


def get_shopper_by_username(db: Session, username: str):
    return db.query(models.Shopper).filter(models.Shopper.username == username).first()


def get_shoppers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Shopper).offset(skip).limit(limit).all()


def create_shopper(db: Session, shopper: schemas.ShopperCreate):
    hashed_password = auth.get_password_hash(shopper.password)
    db_shopper = models.Shopper(username=shopper.username, hashed_password=hashed_password)
    db.add(db_shopper)
    db.commit()
    db.refresh(db_shopper)
    db.refresh(db_shopper)
    return db_shopper


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_shopper_item(db: Session, item: schemas.ItemCreate, shopper_id: int):
    db_item = models.Item(**item.dict(), owner_id=shopper_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

#def delete_shopper_item(db: Session, shopper_id: int):
#    db_item = models.Item( owner_id=shopper_id)
#    db.delete(db_item)
#    db.commit()
#    db.refresh(db_item)
#    return ("the item has been deleted")