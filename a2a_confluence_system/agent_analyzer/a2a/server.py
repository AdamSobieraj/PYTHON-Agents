class Server:
    def __init__(self, name: str, port: int):
        self.name = name
        self.port = port
        self.handlers = {}

    def handle(self, task_name: str):
        def decorator(func):
            self.handlers[task_name] = func
            return func
        return decorator

    def run(self):
        print(f"Server {self.name} running on port {self.port}")
        # tutaj logika nasłuchiwania wiadomości

