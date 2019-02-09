from aspect_lookup import Skill, Experience, Quality, Education


def aspects_to_advert(aspects):
    skills = [x for x in aspects if isinstance(x, Skill)]
    experiences = [x for x in aspects if isinstance(x, Experience)]
    educations = [x for x in aspects if isinstance(x, Education)]  # sad s
    qualities = [x for x in aspects if isinstance(x, Quality)]  # sad s

    if len(skills) > 0:
        print('Skills: \n')
        for aspect in skills:
            print('- {}'.format(aspect.representation))

    if len(experiences) > 0:
        print('\nExperience:')
        for aspect in experiences:
            print('- {}'.format(aspect.representation))

    if len(educations) > 0:
        print('\nEducation:')
        for aspect in educations:
            print('- {}'.format(aspect.representation))


    if len(qualities) > 0:
        print('\nQuality:')
        for aspect in qualities:
            print('- {}'.format(aspect.representation))
