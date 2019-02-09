# import six
import os

from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'zoobot-caf3c0a19fac.json'


CLIENT = language.LanguageServiceClient()


def get_entities(text):
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)
    return CLIENT.analyze_entities(document).entities

if __name__ == '__main__':

    text = 'I would like someone with six years of Java experience'
    entities = get_entities(text)

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
        print('=' * 20)
        print(u'{:<16}: {}'.format('name', entity.name))
        print(u'{:<16}: {}'.format('type', entity_type.name))
        print(u'{:<16}: {}'.format('salience', entity.salience))
        print(u'{:<16}: {}'.format('wikipedia_url',
            entity.metadata.get('wikipedia_url', '-')))
        print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))