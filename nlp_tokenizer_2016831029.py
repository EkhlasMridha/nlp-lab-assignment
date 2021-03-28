import re
import pandas as pd


data = pd.read_csv("./datasets/eng_bang_data.csv")
bangla = data["Bangla"]

bangla_sentences = []
count = 1


for data in bangla:
    sentences = re.split(r'\s', data)
    if len(sentences) > 1:
        print(count, "--", sentences, " - ", len(sentences))
        count += 1

    for sen in sentences:
        bangla_sentences.append(sen)


print("\nDatabase Size : ", len(bangle_data))
print("Total Number of Tokens : ", len(bangle_sentences))
