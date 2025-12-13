from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "gpt2"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

input_text = "Монгол хэлний боловсруулалтын ирээдүй бол"
inputs = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(
    inputs.input_ids,
    max_length=200,
    num_beams=5,
    no_repeat_ngram_size=2
)

print(tokenizer.decode(outputs[0]))
