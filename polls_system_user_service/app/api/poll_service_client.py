import httpx

class PollServiceClient:
    POLL_SERVICE_URL = "http://localhost:8010"

    @staticmethod
    async def delete_user_answers(user_id: int):
        # Call Poll Service to delete the user's answers
        poll_service_endpoint = f"{PollServiceClient.POLL_SERVICE_URL}/answers/user/{user_id}"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.delete(poll_service_endpoint)
                if response.status_code != 200:
                    raise Exception(
                        f"Failed to delete answers for user {user_id}: {response.text}"
                    )
            except Exception as e:
                raise Exception(f"Error communicating with Poll Service: {str(e)}")
