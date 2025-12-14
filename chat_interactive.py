import os
from openai import OpenAI

# Initialize client with API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

client = OpenAI(api_key=api_key)

# Initialize conversation history
messages = [
    {"role": "system", "content": "You are a helpful cybersecurity assistant for a multi-domain intelligence platform."}
]

print("=" * 60)
print("ChatGPT Console Chat (type 'quit' to exit)")
print("=" * 60)

while True:
    # Get user input
    user_input = input("\nYou: ").strip()
    
    # Exit condition
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    
    # Skip empty input
    if not user_input:
        print("Please enter a message.")
        continue
    
    # Add user message to history
    messages.append({"role": "user", "content": user_input})
    
    try:
        # Get AI response
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=messages
        )
        
        # Extract response
        assistant_message = completion.choices[0].message.content
        
        # Add assistant response to history
        messages.append({"role": "assistant", "content": assistant_message})
        
        # Display response
        print(f"\nAI: {assistant_message}")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")
        # Remove user message if API call failed
        messages.pop()