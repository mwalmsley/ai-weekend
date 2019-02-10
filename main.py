from local_speech import transcribe_file
from aspect_lookup import get_aspects, all_aspects_are_filled
from write_advert import aspects_to_advert
from streaming_speech import aspects_from_stream


if __name__ == '__main__':

    welcome_message = '\n\nHello! Please describe your ideal candidate'
    aspects = aspects_from_stream(welcome_message)
    if not all_aspects_are_filled(aspects):
        prompt = "I didn't catch you mentioning experience. Anything you'd like to add?"
        aspects.extend(aspects_from_stream(prompt))
    aspects_to_advert(aspects)
