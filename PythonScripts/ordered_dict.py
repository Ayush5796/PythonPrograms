from collections import OrderedDict

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'java'
favourite_languages['john'] = 'c++'
favourite_languages['stephan'] = 'c'

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + language.title() + ".")