import openai

openai.api_key =settings.OPENAI_API_KEY

def query_llm(prompt, contract_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a legal document analyst."},
            {"role": "user", "content": prompt + "\n\n" + contract_text}
        ]
    )
    return response.choices[0].message.content.strip()

