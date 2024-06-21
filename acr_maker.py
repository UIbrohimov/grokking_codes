def split_into_syllables(word):
    syllables = []
    
    vowels = "aeiouy"
    
    for letter in word:
        if letter.lower() in vowels:
            index = word.find(letter) + 1
            if index == 0:
                break
            if word[word.index(letter)+2] in vowels:
                syllable = word[0:index]
                word = word[index:]
                syllables.append(syllable)
            else:
                syllable = word[0:index+1]
                word = word[index+1:]
                syllables.append(syllable)

    return syllables


def make_acronym(syllables):
    acronym = ""
    for syllable in syllables:
        acronym += syllable[0].upper()

    if len(acronym) > 3:
        return acronym[0] + acronym[len(acronym)-2:]

    return acronym


# Test the function
word = "Milliybank"
syllables = split_into_syllables(word)
print(syllables)
print(make_acronym(syllables)) 

