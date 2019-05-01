def wordsRecognition(word1, word2):
    def getIdentifier(w1, w2):
        return ''.join(sorted(set(s for s in w1 if s not in w2)))

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]
