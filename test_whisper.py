import os
import openai
import sys
import whisper
_key = "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"
openai.api_key = _key
# Load your API key from an environment variable or secret management service


model = whisper.load_model("base")

# load audio and pad/trim it to fit 30 seconds
result = model.transcribe('audio/sawadee.mp3', fp16=False, language='Thai')
print(result["text"])
