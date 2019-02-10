from aspect_lookup import Skill, Experience, Quality, Education, Title
from utils import bot_color


def aspects_to_advert(aspects):
    skills = [x for x in aspects if isinstance(x, Skill)]
    experiences = [x for x in aspects if isinstance(x, Experience)]
    educations = [x for x in aspects if isinstance(x, Education)]  # sad s
    qualities = [x for x in aspects if isinstance(x, Quality)]  # sad s
    title = [x for x in aspects if isinstance(x, Title)][0]

    print(bot_color("\n\nHere's your job advert:"))

    print(bot_color('\nJob Title: {}\n'.format(title.representation)))

    if len(skills) > 0:
        print(bot_color('\nSkills'))
        for aspect in skills:
            print(bot_color('- {}'.format(aspect.representation)))

    if len(experiences) > 0:
        print(bot_color('\nExperience'))
        for aspect in experiences:
            print(bot_color('- {}'.format(aspect.representation)))

    if len(educations) > 0:
        print('\nEducation')
        for aspect in educations:
            print('- {}'.format(aspect.representation))


    if len(qualities) > 0:
        print(bot_color('\nQualities'))
        for aspect in qualities:
            print(bot_color('- {}'.format(aspect.representation)))
