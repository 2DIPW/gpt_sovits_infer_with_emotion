from GPT_SoVITS.inference_main import change_gpt_weights, change_sovits_weights, get_tts_wav
from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks

semantic_cls = pipeline(Tasks.text_classification, 'damo/nlp_structbert_emotion-classification_chinese-tiny', model_revision='v1.0.0')


def _analyze_emotion(text, min_confidence=0.5):
    result = semantic_cls(input=text)
    scores = result["scores"]
    labels = result["labels"]
    max_score = max(scores)
    if max_score < min_confidence:
        emotion = "一般"
    else:
        emotion = labels[scores.index(max_score)]
    print(f"原文：{text}\n情绪得分：{result}\n情绪分析结果：{emotion}")
    return emotion


def set_gpt_model_path(path):
    change_gpt_weights(gpt_path=path)


def set_sovits_model_path(path):
    change_sovits_weights(sovits_path=path)


def tts(text, text_language, ref_dict, how_to_cut=0, top_k=20, top_p=0.6, temperature=0.6, ref_free=False):
    # how_to_cut 0：不切 1：凑四句一切 2：凑50字一切 3：按中文句号。切 4：按英文句号.切 5：按标点符号切
    emotion = _analyze_emotion(text)
    ref_audio_path = ref_dict[emotion]["Path"]
    prompt_text = ref_dict[emotion]["Text"]

    synthesis_result = get_tts_wav(ref_wav_path=ref_audio_path,
                                   prompt_text=prompt_text,
                                   prompt_language=text_language,
                                   text=text,
                                   text_language="all_zh",
                                   how_to_cut=how_to_cut,
                                   top_k=top_k,
                                   top_p=top_p,
                                   temperature=temperature,
                                   ref_free=ref_free)


    return next(synthesis_result)




