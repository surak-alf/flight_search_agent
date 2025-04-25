# mcp_client.py
import requests
from config import MCP_SERVER_URL

class MCPClient:
    def __init__(self):
        self.base_url = MCP_SERVER_URL

    def search_flights(self, origin: str, destination: str, date: str, **kwargs):
        """
        Sends a flight search request to the MCP server.

        Args:
            origin: Departure city.
            destination: Arrival city.
            date: Travel date (YYYY-MM-DD).
            **kwargs: Additional parameters as needed by the MCP server.

        Returns:
            The JSON response from the MCP server, or None if an error occurs.
        """
        endpoint = f"{self.base_url}/flights"  # Adjust the endpoint as needed
        params = {
            "origin": origin,
            "destination": destination,
            "date": date,
            **kwargs,
        }
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()  # Raise an exception for bad status codes
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with MCP server: {e}")
            return None

# Example usage (you'll likely call this from your agent)
if __name__ == "__main__":
    client = MCPClient()
    results = client.search_flights(origin="London", destination="New York", date="2025-05-10")
    if results:
        print("Flight Search Results:")
        print(results)
    else:
        print("Flight search failed.")
