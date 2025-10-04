from strands import Agent, tool
from strands_tools import calculator,current_time
from strands.models import BedrockModel

model = BedrockModel(model_id="amazon.nova-lite-v1:0"
                   )

# Create an agent with tools 
agent = Agent(model=model, tools=[calculator, current_time])

print(agent.model.config)
# Ask the agent a question that uses the available tools
message = """
I have 2  request:

1. Calculate 3111696 / 74088
2. What is the current time in AEST?

Use your python tools to confirm that the script works before outputting it
"""

agent(message)
