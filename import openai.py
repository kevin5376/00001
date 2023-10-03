import openai

from dotenv import dotenv_values

config = dotenv_values(".env")

openai.api_key = config['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'] # Fill in your own key


def generate_blog(paragraph_topic):
  response = openai.Completion.create(
    model = 'text-davinci-002',
    prompt = 'Write a paragraph about the following topic. ' + paragraph_topic,
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response.choices[0].text

  return retrieve_blog