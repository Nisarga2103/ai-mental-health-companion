from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration

# Load model & tokenizer once
model_name = "facebook/blenderbot-400M-distill"
tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
model = BlenderbotForConditionalGeneration.from_pretrained(model_name)

def generate_response(user_input):
    # Encode input
    inputs = tokenizer([user_input], return_tensors="pt")

    # Generate output with constraints
    reply_ids = model.generate(
        **inputs,
        max_length=60,
        num_beams=3,
        early_stopping=True
    )

    # Decode response
    response = tokenizer.batch_decode(reply_ids, skip_special_tokens=True)[0]
    return response
