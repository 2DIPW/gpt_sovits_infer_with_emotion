from GPT_SoVITS import inference_with_emotion
import winsound
import argparse
import yaml
import os
from datetime import datetime
import soundfile as sf


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', type=str, default="text.txt",
                        help='Path of input text file, default is text.txt')
    parser.add_argument('-o', '--output', type=str, default="output/",
                        help='Path of output wav file, default is output/')
    parser.add_argument('-c', '--config', type=str, default="config.yaml",
                        help='Path of config yaml file, default is config.yaml')
    parser.add_argument('-a', '--audition', action='store_true', default=False,
                        help='Switch of audition')
    args = parser.parse_args()

    with open(args.config, 'r', encoding="utf-8") as f:
        config = yaml.safe_load(f)

    inference_with_emotion.set_gpt_model_path(config["GPT_model"])
    inference_with_emotion.set_sovits_model_path(config["SoVITS_model"])

    os.makedirs(args.output, exist_ok=True)

    with open(args.input, 'r', encoding="utf-8") as f:
        t = datetime.now().strftime('%Y%m%d-%H%M%S')
        i = 0
        for line in f:
            i += 1
            sampling_rate, audio_data = inference_with_emotion.tts(text=line, text_language="all_zh", ref_dict=config["ref_dict"],
                                                                   how_to_cut=config["how_to_cut"], top_k=config["top_k"],
                                                                   top_p=config["top_p"], temperature=config["temperature"], ref_free=False)
            output_wav_path = os.path.join(args.output, f"{t}-{str(i)}.wav")
            sf.write(output_wav_path, audio_data, sampling_rate)
            if args.audition:
                print("正在播放...")
                winsound.PlaySound(output_wav_path, winsound.SND_ASYNC)
                input("按回车键继续下一条")

