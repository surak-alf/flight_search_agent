# agent.py
import os
from mcp_client import MCPClient
from prompts import create_flight_search_prompt, create_result_formatting_prompt
import google.generativeai as genai
from config import GOOGLE_API_KEY  

# Configure Gemini API (replace with your actual API key)
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    raise ValueError("Please set the GOOGLE_API_KEY environment variable.")
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash') # Or 'gemini-pro-vision' for multimodal

class FlightSearchAgent:
    def __init__(self):
        self.mcp_client = MCPClient()

    def process_user_query(self, user_query: str):
        """
        Processes the user's query to extract flight search parameters and retrieve results.
        """
        prompt = create_flight_search_prompt(user_query)
        response = model.generate_content(prompt)
        extracted_parameters = self._parse_extracted_parameters(response.text)

        if all(extracted_parameters.values()):
            results = self.mcp_client.search_flights(**extracted_parameters)
            if results:
                formatting_prompt = create_result_formatting_prompt(results)
                formatted_response = model.generate_content(formatting_prompt)
                return formatted_response.text
            else:
                return "No flights found based on your criteria."
        else:
            missing_info = [k for k, v in extracted_parameters.items() if not v]
            return f"Could you please provide more details? Missing: {', '.join(missing_info)}"

    def _parse_extracted_parameters(self, text: str):
        """
        Parses the Gemini response to extract flight search parameters.
        This is a basic implementation and might need refinement.
        """
        params = {}
        for line in text.split('\n'):
            if "Origin:" in line:
                params['origin'] = line.split("Origin:")[1].strip()
            elif "Destination:" in line:
                params['destination'] = line.split("Destination:")[1].strip()
            elif "Date (YYYY-MM-DD):" in line:
                params['date'] = line.split("Date (YYYY-MM-DD):")[1].strip()
        return params

# Example usage
if __name__ == "__main__":
    agent = FlightSearchAgent()
    user_input = "Find me flights from Nairobi to Addis Ababa next month"
    response = agent.process_user_query(user_input)
    print(f"User Query: {user_input}")
    print(f"Agent Response:\n{response}")

    user_input_2 = "Flights to Kigali on 2025-06-15 from Entebbe"
    response_2 = agent.process_user_query(user_input_2)
    print(f"\nUser Query: {user_input_2}")
    print(f"Agent Response:\n{response_2}")
