import pandas as pd
data_dict = {
    "name": ["Han", "Hue", "Ha"],
    "score": [8, 9, 10]
}
data = pd.DataFrame(data_dict)
print(data[data.name == "Hax"].score)
