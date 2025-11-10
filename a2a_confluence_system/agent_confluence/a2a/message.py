class Message:
    async def reply(self, payload: dict):
        print(f"Replying with: {payload}")
