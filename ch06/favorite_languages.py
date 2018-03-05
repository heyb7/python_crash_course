favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("Sarah's favorite language is " + favorite_languages['sarah'].title() + '.')

print("\n")

#遍历字典中所有的键值对
for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + '.')

print('\n')

#遍历字典中所有的键
for name in favorite_languages.keys():
    print(name.title())

print('\n')

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + 
        favorite_languages[name].title() + "!")

print('\n')
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print('\n')
#按顺序遍历字典中的所有键
for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

#遍历字典中的所有值
print('\n')
print("The folloing languages have been mentioned.")
for language in favorite_languages.values():
    print(language.title())

#使用set剔除重复值
print('\n')
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())