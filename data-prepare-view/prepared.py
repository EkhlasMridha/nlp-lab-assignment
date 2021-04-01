import read_data as data_read


data = data_read.data
data = data.drop("Attribution", axis=1)
print("Modified Dataset : \n\n", data.head())

data.to_csv("../datasets/eng_bang_data.csv", index=False)


