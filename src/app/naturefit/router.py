from fastapi import APIRouter
from src.app.naturefit.schemas.common import Message,InputMessage,ResultMessage
from src.app.naturefit import controller as nf_controller



router=APIRouter()


@router.post("/chat/")
async def chat(message: InputMessage):
    user_message = message.user_input.lower()
    print(f"Received user message: {user_message}")  # Debugging line

    # Default bot response
    bot_response = "I'm sorry, I don't understand that. Could you rephrase?"

    # Basic pattern matching for specific queries
    if "hello" in user_message or "hi" in user_message:
        bot_response = "Hello! How can I assist you today?"
    elif "how are you" in user_message:
        bot_response = "I'm doing well, thank you for asking!"
    elif "bye" in user_message:
        bot_response = "Goodbye! Have a great day!"
    elif "thank you" in user_message or "thanks" in user_message:
        bot_response = "You're welcome!"
    
    # Fetch product information from MongoDB
    elif "products" in user_message or "product" in user_message:
        bot_response = await nf_controller.get_products()
    
    # Fetch service information from MongoDB
    elif "services" in user_message or "service" in user_message:
        bot_response = await nf_controller.get_services()

    # Fetch brand information from MongoDB
    elif "brand" in user_message or "about the brand" in user_message or "your brand" in user_message:
        bot_response = await nf_controller.get_brand()

    # Add more dynamic queries as needed
    elif "help" in user_message:
        bot_response = "I can assist you with queries about our products, services, brand, and more. Just ask!"
    
    # If no match, fallback to default response
    print(f"Bot response: {bot_response}")  # Debugging line
    
  
    return {"user_message": message.user_input, "bot_response": bot_response}


@router.get("/history/")
async def get_history():
    # Fetch chat history from MongoDB
    response=await nf_controller.msg_response()
    return {"msg":"success","result":response}

@router.get("/test")
async def test():
    return True


