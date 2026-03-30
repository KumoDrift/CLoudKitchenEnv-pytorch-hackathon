from pydantic import BaseModel
from typing import List, Optional


class Order(BaseModel):
    id: int
    name: str
    cook_time: int
    deadline: int
    value: float


class Slot(BaseModel):
    slot_id: int
    order_id: Optional[int]  # None if free
    remaining_time: int      # 0 if free


class Observation(BaseModel):
    current_time: int
    orders: List[Order]
    slots: List[Slot]


class Assignment(BaseModel):
    slot_id: int
    order_id: int


class Action(BaseModel):
    assignments: List[Assignment]


class Reward(BaseModel):
    value: float