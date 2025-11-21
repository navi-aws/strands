from strands import Agent
from strands_tools import use_aws, current_time
from strands.models import BedrockModel

model = BedrockModel(model_id="amazon.nova-lite-v1:0",
                   streaming=True)

# Use the detailed system prompt
system_prompt = """You are an AWS cloud assistant. You can
check my AWS account and respond to queries about resources like EC2.

Provide clear, concise responses and specify if any 
information cannot be accessed.
"""

agent = Agent(model=model,
    tools=[use_aws, current_time],
    system_prompt=system_prompt
)

if __name__ == "__main__":
    print("\n 💬 What do you want to know about your AWS Resources 💬\n")
    print("📚 🏗️  Using STRANDS built-in tool called Use-AWS. 🏗️  📚")
    print("\n                 Type 'exit' to quit 👋\n")
    print("\n Example - aws sagemaker list-domains --region us-east-1 \n")

    while True:
        try:
            user_input = input("\n> ").strip()
            
            if user_input.lower() == "exit":
               print("\n Thank you for using AWS Assistant💡! Goodbye! 👋")
               break

            # Get and display the response
            response = agent(user_input)
            print(f"\n{response}\n")
            
        except KeyboardInterrupt:
            print("\n\nExecution interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")
            print("Please try a different request.")

