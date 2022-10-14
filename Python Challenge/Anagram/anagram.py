def find_anagrams(word, candidates):
    
    result = []

    for i in candidates:
        if word.lower() == i.lower():
            continue
        elif sorted(word.lower()) == sorted(i.lower()):
            print(word)
            print(i)
            result.append(i)
    
    return result
