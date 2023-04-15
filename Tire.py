class Tire:

    def __init__(self, tire_type: str, description: str):
        self.type = tire_type
        self.description = description

    def __str__(self) -> str:
        return self.description
