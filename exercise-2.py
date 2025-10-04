from strands import Agent
from strands_tools import http_request
from strands.models import BedrockModel

model = BedrockModel(model_id="amazon.nova-lite-v1:0",
                   streaming=True)

WEATHER_SYSTEM_PROMPT = """You are a weather assistant with HTTP capabilities. You can:
1. Make HTTP requests to the National Weather Service API
2. Process and display weather forecast data


When displaying responses:
- Answer about weather in 1 line in a human-readable way
- Handle errors appropriately

"""  

agent = Agent(model=model,
    tools=[http_request],
    system_prompt=WEATHER_SYSTEM_PROMPT
)


if __name__ == "__main__":
    print("\n             Weather Forecaster Strands Agent\n") 
    print ("            🌦️  🤍 ☁️  🌿 🍃 ✨️ ⛈️  🫧  🌤️  🌧️  ☀️\n")
    print("  ☀️  I can get weather forecasts for cities in USA ☀️ ")
    print("     ☀️  I use the National Weather Service API ☀️")
    print("\n            Type 'exit' - to say Goodbye 👋")
   

    # Interactive loop
    while True:
        try:
            user_input = input("\n> ")

            if user_input.lower() == "exit":
                print("\nGoodbye! 👋")
                break

            response = agent(user_input)

            print(str(response))
                        
        except KeyboardInterrupt:
            print("\n\nExecution interrupted. Exiting...")
            break
        except Exception as e:
            print(f"\nAn error occurred: {str(e)}")

            print("Please try a different request.")

