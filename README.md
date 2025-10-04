# Strands AI Agent Exercises

This project contains a collection of five Python exercises demonstrating the capabilities of the Strands AI framework with Amazon Bedrock's Nova Pro model. Each exercise showcases different aspects of building intelligent agents with various tools and system prompts.

## Prerequisites

- Python 3.10 or higher
- AWS account with Bedrock access
- Proper AWS credentials configured
- Required Python packages (see requirements.txt)

## Installation

```bash
pip install -r requirements.txt
```

## Exercise Descriptions

### Exercise 1: Basic Agent Interaction
**File:** `exercise-1.py`

Make a simple query without any additional tools or complex system prompts. It's perfect for understanding the core mechanics of agent initialization and basic conversational capabilities.

### Exercise 2: Weather Forecasting Agent
**File:** `exercise-2.py`

The agent is equipped with the `http_request` tool and a specialized system prompt that enables it to interact with the National Weather Service API. Users can request weather forecasts for cities across the USA.

### Exercise 3: Mathematical and Time Operations
**File:** `exercise-3.py`

This exercise showcases the agent's ability to perform precise calculations and time-related queries using built-in tools. 

### Exercise 4: AWS Cloud Resource Assistant
**File:** `exercise-4.py`

This advanced exercise creates a cloud infrastructure assistant capable of interacting with AWS services through the `use_aws` tool. 

### Exercise 5: Dog Research Specialist
**File:** `exercise-5.py`

The agent is configured with access to the `http_request` tool, enabling it to search Wikipedia and other web sources for information. This showcase how agents can perform targeted research and present findings in a structured, bullet-point format.

## Key Features Demonstrated

- Model Integration
- Tool Integration
- System Prompts
- Interactive Interfaces- Command-line interfaces with proper error handling
- Real-world Applications- Weather forecasting, cloud management, research, and calculations
