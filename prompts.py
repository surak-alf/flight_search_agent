# prompts.py

def create_flight_search_prompt(user_query: str):
    """
    Creates a prompt for Gemini to extract flight search parameters.
    """
    prompt = f"""You are a helpful assistant designed to extract flight search parameters
from user queries. Please identify the origin city, destination city, and travel date
from the following query. If any information is missing or ambiguous, indicate that.

User Query: {user_query}

Extracted Parameters:
Origin:
Destination:
Date (YYYY-MM-DD):
"""
    return prompt

def create_result_formatting_prompt(flight_results: list):
    """
    Creates a prompt for Gemini to format flight search results nicely.
    """
    if not flight_results:
        return "No flights found."

    results_string = "\n".join([f"- Flight from {res['departure_city']} to {res['arrival_city']} on {res['date']} at {res['departure_time']} - Price: {res['price']}" for res in flight_results[:5]]) # Show top 5

    prompt = f"""Here are some flight search results:
{results_string}

Please format these results in a user-friendly way, highlighting the key information
for each flight (departure city, arrival city, date, time, price).
"""
    return prompt
