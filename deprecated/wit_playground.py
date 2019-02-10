import json
import time
from collections import namedtuple

import requests
from wit import Wit

# to authenticate (do not share)
ACCESS_TOKEN = '2R6BYRIRG6EMLR2MH2FZLFVMBRLYCMDW'

# training examples have these fields
Example = namedtuple('Example', ['text', 'entity_value'])


def make_validation_json(text, entity_value):
    return json.dumps([
        {
            "text": text,
            "entities": [
                {"entity": "intent", "value": entity_value}
            ]
        }])


def train_on_examples(examples):
    for example in examples:
        data = make_validation_json(**example._asdict())
        response = requests.post(
            url='https://api.wit.ai/samples?v=20190208',
            data=data,
            headers= {
                'Authorization': 'Bearer {}'.format(ACCESS_TOKEN),
                'Content-Type': 'application/json'}
        )


if __name__ == '__main__':

    # train model on these examples
    # will be ignored if already provided
    examples = [
        Example(text='How old is your husband?', entity_value='senior-sexism'),
        Example(text='What does your husband do?', entity_value='senior-sexism')
    ]

    train_on_examples(examples)
    # training is not immediate, need to keep an eye on this


    # get a classification back
    message = "What is your husband's job?"

    # 1) with python sdk access
    client = Wit(ACCESS_TOKEN)
    response = client.message(message)
    print(response)

    # 2) with API access
    response = requests.get(
        headers={'Authorization': 'Bearer {}'.format(ACCESS_TOKEN)},
        url='https://api.wit.ai/message?v=20190208&q={}'.format(message)
    )
    print(dict(response.json()))
