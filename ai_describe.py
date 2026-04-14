from openai import OpenAI
import base64

client = OpenAI(api_key="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")

def describe_image(path):
    with open(path, "rb") as f:
        image_bytes = f.read()

    image_base64 = base64.b64encode(image_bytes).decode("utf-8")

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[{
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Describe this image clearly for a blind person. First give a short summary, then explain the key details, important parts, and relationships in a natural spoken way."
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{image_base64}"
                }
            ]
        }]
    )

    return response.output_text
