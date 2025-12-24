"""
分词
"""

def tiktoken_t():
    """
    [359, 32898, 24694]
    un
    belie
    vable
    """
    import tiktoken
    text = "unbelievable"
    encoder = tiktoken.encoding_for_model("gpt-4")
    tokens = encoder.encode(text)
    print(tokens)
    for i in tokens:
        print(encoder.decode([i]))
 


def jieba_t():
    import jieba
    text = "长春市长春节致辞"
    words = jieba.cut(text)
    print(list(words))


def transformers_t():
    from transformers import AutoTokenizer

    # 使用多语言BERT分词器
    tokenizer = AutoTokenizer.from_pretrained("bert-base-multilingual-cased")

    text = "unbelievable"
    tokens = tokenizer.tokenize(text)
    print(tokens)
    # decoded = tokenizer.decode(tokenizer.encode(text))
    # print(decoded)  # 完美还原


if __name__ == "__main__":
    # tiktoken_t()
    # jieba_t()
    transformers_t()