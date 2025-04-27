"""
Utility functions for ASHA chatbot to retrieve relevant information and enhance responses.
"""

import json
import re
from career_knowledge import (
    CAREER_RESOURCES,
    INDUSTRY_INSIGHTS,
    CAREER_TRANSITIONS,
    CAREER_CHALLENGES,
    CAREER_DOCUMENTS,
    INSPIRING_LEADERS
)

def get_resources_by_stage(career_stage, category=None):
    """
    Retrieve career resources for a specific career stage.
    
    Args:
        career_stage (str): 'Starter', 'Restarter', or 'Riser'
        category (str, optional): Specific category of resources to retrieve
        
    Returns:
        dict: Resources matched to career stage and category
    """
    if career_stage not in CAREER_RESOURCES:
        return {}
    
    if category and category in CAREER_RESOURCES[career_stage]:
        return {category: CAREER_RESOURCES[career_stage][category]}
    
    return CAREER_RESOURCES[career_stage]

def get_industry_insights(industry):
    """
    Retrieve industry-specific insights.
    
    Args:
        industry (str): Industry name to look up
        
    Returns:
        dict: Industry insights or empty dict if not found
    """
    # Normalize input
    industry_lower = industry.lower()
    
    # Check for exact matches first
    if industry_lower in INDUSTRY_INSIGHTS:
        return INDUSTRY_INSIGHTS[industry_lower]
    
    # Check for partial matches
    for key in INDUSTRY_INSIGHTS:
        if key in industry_lower or industry_lower in key:
            return INDUSTRY_INSIGHTS[key]
    
    return {}

def get_career_challenge_advice(challenge_keyword):
    """
    Retrieve advice for common career challenges.
    
    Args:
        challenge_keyword (str): Keyword related to the challenge
        
    Returns:
        dict: Challenge information and strategies
    """
    # Check for direct match
    if challenge_keyword in CAREER_CHALLENGES:
        return CAREER_CHALLENGES[challenge_keyword]
    
    # Check for keyword matches in descriptions
    for challenge, data in CAREER_CHALLENGES.items():
        if challenge_keyword.lower() in data["description"].lower():
            return data
    
    return {}

def get_document_tips(document_type):
    """
    Retrieve tips for career documents (resume, cover letter, etc.)
    
    Args:
        document_type (str): Type of document (resume, cover_letter, etc.)
        
    Returns:
        list: Tips for the specified document type
    """
    # Normalize input
    doc_type = document_type.lower().replace(" ", "_")
    
    # Map common variations to standard keys
    mapping = {
        "resume": "resume_tips",
        "cv": "resume_tips",
        "cover": "cover_letter_tips",
        "cover_letter": "cover_letter_tips",
        "interview": "interview_preparation",
        "salary": "salary_negotiation_tips",
        "negotiation": "salary_negotiation_tips"
    }
    
    # Find the right key
    for key, value in mapping.items():
        if key in doc_type:
            if value in CAREER_DOCUMENTS:
                return CAREER_DOCUMENTS[value]
    
    return []

def get_transition_advice(from_stage, to_stage="Riser"):
    """
    Get advice for career transitions between stages.
    
    Args:
        from_stage (str): Starting career stage
        to_stage (str): Target career stage
        
    Returns:
        list: Transition advice strategies
    """
    transition_key = f"{from_stage}_to_{to_stage}"
    
    if transition_key in CAREER_TRANSITIONS:
        return CAREER_TRANSITIONS[transition_key]
    
    return []

def get_inspiring_leaders(field=None):
    """
    Get inspiring women leaders, optionally filtered by field.
    
    Args:
        field (str, optional): Field to filter by
        
    Returns:
        list: Leaders in the specified field or all fields
    """
    if not field:
        # Return some leaders from each field
        all_leaders = []
        for field_leaders in INSPIRING_LEADERS.values():
            all_leaders.extend(field_leaders[:1])  # Just take the first from each field
        return all_leaders
    
    # Normalize input
    field_lower = field.lower()
    
    # Check for exact matches
    if field_lower in INSPIRING_LEADERS:
        return INSPIRING_LEADERS[field_lower]
    
    # Check for partial matches
    for key, leaders in INSPIRING_LEADERS.items():
        if key in field_lower or field_lower in key:
            return leaders
    
    return []

def format_resources_for_response(resources, resource_type, limit=3):
    """
    Format resources into a readable string for responses.
    
    Args:
        resources (list): List of resource dictionaries
        resource_type (str): Type of resources being formatted
        limit (int): Maximum number of resources to include
        
    Returns:
        str: Formatted resources string
    """
    if not resources:
        return ""
    
    formatted = f"\n\nHere are some {resource_type} resources that might help:\n\n"
    
    for i, resource in enumerate(resources[:limit]):
        name = resource.get("name", "")
        description = resource.get("description", "")
        formatted += f"• **{name}**: {description}\n"
    
    return formatted

def extract_keywords(text, keywords_list):
    """
    Extract keywords from text based on a provided list.
    
    Args:
        text (str): Text to analyze
        keywords_list (list): List of keywords to look for
        
    Returns:
        list: Matched keywords found in the text
    """
    text_lower = text.lower()
    found_keywords = []
    
    for keyword in keywords_list:
        if keyword.lower() in text_lower:
            found_keywords.append(keyword)
    
    return found_keywords

def detect_career_document_inquiry(text):
    """
    Detect if the query is about career documents.
    
    Args:
        text (str): User query text
        
    Returns:
        str or None: Document type if detected, None otherwise
    """
    document_keywords = {
        "resume": ["resume", "cv", "curriculum vitae"],
        "cover_letter": ["cover letter", "application letter"],
        "interview": ["interview", "job interview", "interview questions", "interview prep"],
        "salary_negotiation": ["salary negotiation", "ask for raise", "compensation negotiation"]
    }
    
    text_lower = text.lower()
    
    for doc_type, keywords in document_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return doc_type
    
    return None

def detect_industry_mention(text):
    """
    Detect if an industry is mentioned in the text.
    
    Args:
        text (str): User query text
        
    Returns:
        str or None: Industry if detected, None otherwise
    """
    industries = list(INDUSTRY_INSIGHTS.keys())
    text_lower = text.lower()
    
    for industry in industries:
        if industry in text_lower:
            return industry
    
    # Check for common variants
    industry_variants = {
        "tech": "technology",
        "medical": "healthcare",
        "banking": "finance",
        "teaching": "education",
        "art": "creative",
        "design": "creative"
    }
    
    for variant, industry in industry_variants.items():
        if variant in text_lower:
            return industry
    
    return None

def detect_career_challenge(text):
    """
    Detect if a career challenge is mentioned in the text.
    
    Args:
        text (str): User query text
        
    Returns:
        str or None: Challenge type if detected, None otherwise
    """
    challenge_keywords = {
        "imposter_syndrome": ["imposter", "fraud", "not qualified", "don't deserve"],
        "work_life_balance": ["work life", "balance", "burnout", "overwhelmed", "stress"],
        "salary_negotiation": ["negotiate", "salary", "pay", "compensation", "raise"],
        "career_pivot": ["change career", "transition", "pivot", "switch field", "new industry"],
        "visibility": ["visibility", "recognition", "noticed", "overlooked", "credit"],
        "managing_up": ["manager", "boss", "supervisor", "managing up"]
    }
    
    text_lower = text.lower()
    
    for challenge, keywords in challenge_keywords.items():
        if any(keyword in text_lower for keyword in keywords):
            return challenge
    
    return None

def enhance_response_with_knowledge(query, career_stage, response):
    """
    Enhance the AI's response with relevant knowledge base information.
    
    Args:
        query (str): User's original query
        career_stage (str): User's career stage
        response (str): Original AI response
        
    Returns:
        str: Enhanced response with relevant knowledge
    """
    # First check if there are API connection issues in the response
    if "API" in response and "key" in response and "connection" in response:
        return response  # Return the error message as is without trying to enhance

    try:
        enhanced_response = response
        
        # Check for document inquiry
        doc_type = detect_career_document_inquiry(query)
        if doc_type:
            tips = get_document_tips(doc_type)
            if tips:
                enhanced_response += "\n\nHere are some specific tips that might help:\n\n"
                for tip in tips[:5]:  # Limit to 5 tips
                    enhanced_response += f"• {tip}\n"
        
        # Check for industry mention
        industry = detect_industry_mention(query)
        if industry:
            insights = get_industry_insights(industry)
            if insights:
                # Only add opportunities relevant to women
                if "opportunities" in insights:
                    enhanced_response += f"\n\nSome current opportunities in {industry.title()} include:\n\n"
                    for opportunity in insights["opportunities"][:3]:
                        enhanced_response += f"• {opportunity}\n"
        
        # Check for career challenge
        challenge = detect_career_challenge(query)
        if challenge:
            challenge_info = get_career_challenge_advice(challenge)
            if challenge_info and "strategies" in challenge_info:
                enhanced_response += "\n\nHere are some practical strategies that might help:\n\n"
                for strategy in challenge_info["strategies"][:3]:
                    enhanced_response += f"• {strategy}\n"
        
        # Add resource recommendations based on career stage
        if career_stage:
            # Determine what type of resources would be most relevant
            resource_category = None
            if "network" in query.lower() or "connect" in query.lower():
                resource_category = "networking"
            elif "skill" in query.lower() or "learn" in query.lower():
                resource_category = "skill_building"
            elif "job" in query.lower() or "search" in query.lower() or "find" in query.lower():
                resource_category = "job_search"
            elif "lead" in query.lower() or "manage" in query.lower() and career_stage == "Riser":
                resource_category = "leadership"
            
            resources = get_resources_by_stage(career_stage, resource_category)
            
            # Format the resources to add to the response
            if resources and resource_category:
                enhanced_response += format_resources_for_response(
                    resources[resource_category], 
                    resource_category.replace("_", " ")
                )
        
        return enhanced_response
    except Exception as e:
        print(f"Error enhancing response: {str(e)}")
        return response  # Return original response if enhancement fails 