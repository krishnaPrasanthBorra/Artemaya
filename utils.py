def enhance_response_with_knowledge(query, career_stage, response):
    """
    Enhances the AI's response with relevant knowledge base information
    
    Args:
        query (str): The user's query
        career_stage (str): The user's career stage (Starter, Restarter, Riser)
        response (str): The initial AI response
        
    Returns:
        str: The enhanced response
    """
    try:
        # First check if API is facing issues
        if "API" in response and "key" in response and "connection" in response:
            return response  # Return the API error message as is
            
        # Rest of the function implementation
        // ... existing code ...
    except Exception as e:
        # If any error occurs in enhancement, return the original response
        print(f"Error enhancing response: {str(e)}")
        return response 