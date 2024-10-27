Read this in [Chinese](./README_ch.md)

Thank you, cydxg, for quantizing this model: https://huggingface.co/cydxg/glm-4-voice-9b-int4

# GLM-4-Voice
GLM-4-Voice is an end-to-end voice model launched by Zhipu AI. GLM-4-Voice can directly understand and generate Chinese and English speech, engage in real-time voice conversations, and change attributes such as emotion, intonation, speech rate, and dialect based on user instructions.

## Model Architecture

![Model Architecture](./resources/architecture.jpeg)
We provide the three components of GLM-4-Voice:
* GLM-4-Voice-Tokenizer: Trained by adding vector quantization to the encoder part of [Whisper](https://github.com/openai/whisper), converting continuous speech input into discrete tokens. Each second of audio is converted into 12.5 discrete tokens.
* GLM-4-Voice-9B: Pre-trained and aligned on speech modality based on [GLM-4-9B](https://github.com/THUDM/GLM-4), enabling understanding and generation of discretized speech.
* GLM-4-Voice-Decoder: A speech decoder supporting streaming inference, retrained based on [CosyVoice](https://github.com/FunAudioLLM/CosyVoice), converting discrete speech tokens into continuous speech output. Generation can start with as few as 10 audio tokens, reducing conversation latency.

A more detailed technical report will be published later.

## Model List
|         Model         | Type |      Download      |
|:---------------------:| :---: |:------------------:|
| GLM-4-Voice-Tokenizer | Speech Tokenizer | [🤗 Huggingface](https://huggingface.co/THUDM/glm-4-voice-tokenizer) |
|    GLM-4-Voice-9B     | Chat Model |  [🤗 Huggingface](https://huggingface.co/cydxg/glm-4-voice-9b-int4)
| GLM-4-Voice-Decoder   | Speech Decoder |  [🤗 Huggingface](https://huggingface.co/THUDM/glm-4-voice-decoder)

## Usage
We provide a Web Demo that can be launched directly. Users can input speech or text, and the model will respond with both speech and text.

![](resources/web_demo.png)

### Preparation
First, download the repository
```shell
git clone --recurse-submodules https://github.com/THUDM/GLM-4-Voice
cd GLM-4-Voice
```
Then, install the dependencies.
```shell
pip install -r requirements.txt
```
Since the Decoder model does not support initialization via `transformers`, the checkpoint needs to be downloaded separately.

```shell
# Git model download, please ensure git-lfs is installed
git clone https://huggingface.co/THUDM/glm-4-voice-decoder
```

### Launch Web Demo
First, start the model service
```shell
python model_server.py --model-path glm-4-voice-9b
```

Then, start the web service
```shell
python web_demo.py
```
You can then access the web demo at http://127.0.0.1:8888.

### Known Issues
* Gradio’s streaming audio playback can be unstable. The audio quality will be higher when clicking on the audio in the dialogue box after generation is complete.

## Examples
We provide some dialogue cases for GLM-4-Voice, including emotion control, speech rate alteration, dialect generation, etc. (The examples are in English.)

* Use a gentle voice to guide me to relax


https://github.com/user-attachments/assets/5f14862c-8c52-471e-ac7c-0c3d93f246b3


* Use an excited voice to commentate a football match



https://github.com/user-attachments/assets/c79e9489-fd8d-406a-8437-c1a5fe0de472



* Tell a ghost story with a mournful voice



https://github.com/user-attachments/assets/1f4b332b-af59-43cd-b65f-bb77ba1d68c5



* Introduce how cold winter is with a Northeastern dialect



https://github.com/user-attachments/assets/f4833a26-ddda-4b71-a510-dab1599a0cfc



* Cry about your lost cat



https://github.com/user-attachments/assets/6a3ee554-73c9-4919-a8a9-d77f31e18744





## Acknowledge
Some code in this project is from:
* [CosyVoice](https://github.com/FunAudioLLM/CosyVoice)
* [transformers](https://github.com/huggingface/transformers)
* [GLM-4](https://github.com/THUDM/GLM-4)
