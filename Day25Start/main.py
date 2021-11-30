import csv
import pandas as pd
import functools


def main():
    # with open("./Day25Start/weather_data.csv") as file:
    #     data = csv.reader(file)
    #     temperature = [int(x[1]) for x in list(data)[1:]]
    #     print(temperature)
    # data = pd.read_csv("./Day25Start/weather_data.csv")
    # lst = data["temp"].to_list()
    # print(data["temp"].max())
    # print(data[data.temp == data["temp"].max()])
    # Create dataframe from scratch
    # data_dict = {
    #     "name": ["Han", "Hue", "Ha"],
    #     "score": [8, 9, 10]
    # }
    # df = pd.DataFrame(data_dict)
    # df.to_csv("./Day25Start/new_data.csv")
    # =====================================
    data = pd.read_csv("./Day25Start/Squirrel_Data.csv")
    col = data["Primary Fur Color"]
    print(col.groupby().count())


if __name__ == '__main__':
    main()
