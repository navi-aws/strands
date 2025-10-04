from strands import Agent
from strands.models import BedrockModel

model = BedrockModel(model_id="us.amazon.nova-pro-v1:0",
                   streaming=True)

# Create an agent with default settings
agent = Agent(model=model)

# Ask the agent a question
agent("Tell me about India in 3 sentences")