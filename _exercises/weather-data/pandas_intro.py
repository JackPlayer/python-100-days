import pandas

celsius_to_farenheit = lambda celsius: (celsius * (9/5)) + 32

def main():
    data = pandas.read_csv("weather-data.csv")

    print("The average temp is: " + str(data['temperature'].mean()))


if __name__ == "__main__":
    main()


