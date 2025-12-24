
DETECTRON2_ONNX_MODEL_TYPES = {
    "detectron2_onnx": dict(
        model_path="",
        label_map="",
        confidence_threshold=0.8,
    ),
    "detectron2_quantized": {
        "model_path": "",
        "label_map": "",
        "confidence_threshold": 0.8,
    }
}

YOLOX_MODEL_TYPES = {
    "yolox": dict(
        model_path="",
        label_map="",
    ),
    "yolox_tiny": dict(
        model_path="",
        label_map="",
    )
}


class UnstructuredDetectronONNXModel:
    pass


class UnstructuredYoloXModel:
    pass


def get_default_model_mappings():
    """default model mappings for models that are in `unstructured_inference` repo"""
    return {
        **dict.fromkeys(DETECTRON2_ONNX_MODEL_TYPES, UnstructuredDetectronONNXModel),
        **dict.fromkeys(YOLOX_MODEL_TYPES, UnstructuredYoloXModel),
    }, {**DETECTRON2_ONNX_MODEL_TYPES, **YOLOX_MODEL_TYPES}


r = get_default_model_mappings()
print(r)
