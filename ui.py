# ui.py
import streamlit as st
from agent import FlightSearchAgent

# Initialize the agent
agent = FlightSearchAgent()

st.title("✈️ Flight Search Agent")

origin = st.text_input("Departure City:")
destination = st.text_input("Arrival City:")
date = st.date_input("Travel Date:")

if st.button("Search Flights"):
    if origin and destination and date:
        user_query = f"Flights from {origin} to {destination} on {date.strftime('%Y-%m-%d')}"
        with st.spinner(f"Searching flights for {origin} to {destination} on {date}..."):
            response = agent.process_user_query(user_query)
        st.subheader("Search Results:")
        st.write(response)
    else:
        st.warning("Please enter the departure city, arrival city, and travel date.")
