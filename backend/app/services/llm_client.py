import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def ask_llm(prompt: str, model: str = "gpt-4o-mini"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "문서 기반으로 정확하게 답변하세요."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message["content"]
