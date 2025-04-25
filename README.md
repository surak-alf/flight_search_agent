# Flight Search Agent with ADK, MCP Client, and Gemini 2.0 Flash

## Overview

This project implements a flight search agent that leverages the Agent Development Kit (ADK) as an MCP (Model Context Protocol) client and utilizes the Google Gemini 2.0 Flash model for natural language understanding and response generation. The agent interacts with an MCP server (which you will need to set up or integrate with) to retrieve flight information based on user queries. A Streamlit user interface is included for easy interaction with the agent.

## Project Structure
```
flight_search_agent/
├── agent.py                  # Main agent logic (ADK, Gemini, tools)
├── mcp_client.py             # Handles communication with MCP server
├── prompts.py                # Contains prompts for Gemini
├── config.py                 # Configuration settings (MCP server URL, etc.)
├── ui.py                     # Streamlit user interface
├── requirements.txt
├── README.md
├── .gitignore
└── venv/       
```
## Setup and Installation

1.  **Clone the repository (if applicable):**
    ```bash
    git clone <https://github.com/surak-alf/flight_search_agent>

    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows:
    .\venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```
    This will install libraries such as `requests`, `google-generativeai`, and `streamlit`.

4.  **Set up your Google Gemini API key:**
    * Obtain a Google Cloud project with the Gemini API enabled and generate an API key.
    * Set the `GOOGLE_API_KEY` environment variable on your system. You can do this in your terminal before running the script:
        ```bash
        # On macOS/Linux:
        export GOOGLE_API_KEY="YOUR_ACTUAL_GEMINI_API_KEY"
        # On Windows (PowerShell):
        $env:GOOGLE_API_KEY = "YOUR_ACTUAL_GEMINI_API_KEY"
        ```
        Alternatively, you can set it permanently in your system's environment variables.

5.  **Configure the MCP Server URL:**
    * Open the `config.py` file.
    * Replace `"YOUR_MCP_SERVER_URL_HERE"` with the actual URL of your MCP server that provides flight data. **Note:** You will need to have an MCP server set up separately to provide flight information. This project focuses on the client side (the agent).

## Running the Application

1.  **Ensure your virtual environment is activated.**

2.  **Run the Streamlit user interface:**
    ```bash
    streamlit run ui.py
    ```
    This command will open a new tab in your web browser with the flight search agent UI.

3.  **Interact with the agent:**
    * Enter the departure city, arrival city, and desired travel date in the provided fields.
    * Click the "Search Flights" button.
    * The agent will process your query using Gemini 2.0 Flash, communicate with the configured MCP server, and display the results in the UI.

## Code Overview

* **`agent.py`:** Contains the main logic for the flight search agent. It uses the `google-generativeai` library to interact with the Gemini model for understanding user queries and formatting responses. It also interacts with the `MCPClient` to send requests to the MCP server.
* **`mcp_client.py`:** Implements the `MCPClient` class, which handles the communication with the MCP server using the `requests` library. It defines a `search_flights` function to send flight search requests to the server.
* **`prompts.py`:** Contains functions that generate prompts for the Gemini model. These prompts guide Gemini to extract flight search parameters from user queries and format the flight search results.
* **`config.py`:** Stores configuration settings for the application, such as the URL of the MCP server.
* **`ui.py`:** Defines the Streamlit user interface for interacting with the flight search agent. It takes user input for origin, destination, and date, sends it to the agent, and displays the results.
* **`requirements.txt`:** Lists the Python packages required for this project.

## Setting up the MCP Server

**Important:** This project assumes you have a running MCP server that provides flight data. Building an MCP server is a separate task that involves:

1.  **Choosing a Flight Data Source:** Decide which API (e.g., airline API, GDS API, aggregator API) you will use to get flight data.
2.  **Implementing the MCP Protocol:** Create a web service that can receive requests according to your defined MCP structure for flight searches.
3.  **Interacting with the Flight Data Source:** Your MCP server will need to translate the MCP requests into API calls to your chosen flight data source.
4.  **Formatting the Responses:** The MCP server will then need to format the data received from the flight data source into an MCP-compliant response to send back to the agent.

You can use web frameworks like Flask or FastAPI (in Python) to build your MCP server. The specific implementation will depend on the flight data API you choose to work with.

## Potential Enhancements

* **More Sophisticated Prompt Engineering:** Improve the prompts for Gemini to handle more complex queries and provide more nuanced responses.
* **Structured Data Handling:** If the MCP server provides structured flight data, update the agent and UI to display it in a more organized way (e.g., using tables).
* **Additional Search Parameters:** Allow users to specify more search criteria (e.g., number of passengers, preferred airlines, cabin class).
* **Error Handling and Feedback:** Implement more robust error handling and provide informative feedback to the user in case of errors or no results.
* **Advanced ADK Features:** Explore and integrate more advanced features of the ADK for managing agent state, using more complex tools, and potentially orchestrating multi-agent workflows.
* **Testing:** Add unit and integration tests to ensure the reliability of the agent and MCP client.

## Disclaimer

This project provides a basic framework for a flight search agent. You will need to configure it with your own Google Gemini API key and, crucially, set up or integrate with an MCP server that provides access to flight data. The functionality and accuracy of the agent will depend heavily on the capabilities and reliability of the MCP server and the underlying flight data source.