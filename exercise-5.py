from strands import Agent
from strands_tools import http_request
from strands.models import BedrockModel

model = BedrockModel(model_id="amazon.nova-lite-v1:0"
                   )

# Create a basic agent with a specialized system prompt
dog_info = Agent(model=model,
    system_prompt="""You are a dog expert.     
    Your goal is to help get information about dogs in bullet points. No explanation required.
    """,
    tools=[http_request]
)

query = """
Answer this question:
Search wikipedia for the top 5 most popular dog breeds of 2024.
"""
# Run the agent with the query
response = dog_info(query)

