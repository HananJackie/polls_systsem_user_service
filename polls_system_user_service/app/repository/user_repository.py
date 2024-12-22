from sqlalchemy.orm import Session
from app.models.user_model import User

class UserRepository:
    @staticmethod
    async def create_user(db: Session, user: User):
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    async def get_user_by_id(db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    async def update_user(db: Session, user_id: int, updates: dict):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            for key, value in updates.items():
                setattr(user, key, value)
            db.commit()
            db.refresh(user)
        return user

    @staticmethod
    async def delete_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()

    @staticmethod
    async def register_user(db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.is_registered = True
            db.commit()
            db.refresh(user)
        return user

    @staticmethod
    async def get_all_users(db):
        return db.query(User).all()
