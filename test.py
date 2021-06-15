favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

'''print(set(favorite_languages.values()))
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())'''

for k, v in favorite_languages.items():
    print(k + " likes " + v)

print(favorite_languages.items())