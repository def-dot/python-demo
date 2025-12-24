import torch
from transformers import AutoModel

# 加载BGE模型
model = AutoModel.from_pretrained("BAAI/bge-large-zh-v1.5")

# 查看所有参数名称
print("模型参数列表:")
for name, param in model.named_parameters():
    if "query" in name.lower():
        print(f"{name}: {param.shape}")

# 直接访问W_Q权重
try:
    # 不同模型结构可能路径不同
    W_Q = model.encoder.layer[0].attention.self.query.weight
    print(f"W_Q形状: {W_Q.shape}")  # 通常是 [768, 768] 或 [768, 64]
    print(f"W_Q前5个参数: {W_Q[0, :5]}")  # 查看部分参数值
except AttributeError:
    print("模型结构不同，需要调整路径")