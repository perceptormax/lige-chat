from typing import Union

from fastapi import FastAPI

app = FastAPI()


"""
# OpenAI-liked API interface:
## List Models:
curl http://localhost:8000/v1/models
## Output
{
  "object": "list",
  "data": [
    {
      "id": "model-id-0",
      "object": "model",
      "created": 1686935002,
      "owned_by": "organization-owner"
    },
  ],
}
"""

@app.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
            "id": "chatglm_6b",
            "object": "model",
            "created": 1380869047,
            "owned_by": "zp"
            },
        ],
        }

"""
## Chat Completions:
curl http://localhost:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vicuna-7b-v1.3",
    "messages": [{"role": "user", "content": "Hello! What is your name?"}]
  }'
## Output:
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1677652288,
  "model": "gpt-3.5-turbo-0613",
  "choices": [{
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "\n\nHello there, how may I assist you today?",
    },
    "finish_reason": "stop"
  }],
  "usage": {
    "prompt_tokens": 9,
    "completion_tokens": 12,
    "total_tokens": 21
  }
}
"""
@app.get("/v1/chat/completions")
def chat_completion(model,
                    messages):
    resp = {} # TODO fill chat response
    return resp
    

"""
## Text Completions:
curl http://localhost:8000/v1/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vicuna-7b-v1.3",
    "prompt": "Once upon a time",
    "max_tokens": 41,
    "temperature": 0.5
  }'

## Embeddings:
curl http://localhost:8000/v1/embeddings \
  -H "Content-Type: application/json" \
  -d '{
    "model": "vicuna-7b-v1.3",
    "input": "Hello world!"
  }'  
"""



