from local_speech import transcribe_file
from aspect_lookup import get_aspects
from write_advert import aspects_to_advert

if __name__ == '__main__':

    audio_loc = 'data/data_scientist.wav'
    text_transcriptions = transcribe_file(audio_loc)
    text = ''.join(text_transcriptions)[0]
    aspects = get_aspects(text)
    aspects_to_advert(aspects)
