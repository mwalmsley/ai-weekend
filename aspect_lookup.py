# word bank to look for keywords

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

class Title(Aspect):
    pass


qualities = [
    Quality(
        key='client_driven',
        representation='Driven to create client value',
        keywords=['client driven', 'client value', 'business value', 'value for clients', 'drive clients', 'clients']
    ),
    Quality(
        key='responsible',
        representation='Highly responsible',
        keywords=['highly responsible, responsible', 'dependable', 'reliable', 'rely on']
    ),
    Quality(
        key='high-paced',
        representation='Enjoys working in a high-paced environment',
        keywords=['paced', 'high-paced', 'fast', 'quick', 'witted']
    ),
    Quality(
        key='creative',
        representation='Able to develop creative and intelligent solutions',
        keywords=['creative']
    ),
    Quality(
        key='adaptable',
        representation='Adaptable',
        keywords=['adaptable', 'adapt', 'can adjust', 'flexible', 'different areas']
    )
]

skills = [
    Skill(
        key='oral_communication',
        representation='Strong presentation skills. Able to communicate complex information clearly',
        keywords=['speaker', 'presentation', 'talk', 'talking']
    ),
    Skill(
        key='python-desirable',
        representation='Exposure to Python is helpful, but not required',
        keywords=['python']
    )
]


experiences = [
    Experience(
        key='industry',
        representation='Worked in industry',
        keywords=['industry experience', 'worked in industry', 'industry insider']
    )
]


educations = [
    Education(
        key='any_degree',
        representation='University degree in any subject',
        keywords=['any degree', 'university degree']
    ),
    Education(
        key='certified_accountant',
        representation='Certified Public Accountant (CPA)',
        keywords=['accountant', 'certified accountant', 'certified']
    )
]

titles = [
    Title(
        key='strategist',
        representation='Strategist',
        keywords=['strategist'])
]

# really ugly
all_aspects = []
all_aspects.extend(qualities)
all_aspects.extend(educations)
all_aspects.extend(experiences)
all_aspects.extend(skills)
all_aspects.extend(titles)

def get_aspects(text):
    aspects = []
    for aspect in all_aspects:
        for keyword in aspect.keywords:
            if keyword in text:
                aspects.append(aspect)
    return aspects


def all_aspects_are_filled(aspects):
    skills = [aspect for aspect in aspects if isinstance(aspect, Skill)]
    experience = [aspect for aspect in aspects if isinstance(aspect, Experience)]
    qualities = [aspect for aspect in aspects if isinstance(aspect, Quality)]
    educations = [aspect for aspect in aspects if isinstance(aspect, Education)]
    return skills and experience and qualities and educations
