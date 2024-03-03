# 基于中文文本情绪分析自动切换参考音频的 GPT-SoVITS 推理 Demo
## 🚩 简介
基于中文文本情绪分析模型 [StructBERT](https://modelscope.cn/models/iic/nlp_structbert_emotion-classification_chinese-base/summary) 对输入的文本进行情绪八分类（一般、惊讶、高兴、悲伤、喜好、厌恶、愤怒、恐惧）并自动切换预先设置的对应的参考音频，以实现更加富有情感的推理。

基于 [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) 修改，仅保留推理功能。提供了一个可被调用的 `inference_with_emotion.py` 脚本，和一个演示脚本`infer_demo.py`

此项目为一个思路的展示，实际上分类效果很差，仅供学习与交流，抛砖引玉，并非为生产环境准备。

## 📥 部署
### 安装其他依赖
在满足 [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) 所需依赖的基础上，还需安装 modelscope
```shell
pip install modelscope
```
### 配置预训练模型
与 [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) 中相同，需要将预训练模型放置于 `GPT_SoVITS/pretrained_models` 目录

## 🗝 使用方法
### 配置模型
在配置文件 `config.yaml` 中指定 GPT 和 SoVITS 的模型地址和参数。
```yaml
GPT_model: "model/paimeng2-e10.ckpt"
SoVITS_model: "model/paimeng2_e25_s36350.pth"
how_to_cut: 0  # 0：不切 1：凑四句一切 2：凑50字一切 3：按中文句号。切 4：按英文句号.切 5：按标点符号切
top_k: 20
top_p: 0.6
temperature: 0.6
```
### 配置参考音频
对于每种情绪，均需在配置文件 `config.yaml` 中指定文件位置和参考文本。
```yaml
ref_dict:
  一般:
    Path: "ref_audio/normal.wav"
    Text: "既然罗莎莉亚说足迹上有元素力，用元素视野应该能很清楚地看到吧。"
  惊讶:
    Path: "ref_audio/surprised.wav"
    Text: "这个声音是…一斗！你怎么在这里啊？"
  高兴:
    Path: "ref_audio/excited.wav"
    Text: "好耶！《特尔克西的奇幻历险》出发咯！"
  悲伤:
    Path: "ref_audio/sad.wav"
    Text: "呜…别这么伤心…我们会找到他们的！往好的一面想吧！"
  喜好:
    Path: "ref_audio/like.wav"
    Text: "豪华礼物！听、听上去就很值钱！"
  厌恶:
    Path: "ref_audio/dislike.wav"
    Text: "说了半天，这不还是面子的问题吗！"
  愤怒:
    Path: "ref_audio/angry.wav"
    Text: "呜哇好生气啊！不要把我跟一斗相提并论！"
  恐惧:
    Path: "ref_audio/fear.wav"
    Text: "我还以为见不到你了！你突然就消失了呀！"
```
### 准备待合成的文本列表
- 在`text.txt`中填入待合成的文本，一行一条
### 运行语音合成
- 使用`infer_demo.py`
    ```shell
    python infer_demo.py -a
    ```
    可指定的参数:
    - `-i` | `--input`: 待合成的文本文件。默认值：`text.txt`
    - `-o` | `--output`: 合成的音频文件的路径。默认值：`/output`
    - `-c` | `--config`: 配置文件。默认值：`config.yaml`
    - `-a` | `--audition`: 是否试听。


## ⚖ 开源协议
本项目基于 [GNU General Public License v3.0](https://github.com/2DIPW/audio_dataset_vpr/blob/master/LICENSE) 开源

*世界因开源更精彩*
## 📃 参考文献
```
@article{wang2019structbert,
  title={Structbert: Incorporating language structures into pre-training for deep language understanding},
  author={Wang, Wei and Bi, Bin and Yan, Ming and Wu, Chen and Bao, Zuyi and Xia, Jiangnan and Peng, Liwei and Si, Luo},
  journal={arXiv preprint arXiv:1908.04577},
  year={2019}
}
```