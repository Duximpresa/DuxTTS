import azure.cognitiveservices.speech as speechsdk
import os

speech_config = speechsdk.SpeechConfig(subscription="8b7335e4c1cf4708a48453f878a6c802", region="southeastasia")

# Note: if only language is set, the default voice of that language is chosen.
speech_config.speech_synthesis_language = "zh-CN"  # e.g. "de-DE"
# The voice setting will overwrite language setting.
# The voice setting will not overwrite the voice element in input SSML.

# zh-CN-XiaoxiaoNeural
voice_name = ["zh-CN-XiaoxiaoNeural",
              "zh-CN-XiaochenNeural"]
speech_config.speech_synthesis_voice_name = voice_name[1]
speech_config.set_speech_synthesis_output_format(speechsdk.SpeechSynthesisOutputFormat["Riff24Khz16BitMonoPcm"])
audio_config = speechsdk.AudioConfig(filename="test.wav")

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

with open("test.txt", mode="r", encoding="utf-8") as f:
    speechText = f.read()
    print(speechText)
    synthesizer.speak_text_async(f"{speechText}")
# synthesizer.speak_text_async(f"{speechText}")
