from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-large-zh-v1.5")
model = AutoModel.from_pretrained("BAAI/bge-large-zh-v1.5")

inputs = tokenizer("长春市长", return_tensors="pt") 

outputs = model(**inputs)
print(outputs)

sentence_vector = outputs.pooler_output
print("句子向量形状:", sentence_vector)
