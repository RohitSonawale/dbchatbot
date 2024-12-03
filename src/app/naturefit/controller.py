from src.configure.connection.mongodb import (
    products_collection,
    services_collection,
    brands_collection,
    messages_collection)
# Fetch product details from MongoDB
async def get_products():
    products = []
    async for product in products_collection.find():
        products.append({
            "name": product.get("name"),
            "description": product.get("description"),
            "price": product.get("price")
        })

    if not products:
        return "I'm sorry, I couldn't find any products."

    # Return a formatted list of available products
    response = "Here are the available products:\n"
    for product in products:
        response += f"- {product['name']}: {product['description']} (Price: {product['price']})\n"
    
    return response

# Fetch service details from MongoDB
async def get_services():
    services = []
    async for service in services_collection.find():
        services.append({
            "name": service.get("name"),
            "description": service.get("description"),
            "price": service.get("price")
        })

    if not services:
        return "I'm sorry, I couldn't find any services."

    # Return a formatted list of available services
    response = "Here are the available services:\n"
    for service in services:
        response += f"- {service['name']}: {service['description']} (Price: {service['price']})\n"
    
    return response

# Fetch brand details from MongoDB (All documents)
# Fetch brand details from MongoDB (All documents)
async def get_brand():
    # Fetch all brand documents from the brands collection
    brands = []
    async for brand in brands_collection.find():
        brands.append({
            "name": brand.get("name")
        })

    if not brands:
        return "I'm sorry, I couldn't find any information about the brands."

    # Return a formatted list of all available brands (only brand name)
    response = "Here are the available brands:\n"
    response += "\n".join([brand['name'] for brand in brands])  # Join brand names with newline
    
    return response
async def msg_response():
    messages = []
    messages=messages_collection.find()
    
        
    return messages