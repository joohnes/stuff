
# aaabbbcccd
# 1
def firstNonRepeating(text: str):
    dict = {}
    for char in text:
        if char not in dict:
            dict[char] = 1
            continue
        dict[char] += 1
    finallist = []
    if dict:
        for key in dict.keys():
            if dict[key] == 1:
                finallist.append(key)
        for char in text:
            if char in finallist:
                return char
    return "_"


tex = input("Enter: ")
print(f"First non-repeating letter in text is: {firstNonRepeating(tex)}")
