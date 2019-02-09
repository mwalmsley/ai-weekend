from local_speech import transcribe_file
from aspect_lookup import get_aspects
from write_advert import aspects_to_advert


if __name__ == '__main__':

    audio_loc = 'data/data_scientist.wav'
    # text_transcriptions = transcribe_file(audio_loc)
    # text_transcriptions = ['so I would like to hire a data scientist who actually has what it takes', ' you know so they need to understand', " that it's not just about like some fancy algorithm that gets about understanding your data knowing read comes from and being able to connect this back to real life applications", ' Set It Off']
    # print(text_transcriptions)
    # text = ''.join(text_transcriptions)[0]
    print('\n')
    print('\n')
    text = 'someone with any degree and industry experience, who creates client value'
    print(text)
    # entities = get_entities(text)
    # print(entities)
    print('\nAspects:')
    aspects = get_aspects(text)
    print(aspects)
    print('\nJob Advert... ')
    aspects_to_advert(aspects)