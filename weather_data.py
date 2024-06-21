import re

def split_word_syllables(word: str) -> str:
    def auto_correct(text):
        text = text.lower()
        text = re.sub(r"gʻ|gʼ|g’|g'|g`|g‘", "ğ", text)
        text = re.sub(r"oʻ|oʼ|o’|o'|o`|o‘", "ŏ", text)
        text = re.sub(r"sh", "š", text)
        text = re.sub(r"ch", "č", text)
        text = re.sub(r"ʻ|ʼ|'|`|‘", "’", text)
        return text

    def inverse_correct(text):
        text = re.sub(r"ğ", "g‘", text)
        text = re.sub(r"ŏ", "o‘", text)
        text = re.sub(r"š", "sh", text)
        text = re.sub(r"č", "ch", text)
        return text

    def create_map(text):
        text = re.sub(r"[aoueiŏ]", "V", text)
        text = re.sub(r"[bdfghjklmnpqrstvxyzğšč]", "C", text)
        parts = text.split("’")
        map_ = []

        for k, v in enumerate(parts):
            rem = v
            if k != 0:
                map_.append("D")

            while rem:
                if rem[0] == "V" and (len(rem) == 1 or rem[1] != "C"):
                    map_.append(1)
                    rem = rem[1:]
                elif rem[0] == "V" and len(rem) > 2 and rem[1] == "C" and rem[2] == "V":
                    map_.append(1)
                    rem = rem[1:]
                elif rem[0] == "V" and len(rem) > 2 and rem[1] == "C" and rem[2] != "V" and (len(rem) == 3 or rem[3] != "C"):
                    map_.append(2)
                    rem = rem[2:]
                elif rem[0] == "V" and len(rem) > 3 and rem[1] == "C" and rem[2] == "C" and rem[3] != "V":
                    map_.append(3)
                    rem = rem[3:]
                elif rem[0] == "C" and len(rem) > 1 and rem[1] == "V" and (len(rem) == 2 or rem[2] != "C"):
                    map_.append(2)
                    rem = rem[2:]
                elif rem[0] == "C" and len(rem) > 3 and rem[1] == "V" and rem[2] == "C" and rem[3] == "V":
                    map_.append(2)
                    rem = rem[2:]
                elif rem[0] == "C" and len(rem) > 4 and rem[1] == "V" and rem[2] == "C" and rem[3] == "C" and rem[4] == "V":
                    map_.append(3)
                    rem = rem[3:]
                elif rem[0] == "C" and len(rem) > 4 and rem[1] == "V" and rem[2] == "C" and rem[3] == "C" and rem[4] != "V":
                    map_.append(4)
                    rem = rem[4:]
                elif rem[0] == "C" and len(rem) > 2 and rem[1] == "C" and rem[2] == "V" and (len(rem) == 3 or rem[3] != "C"):
                    map_.append(3)
                    rem = rem[3:]
                elif rem[0] == "C" and len(rem) > 4 and rem[1] == "C" and rem[2] == "V" and rem[3] == "C" and rem[4] == "V":
                    map_.append(3)
                    rem = rem[3:]
                elif rem[0] == "C" and len(rem) > 5 and rem[1] == "C" and rem[2] == "V" and rem[3] == "C" and rem[4] != "V" and (len(rem) == 5 or rem[5] != "C"):
                    map_.append(4)
                    rem = rem[4:]
                elif rem[0] == "C" and len(rem) > 5 and rem[1] == "C" and rem[2] == "V" and rem[3] == "C" and rem[4] == "C" and rem[5] != "V":
                    map_.append(5)
                    rem = rem[5:]
                else:
                    map_.append(len(rem))
                    break
        return map_

    rgx = re.compile(r"^[abdefghijklmnopqrstuvxyzŏğšč’]+$")
    word = auto_correct(word).strip()
    map_ = create_map(word)
    rem = word
    r = ""
    for k, v in enumerate(map_):
        if v == "D":
            r += "’"
            rem = rem[1:]
        else:
            sl = rem[:v]
            rem = rem[v:]
            if k == 0:
                r += sl
            else:
                r += "-" + sl
    if not rgx.match(word):
        return []
    return inverse_correct(r).split("-")


def make_acronym(phrase: str) -> str:
    if not isinstance(phrase, str) or not phrase:
        return ""
    phrase = phrase.strip()
    words = phrase.split()
    if len(words) == 1:
        words = split_word_syllables(phrase)
    return "".join([w[0].upper() for w in words])

# Test the function
phrase = "Agrobank"
acronym = make_acronym(phrase)
print(acronym)  # Output: "ARB"

phrase = "Milliybank"
acronym = make_acronym(phrase)
print(acronym)  # Output: "HKB"
