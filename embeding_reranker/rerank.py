def flagembedding_t():
    from FlagEmbedding import FlagAutoReranker
    reranker = FlagAutoReranker.from_finetuned('BAAI/bge-reranker-large',
                                            query_max_length=256,
                                            passage_max_length=512,
                                            use_fp16=True,
                                            devices=['cpu']) # Setting use_fp16 to True speeds up computation with a slight performance degradation
    score = reranker.compute_score(['query', 'passage'])
    print(score) # -1.5263671875

    # You can map the scores into 0-1 by set "normalize=True", which will apply sigmoid function to the score
    score = reranker.compute_score(['query', 'passage'], normalize=True)
    print(score) # 0.1785258315203034

    scores = reranker.compute_score([['what is panda?', 'hi'], ['what is panda?', 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.']])
    print(scores) # [-5.60546875, 5.76171875]

    # You can map the scores into 0-1 by set "normalize=True", which will apply sigmoid function to the score
    scores = reranker.compute_score([['what is panda?', 'what panda eat?'], ['what is panda?', 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.']], normalize=True)
    print(scores) # [0.0036642203307843528, 0.9968641641227171]


def transform_t():
    import torch
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained('BAAI/bge-reranker-large')
    model = AutoModelForSequenceClassification.from_pretrained('BAAI/bge-reranker-large')
    model.eval()

    pairs = [['what is panda?', 'hi'], ['what is panda?', 'The giant panda (Ailuropoda melanoleuca), sometimes called a panda bear or simply panda, is a bear species endemic to China.']]
    with torch.no_grad():
        inputs = tokenizer(pairs, padding=True, truncation=True, return_tensors='pt', max_length=512)
        scores = model(**inputs, return_dict=True).logits.view(-1, ).float()
        print(scores)



if __name__ == "__main__":
    transform_t()