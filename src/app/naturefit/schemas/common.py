from pydantic import BaseModel
class Message(BaseModel):
    user_message: str
    bot_response: str
class InputMessage(BaseModel):
    user_input: str
        
class ResultMessage(BaseModel):
    message_result: str       