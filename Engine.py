from enum import Enum


class EngineTypeEnum(Enum):
    ELECTRIC = "electric"
    DIESEL = "diesel"
    GASOLINE = "gasoline"


class Engine:

    def __init__(self, engine_type: EngineTypeEnum):
        self.type = engine_type
