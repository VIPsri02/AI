class SessionMemory:
    def __init__(self):
        self.history = []

    def add(self, user, assistant):
        self.history.append({"user": user, "assistant": assistant})

    def get(self):
        return "\n".join(
            [f"User: {h['user']}\nAssistant: {h['assistant']}" for h in self.history]
        )