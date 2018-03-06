favorite_places = {
    'john': ['beijing', 'shanghai', 'shenzhen'],
    'peter': ['new york', 'boston', 'washington'],
    'lily': ['italy', 'china', 'france'],
}

for name, places in favorite_places.items():
    print('\n' + name + "'s favorite place: ")
    for place in places:
        print('\t' + place)