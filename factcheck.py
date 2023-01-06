import openai

openai.api_key = "YOUR_API_KEY"

# Set up the GPT-3 model
model_engine = "text-davinci-002"
model_prompt = "Is the statement 'The earth is flat' true or false?"

# Generate text based on the prompt
completions = openai.Completion.create(
    engine=model_engine,
    prompt=model_prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Get the generated text
generated_text = completions.choices[0].text

# Check if the generated text contains any indication that the statement is false
if "false" in generated_text.lower():
  print("The statement is false.")
else:
  print("The statement is true or unclear.")
