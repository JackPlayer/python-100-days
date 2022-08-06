import numpy
import numpy as np
import pandas

def main():
    squirrel_data = pandas.read_csv("squirrel_data.csv")

    fur_color_dict = {}
    distinct_fur_colors = squirrel_data["Primary Fur Color"].unique()

    print(distinct_fur_colors)
    fur_color_counts = []

    for distinct_fur_color in distinct_fur_colors:
        count = len(squirrel_data[squirrel_data["Primary Fur Color"] == distinct_fur_color])
        fur_color_counts.append(count)
    print(len(fur_color_counts))

    print(len(list(distinct_fur_colors)[1:]))
    fur_data_dict ={
        "fur_colors": list(distinct_fur_colors),
        "counts": fur_color_counts
    }

    fur_data_df = pandas.DataFrame.from_dict(fur_data_dict)
    print(fur_data_df)


if __name__ == "__main__":
    main()

