import io
import os

from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'zoobot-caf3c0a19fac.json'


def transcribe_file(speech_file):
    """Transcribe the given audio file."""
    client = speech.SpeechClient()

    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code='en-US')

    response = client.recognize(config, audio)

    # The first alternative is the most likely one for this portion.
    return [result.alternatives[0].transcript for result in response.results]


if __name__ == '__main__':
    speech_file = 'data/interview.wav'
    transcribe_file(speech_file)
