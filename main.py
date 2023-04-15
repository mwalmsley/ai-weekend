from aspect_lookup import get_aspects, all_aspects_are_filled
from write_advert import aspects_to_advert
from streaming_speech import aspects_from_stream
import sounddevice

from utils import bot_color, noalsaerr

if __name__ == '__main__':
    with noalsaerr():  # works around an error message that distracts from the demo

        welcome_message = bot_color('\n\n***  Hello! Please describe your ideal candidate*** \n')
        aspects = aspects_from_stream(welcome_message)  # find job advert aspects in the audio stream (live)

        if not all_aspects_are_filled(aspects):  # did the speaker miss a job advert section? If so...
            prompt = bot_color("\n***I didn't catch you mentioning experience. Anything you'd like to add?***\n")
            aspects.extend(aspects_from_stream(prompt))  # ask them if they'd like anything in the missing section

        aspects_to_advert(aspects)  # print a nicely worded job advert, based on what the speaker asked for
