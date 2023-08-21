from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class ModelInfo(BaseModel):
    id: str
    object: str = "model"
    created: int
    owned_by: str


class ModelList(BaseModel):
    object: str = "list"
    data: List[ModelInfo]


class FunctionCallInfo(BaseModel):
    name: str
    arguments: str

class ChatMessage(BaseModel):
    role: str
    content: Optional[str]
    function_call: FunctionCallInfo


class ChatCompletionChoice(BaseModel):
    index: int
    message: ChatMessage
    finish_reason: str


class Usage(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int


class ChatCompletion(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str # ModelInfo.id
    choices: list[ChatCompletionChoice]
    usage: Usage


class APIResult(BaseModel):
    api_end_point: str
    called_at: datetime
    input: str
    openai_response: Optional[ChatCompletion]