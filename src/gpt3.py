

import os
import openai

openai.organization = "org-KwgygO2WQTwpBaK8iwQlnTiq"
openai.api_key = "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"
models = openai.Model.list()

async def gpt3(query):
        completion = openai.Completion.create(
            model="text-davinci-002",
            prompt=query,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0)

        return completion.choices[0]["text"]
