cities = {
    'beijing': {
        'country': 'china',
        'population': 20000000,
        'fact': 'it is capital of china.'
    },

    'shanghai': {
        'country': 'china',
        'populaton': 22000000,
        'fact': 'it is a beautiful city.'
    },

    'new york': {
        'country': 'america',
        'population': 8000000,
        'fact': 'it is bigger city of america.'
    },
}

for city, infos in cities.items():
    print('\n' + city)
    for key, value in infos.items():
        print('\t' + key + ': ' + str(value))