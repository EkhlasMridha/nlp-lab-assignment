import pandas as pd
import re
from tabulate import tabulate
import operator


def loadDataset():
    data = pd.read_csv("./datasets/eng_bang_data.csv")
    return data["English"], data["Bangla"]


def corpusSizeWords(data):
    size = 0
    for singleData in data:
        size += len(re.split('[; |,]+', singleData))
    return size


def corpusSizeLines(data):
    size = 0
    for singleData in data:
        sentences = re.split(r'[!?.।]+ +', singleData)
        size += len(sentences)
    return size


def corpusSizeChars(data):
    size = 0
    for singleData in data:
        size += len(singleData)-singleData.count(" ")
    return size


def avgSentenceLength(totalWords, total_sentences):
    return totalWords/total_sentences


def vocabularySize(data):
    uniqueWords = set()
    for singleData in data:
        sentences = re.split(r'\s', singleData)
        for sen in sentences:
            uniqueWords.add(sen)
            
    return uniqueWords


def lex_div(data):
    allWord = []
    for singleData in data:
        sentences = re.split(r'\s', singleData)
        for sen in sentences:
            allWord.append(sen)

    uniqueWords = vocabularySize(data)
    wordFreq = []
    for word in uniqueWords:
        wordFreq.append(allWord.count(word))

    return sum(wordFreq)/len(wordFreq)


def top10FreqWords(data):
    allWord = []
    wordsFreq = {}

    for singleData in data:
        sentences = re.split(r'\s', singleData)
        for sen in sentences:
            allWord.append(sen)

    uniqueWords = vocabularySize(data)
    totalWords = len(allWord)

    for word in uniqueWords:
        unitWordFrequency = allWord.count(word)
        wordPercentage = (unitWordFrequency/totalWords)*100
        wordsFreq[word] = [unitWordFrequency, wordPercentage]

    sortedDict = sorted(wordsFreq.items(), key=operator.itemgetter(1), reverse=True)
    return sortedDict[:10]


def histogramTable(
        bangle,
        english
):
    print("\n(1) Statistics from parallel corpus:\n")
    table = [["Corpus size [words] excluding punctuation", english[0], bangle[0]],
             ["Corpus size [chars] excluding spaces", english[1], bangle[1]],
             ["Average sentence length [words]", english[2], bangle[2]],
             ["Vocabulary size [number of unique words]", english[3], bangle[3]],
             ["Lexical diversity*", english[4], bangle[4]],
             ["Corpus size [in lines]", english[5], bangle[5]]]
    headers = ["", "English side", "Bangla side"]
    print(tabulate(table, headers, tablefmt="pretty"))


if __name__ == "__main__":
    english_data, bangla_data = loadDataset()
    bangle_results = [
        corpusSizeWords(bangla_data),
        corpusSizeChars(bangla_data),
        avgSentenceLength(corpusSizeWords(bangla_data), corpusSizeLines(bangla_data)),
        len(vocabularySize(bangla_data)),
        lex_div(bangla_data),
        corpusSizeLines(bangla_data)
    ]
    english_results = [
        corpusSizeWords(english_data),
        corpusSizeChars(english_data),
        avgSentenceLength(corpusSizeWords(english_data), corpusSizeLines(english_data)),
        len(vocabularySize(english_data)),
        lex_div(english_data),
        corpusSizeLines(english_data)
    ]

    histogramTable(bangle_results, english_results)

    ban_freq_words = top10FreqWords(bangla_data)
    eng_freq_words = top10FreqWords(english_data)
    print("\n\n(2) Top ten frequent words in your parallel corpus:")
    print("Top ten frequent words in Bangla Side : ", ban_freq_words)
    print("Top ten frequent words in English Side : ", eng_freq_words)