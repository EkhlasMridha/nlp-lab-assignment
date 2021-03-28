import re
import pandas as pd


data = pd.read_csv("./datasets/eng_bang_data.csv")
bangla = data["Bangla"]

banglaSentences = []
count = 1


for data in bangla:
    sentences = re.split(r'[!?.।]+ +', data)
    if len(sentences) > 1:
        print( count, "--", sentences, " - ", len(sentences))
        count += 1

    for sen in sentences:
        banglaSentences.append(sen)


print("\nDatabase Size : ", len(bangla))
print("Total Number of Sentences : ", len(banglaSentences))
