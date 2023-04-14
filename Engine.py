from enum import Enum


class EngineTypeEnum(Enum):
    ELECTRIC = "electric"
    DIESEL = "diesel"
    GASOLINE = "gasoline"


class Engine:

    def __init__(self, engine_type: EngineTypeEnum, description: str):
        self.type = engine_type
        self.description = description

    def __str__(self) -> str:
        return self.description
