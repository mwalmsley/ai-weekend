from aspect_lookup import get_aspects, all_aspects_are_filled
from write_advert import aspects_to_advert
from streaming_speech import aspects_from_stream
import sounddevice

from ctypes import *
from contextlib import contextmanager
import pyaudio

from utils import bot_color


ERROR_HANDLER_FUNC = CFUNCTYPE(None, c_char_p, c_int, c_char_p, c_int, c_char_p)

def py_error_handler(filename, line, function, err, fmt):
    pass

c_error_handler = ERROR_HANDLER_FUNC(py_error_handler)

@contextmanager
def noalsaerr():
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)
    yield
    asound.snd_lib_error_set_handler(None)


if __name__ == '__main__':
    with noalsaerr():
        welcome_message = bot_color('\n\n***  Hello! Please describe your ideal candidate*** \n')
        aspects = aspects_from_stream(welcome_message)
        if not all_aspects_are_filled(aspects):
            prompt = bot_color("\n***I didn't catch you mentioning experience. Anything you'd like to add?***\n")
            aspects.extend(aspects_from_stream(prompt))
        aspects_to_advert(aspects)
