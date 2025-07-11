from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import Tool
from datetime import datetime

# Save tool
def save_to_txt(data: str, filename: str = "itinerary.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Travel Itinerary ---\nTimestamp: {timestamp}\n\n{data}\n\n"
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)
    
    return f"Data successfully saved to {filename}"

save_tool = Tool(
    name="save_itinerary",
    func=save_to_txt,
    description="Saves the travel itinerary to a text file.",
)

# Flight search tool (using DuckDuckGo)
flight_search = DuckDuckGoSearchRun()
flight_search_tool = Tool(
    name="flight_search",
    func=lambda x: flight_search.run(f"flights to {x}"),
    description="Search for flights to a destination.",
)

# Hotel search tool (using DuckDuckGo)
hotel_search = DuckDuckGoSearchRun()
hotel_search_tool = Tool(
    name="hotel_search",
    func=lambda x: hotel_search.run(f"hotels in {x}"),
    description="Search for hotels in a destination.",
)

# Wikipedia tool for attractions
api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki_tool = WikipediaQueryRun(
    name="attraction_search",
    api_wrapper=api_wrapper,
    description="Search Wikipedia for top attractions in a destination.",
)