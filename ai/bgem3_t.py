import torch
from transformers import AutoTokenizer, AutoModel

# 选择 BGE-M3 模型名称，假设是从 huggingface 上加载
model_name = "BAAI/bge-m3"  # 假设 BGE-M3 模型已在 Hugging Face 上发布

# 加载模型和分词器
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

def generate_dense_vector(text):
    # 对输入文本进行编码
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
    
    # 通过模型获取输出
    with torch.no_grad():
        outputs = model(**inputs)
    
    # 获取最后一层的隐藏状态 (hidden states)，通常取[CLS]的位置
    last_hidden_state = outputs.last_hidden_state
    
    # 获取[CLS]的嵌入向量，通常是第一个 token 的向量
    cls_embedding = last_hidden_state[:, 0, :].squeeze().numpy()
    
    return cls_embedding

# 示例文本
text = "深度学习在自然语言处理中的应用"
dense_vector = generate_dense_vector(text)
print("生成的密集向量：", dense_vector)
