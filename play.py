from transformers import pipeline

prompt = "Write an email about an alpaca that likes flan"
model = pipeline(model="declare-lab/flan-alpaca-base")
res = model(prompt, max_length=128, do_sample=True)
print(res[0]['generated_text'])
