import string
import math
import statistics
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





def loadCoRoLaFrequencyList(filepath):
    freq_dict = {}
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            word, freq = line.strip().split()
            freq_dict[word] = int(freq)
    return freq_dict




def getAverageCoRoLaWordFrequency(text, freq_dict):
    
    #Words not found in freq_dict are ignored
    
    tokens = text.split()
    words = [token.strip(string.punctuation).lower() for token in tokens if token.strip(string.punctuation)]
    
    freqs = [freq_dict[w] for w in words if w in freq_dict]
    
    return sum(freqs) / len(freqs)




def getRareWordRatio(text, freq_dict, threshold):

    #Ratio of rare words in the text. A word is considered rare if its frequency in CoRoLa is below 'threshold'.
    
    tokens = text.split()
    words = [token.strip(string.punctuation).lower() for token in tokens if token.strip(string.punctuation)]
    
    rare_count = sum(1 for w in words if w in freq_dict and freq_dict[w] < threshold)
    return rare_count / len(words)





freq_dict = loadCoRoLaFrequencyList("src\corola_word_freq_all.tsv")
print(list(freq_dict.items())[100:110])


text = "Azi am mers la mare, nu la munte."

print("Average word frequency:", getAverageCoRoLaWordFrequency(text, freq_dict))
print("Rare word ratio:", getRareWordRatio(text, freq_dict, threshold=100000))

print(statistics.mean(freq_dict.values()))
print(statistics.median(freq_dict.values()))
print(statistics.mode(freq_dict.values()))

