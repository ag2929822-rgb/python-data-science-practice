from openai import OpenAI
client = OpenAI(
    api_key ="your-api-key-here",
)

from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are virtual assitant name Jarvis skilled general task like alexa and google cloud."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
