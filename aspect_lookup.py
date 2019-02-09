from collections import namedtuple
import itertools

class Aspect():

    def __init__(self, key, representation, keywords):
        self.key = key
        self.representation = representation
        self.keywords = keywords


    def __repr__(self):
        return 'Aspect with key: {}'.format(self.key)


class Skill(Aspect):
    pass


class Experience(Aspect):
    pass


class Quality(Aspect):
    pass


class Education(Aspect):
    pass


qualities = [
    Quality(
        key='client_driven',
        representation='Driven to create client value',
        keywords=['client driven', 'client value', 'business value', 'value for clients']
    ),
    Quality(
        key='responsible',
        representation='Highly responsible',
        keywords=['highly responsible, responsible', 'dependable', 'reliable']
    )
]

skills = [
    Skill(
        key='oral_communication',
        representation='Strong presentation skills. Able to communicate complex information clearly',
        keywords=['speaker', 'presentation', 'talk']
    )
]


experiences = [
    Experience(
        key='industry',
        representation='Experience in industry',
        keywords=['industry experience', 'worked in industry']
    )
]


education = [
    Education(
        key='any_degree',
        representation='University degree in any subject',
        keywords=['any degree', 'university degree']
    )
]

# really ugly
all_aspects = []
all_aspects.extend(qualities)
all_aspects.extend(education)
all_aspects.extend(skills)

def get_aspects(text):
    aspects = []
    for aspect in all_aspects:
        for keyword in aspect.keywords:
            if keyword in text:
                aspects.append(aspect)
    return aspects
