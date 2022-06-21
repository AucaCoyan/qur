from enum import Enum


class Status(Enum):
    PENDING = "Pending"
    TODO = "To-Do"
    REJECTED = "Rejected"


Status.PENDING
