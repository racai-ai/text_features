import string
import math
from collections import Counter

def getPunctuationCount(text):

    punctuation_set = set(string.punctuation)
    punctuation_count = 0

    for ch in text:
        if ch in punctuation_set:
            punctuation_count = punctuation_count + 1

    return punctuation_count

print(getPunctuationCount("a.tett,ythth!"))


def getAverageSentenceLength(text):

    for sep in ".!?":
        text = text.replace(sep, "|")

    sentences = [s.strip() for s in text.split("|") if s.strip()]

    word_counts = []
    for sentence in sentences:
        tokens = sentence.split()
        words = [token.strip(string.punctuation) for token in tokens if token.strip(string.punctuation)]
        word_counts.append(len(words))

    avg_length = sum(word_counts) / len(word_counts)
    return avg_length


print(getAverageSentenceLength("Hello! How are you doing today? I am fine, thank you."))



def getNumberOfSentences(text):

    for sep in ".!?":
        text = text.replace(sep, "|")

    sentences = [s.strip() for s in text.split("|") if s.strip()]

    return len(sentences)


print(getNumberOfSentences("Hello! How are you doing today? I am fine, thank you."))


def getAverageCharactersPerWord(text):

    tokens = text.split()

    words = [token.strip(string.punctuation) for token in tokens if token.strip(string.punctuation)]

    total_chars = sum(len(word) for word in words)
    avg_chars = total_chars / len(words)

    return avg_chars

print(getAverageCharactersPerWord("Testing this function"))



def getUniqueWordRatio(text):

    tokens = text.split()
    words = [token.strip(string.punctuation).lower() for token in tokens if token.strip(string.punctuation)]

    unique_words = set(words)
    ratio = len(unique_words) / len(words)
    return ratio


print(getUniqueWordRatio("Hello! How are you doing today? I am fine, thank you."))



def getYuleK(text):

    #Lower K = more diverse vocabulary, Higher K = more repetition
    
    tokens = text.split()
    words = [token.strip(string.punctuation).lower() for token in tokens if token.strip(string.punctuation)]

    N = len(words) 

    freqs = Counter(words)
    freq_of_freq = Counter(freqs.values())

    sum_i2Vi = sum(i**2 * Vi for i, Vi in freq_of_freq.items())

    K = 10000 * (sum_i2Vi - N) / (N**2)
    return K

print(getYuleK("The cat sleeps, the cat runs. The cat eats."))


def getMaas(text):
    
    #Another type of lexical diversity measure

    tokens = text.split()
    words = [token.strip(string.punctuation).lower() for token in tokens if token.strip(string.punctuation)]

    N = len(words)     
    V = len(set(words))  

    Maas = (math.log(N) - math.log(V)) / (math.log(N)**2)

    return Maas

print(getMaas("The cat sleeps, the cat runs. The cat eats."))
