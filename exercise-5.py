from strands import Agent
from strands_tools import http_request

# Create a basic agent with a specialized system prompt
dog_breed_helper = Agent(
    system_prompt="""You are a dog breed expert.     
    Your goal is to help pet parents make an informed decision about their choice in a dog.
    in bullet points. No explanation required.
    """,
    tools=[http_request]
)

query = """
Answer this question:
Search wikipedia for the top 5 most popular dog breeds of 2024.
"""
# Run the agent with the query
response = dog_breed_helper(query)

