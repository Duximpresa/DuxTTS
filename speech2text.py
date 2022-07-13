import azure.cognitiveservices.speech as speechsdk


# 输入的参数

language_list = ["zh-CN", "en-US"]
filename = "kepu-02.wav" # 文件路径
language = language_list[0]

def from_file(filename, language):
    speech_config = speechsdk.SpeechConfig(subscription="8b7335e4c1cf4708a48453f878a6c802", region="southeastasia")
    audio_input = speechsdk.AudioConfig(filename=filename)
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_input)

    speech_config.speech_recognition_language=language

    result = speech_recognizer.recognize_once_async().get()
    print(result.text)
    return result.text
# print(language)
resultText = from_file(filename, language)

with open("b.txt", mode="w", encoding="utf-8") as f:
    f.write(resultText)
    f.close


