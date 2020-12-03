def anagrams(word, words):
    if words == []:
        return []
    if sorted(word)== sorted(words[0]):
        return [words[0]] + anagrams(word, words[1:])
    return anagrams(word, words[1:])
