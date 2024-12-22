from app.repository.user_repository import UserRepository
from app.models.user_model import User
from app.api.poll_service_client import PollServiceClient

class UserService:
    POLL_SERVICE_URL = "http://localhost:8010"

    @staticmethod
    async def create_user(db, user):
        user = User(**user.dict())
        return await UserRepository.create_user(db, user)

    @staticmethod
    async def get_user_by_id(db, user_id):
        return await UserRepository.get_user_by_id(db, user_id)

    @staticmethod
    async def update_user(db, user_id, updates):
        return await UserRepository.update_user(db, user_id, updates.dict())

    @staticmethod
    async def delete_user(db, user_id):
        # Call Poll Service to delete the user's answers
        try:
            await PollServiceClient.delete_user_answers(user_id)
        except Exception as e:
            raise Exception(f"Failed to delete user answers in Poll Service: {str(e)}")

        # Delete the user from the database
        await UserRepository.delete_user(db, user_id)

    @staticmethod
    async def register_user(db, user_id):
        user = await UserRepository.get_user_by_id(db, user_id)
        if not user:
            return None
        return await UserRepository.register_user(db, user_id)

    @staticmethod
    async def get_all_users(db):
        return await UserRepository.get_all_users(db)
