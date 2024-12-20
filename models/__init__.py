from dataclasses import dataclass
from typing import Optional

@dataclass
class Book:
    id: int
    title: str
    author: str

@dataclass
class Member:
    id: int
    name: str
    email: str