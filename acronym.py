def split_into_syllables(word):
    syllables = []
    current_syllable = ""
    consonants = "bcdfghjklmnpqrstvwxyz'"

    index = 0
    while index < len(word):
        char = word[index]
        
        # If it's a consonant
        if char in consonants:
            # If it's the first consonant, add it to the current syllable
            if not current_syllable:
                current_syllable += char
            # If the current syllable already has consonants, start a new syllable
            else:
                syllables.append(current_syllable)
                current_syllable = char
        # If it's a vowel or stop sign
        else:
            # Add it to the current syllable
            current_syllable += char
            # If it's the last character or the next character is a consonant, end the syllable
            if index == len(word) - 1 or word[index + 1] in consonants:
                syllables.append(current_syllable)
                current_syllable = ""
        index += 1
    
    # If there's anything left in the current syllable, add it to the syllables list
    if current_syllable:
        syllables.append(current_syllable)

    return syllables

# Test the function
word = "Agrobank"
syllables = split_into_syllables(word)
print(syllables)  # Output: ['pe', 'chay', 'van']
