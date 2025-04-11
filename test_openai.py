import openai

# Set your OpenAI API key
openai.api_key = "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"  
try:
    # Make a call to the OpenAI chat completion API using the correct method
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # You can replace this with the appropriate model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello! How can I use the new API?"}
        ]
    )
    
    # Output the response
    print(response['choices'][0]['message']['content'])
    
except openai.error.AuthenticationError as e:
    print(f"Authentication error: {e}")
except openai.error.RateLimitError as e:
    print(f"Rate limit exceeded: {e}")
except openai.error.OpenAIError as e:
    print(f"An OpenAI error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

