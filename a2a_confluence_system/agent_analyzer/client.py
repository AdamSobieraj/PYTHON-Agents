class Client:
    def __init__(self, url: str):
        self.url = url

    async def send(self, task_name: str, payload: dict):
        print(f"Sending {task_name} to {self.url} with {payload}")
        return {"status": "ok", "data": payload}
