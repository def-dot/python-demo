from transformers import pipeline


def text_generation():
    # 文本生成
    generator = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
    generated_text = generator("Hugging Face is a company that", max_length=50)

    print(generated_text)  # Hugging Face is a company that specializes in the development of artificial intelligence (AI) models and systems. They are known for their work on language models, particularly the BERT model, which has been used to improve natural language processing capabilities.\n\nSuppose


def sentiment_analysis():
    # 文本分类
    generator = pipeline("sentiment-analysis", model="Qwen/Qwen2.5-0.5B-Instruct")
    generated_text = generator("I love using Hugging Face!")
    print(generated_text)  # [{'label': 'LABEL_1', 'score': 0.996843695640564}]


def question_answering():
    # 问答 （基于context上下文分析，得出问题答案，Qwen不支持）
    generator = pipeline("question-answering", model="Qwen/Qwen2.5-0.5B-Instruct")
    generated_text = generator(question="what is NFC", context="NFC is a chip")
    print(generated_text)


def translation_en_to_zh():
    # 翻译
    generator = pipeline("translation_en_to_zh", model="Qwen/Qwen2.5-0.5B-Instruct")
    generated_text = generator("who are you")
    print(generated_text)


def summarization():
    # 总结
    generator = pipeline("summarization", model="Qwen/Qwen2.5-0.5B-Instruct")
    generated_text = generator("who are you")
    print(generated_text)


def ner():
    # 命名实体识别 named entity recognition
    generator = pipeline("ner", model="Qwen/Qwen2.5-0.5B-Instruct")
    generated_text = generator("tom is a stupid boy")
    print(generated_text)

ner()
