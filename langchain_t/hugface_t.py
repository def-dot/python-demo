from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from transformers import BitsAndBytesConfig
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

from langchain_huggingface import HuggingFacePipeline
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline


def local_run():
    tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
    pipe = pipeline(
        "text-generation", model=model, tokenizer=tokenizer, max_new_tokens=10
    )
    hf = HuggingFacePipeline(pipeline=pipe)
    r = hf.invoke("what is golang, answer in 20 words")
    print(r)


def remote_run():
    import os
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype="float16",
        bnb_4bit_use_double_quant=True
    )


    llm = HuggingFaceEndpoint(
        repo_id="Qwen/Qwen2.5-0.5B-Instruct",
        task="text-generation",
        max_new_tokens=512,
        do_sample=False,
        repetition_penalty=1.03,  # 重复惩罚因子
        model_kwargs={"quantization_config": quantization_config}
    )
    r = llm.invoke("what is golang, answer in 20 words")
    print(r)


