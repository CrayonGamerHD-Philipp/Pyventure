from pydantic import BaseModel
from typing import List, Tuple

class Player(BaseModel):
    id: int
    name: str
    email: str
    password: str
    health: int
    coins: int
    resources: List[Tuple[str, int]]
    inventory: List[Tuple[str, int]]
    progress: List[Tuple[str, str]]
