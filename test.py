from litellm import completion
import os

os.environ['GROQ_API_KEY'] ="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"
response = completion(
    model="groq/moonshotai/kimi-k2-instruct-0905", 
    messages=[
       {"role": "user", "content": "hello from litellm"}
   ],
)
print(response.choices[0].message.content)