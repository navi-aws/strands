from strands import Agent
from ddgs import DDGS
from strands.models import BedrockModel

model = BedrockModel(model_id="amazon.nova-lite-v1:0"
                   )

# Create a web search tool
@tool
def websearch(keywords: str, region: str = "us-en", max_results: int = 1) -> str:
    try:
        results = DDGS().text(keywords, region=region, max_results=max_results)
        return results if results else "No results found."
    except Exception as e:
        return f"Error: {e}"
        # Create a basic agent with a specialized system prompt
dog_info = Agent(model=model,
    system_prompt="""You are a dog expert.     
    Your goal is to help get information about dogs in bullet points. No explanation required.
    """,
    tools=[websearch]
)

query = """
Answer this question:
Search wikipedia for the top 5 most popular dog breeds of 2024.
"""
# Run the agent with the query
response = dog_info(query)
