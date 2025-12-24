from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("BAAI/bge-large-zh-v1.5")
text = "长春市长"
r = tokenizer.tokenize(text)  # 查看分词
print(r)  # ['长', '春', '市', '长', '春', '节', '致', '辞']
r = tokenizer.convert_tokens_to_ids(r)  # 每个token对应的ID
print(r)  # [7270, 3217, 2356, 7270, 3217, 5688, 5636, 6791]