from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.service.user_service import UserService
from app.database import get_db
from app.models.schemas import UserCreate, UserUpdate, UserResponse


router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    return await UserService.create_user(db, user_data)

@router.get("/{user_id}", response_model=UserResponse)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = await UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.from_orm(user)

@router.get("/", response_model=list[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
    users = await UserService.get_all_users(db)
    return [UserResponse.from_orm(user) for user in users]

@router.put("/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, updates: UserUpdate, db: Session = Depends(get_db)):
    user = await UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return await UserService.update_user(db, user_id, updates)

@router.delete("/{user_id}", response_model=dict)
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = await UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await UserService.delete_user(db, user_id)
    return {"message": "User and associated answers deleted"}

@router.put("/{user_id}/register", response_model=dict)
async def register_user(user_id: int, db: Session = Depends(get_db)):
    user = await UserService.register_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": f"User {user_id} is now registered"}

@router.get("/{user_id}/is_registered", response_model=dict)
async def is_registered_user(user_id: int, db: Session = Depends(get_db)):
    user = await UserService.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"is_registered": user.is_registered}
