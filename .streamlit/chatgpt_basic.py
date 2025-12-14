from openai import OpenAI
# Initialize the OpenAI client with your API key
client = OpenAI(api_key='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')
# Make a simple API call
completion = client.chat.completions.create(
model="gpt-4o",
messages=[
{"role": "system", "content": "You are a helpful assistant."},
{"role": "user", "content": "Hello! What is AI?"}
]
)
# Print the response
print(completion.choices[0].message.content)