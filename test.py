from openai import OpenAI
# gets API Key from environment variable OPENAI_API_KEY
from dotenv import dotenv_values

config = dotenv_values(".env")
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key= config['OPENAI_API_KEY'],
)

completion = client.chat.completions.create(
  model="openai/gpt-3.5-turbo",
  messages=[
    {
      "role": "user",
      "content": "how to install a babylon js in node modules",
    },
  ],
)
print(completion.choices[0].message.content)