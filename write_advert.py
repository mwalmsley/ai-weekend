from aspect_lookup import Skill, Experience, Quality, Education


def aspects_to_advert(aspects):
    skills = [x for x in aspects if isinstance(x, Skill)]
    experiences = [x for x in aspects if isinstance(x, Experience)]
    educations = [x for x in aspects if isinstance(x, Education)]  # sad s
    qualities = [x for x in aspects if isinstance(x, Quality)]  # sad s

    print("\n\nHere's your job advert:")

    if len(skills) > 0:
        print('\nSkills')
        for aspect in skills:
            print('- {}'.format(aspect.representation))

    if len(experiences) > 0:
        print('\nExperience')
        for aspect in experiences:
            print('- {}'.format(aspect.representation))

    if len(educations) > 0:
        print('\nEducation')
        for aspect in educations:
            print('- {}'.format(aspect.representation))


    if len(qualities) > 0:
        print('\nQualities')
        for aspect in qualities:
            print('- {}'.format(aspect.representation))
