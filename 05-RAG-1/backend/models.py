from pydantic import BaseModel
from typing import List, Optional, Literal, Union


class Message(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    sourcePages: Optional[List[int]] = None  # Optional, used by assistant only


class ChatRequest(BaseModel):
    query: str
    messages: List[Message]