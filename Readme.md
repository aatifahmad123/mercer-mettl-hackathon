MCP-Based Multi-Agent Travel Planner
Overview
A minimal prototype for a hackathon, demonstrating a multi-agent travel planner using LangChain and Google Gemini. Agents handle flight search, hotel search, and attraction recommendations, with results saved to itinerary.txt. MCP is simulated via sequential tool calls.
Setup

Prerequisites:
Python 3.10+
Install dependencies: pip install langchain langchain-google-genai python-dotenv pydantic langchain-community


Environment:
Create a .env file with: GOOGLE_API_KEY=your_api_key_here
Obtain a Google Gemini API key from Google Cloud.


Run:
Execute python main.py
Enter a destination (e.g., "Paris") and dates (e.g., "2025-08-01 to 2025-08-03").
View the travel plan in the console and saved to itinerary.txt.



Usage

Input destination and dates when prompted.
The system fetches flight, hotel, and attraction data, then generates and saves an itinerary.
Example output in itinerary.txt:--- Travel Itinerary ---
Timestamp: 2025-07-11 12:25:00
Destination: Paris
Dates: 2025-08-01 to 2025-08-03
Flights: Flights to Paris available via Kayak, Expedia...
Hotels: Hotels in Paris include Hilton, Marriott...
Attractions: Eiffel Tower, Louvre Museum...
Itinerary: Day 1: Arrive, check into hotel, visit Eiffel Tower...



Notes

Uses DuckDuckGo for flights and hotels, Wikipedia for attractions.
Limited by time; no full MCP server or travel APIs (e.g., Google Flights).
Future enhancements: Add real travel APIs, Streamlit UI, and full MCP integration.

Demo
Run python main.py, enter "Paris" and "2025-08-01 to 2025-08-03", and check itinerary.txt for the plan.