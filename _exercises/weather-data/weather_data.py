import csv

def main():
    with open("weather-data.csv", "r") as csv_file:
        csv_data = csv.reader(csv_file)

        temperatures = [int(csv_day[1]) for csv_day in list(csv_data)[1:]]
        for day in csv_data:
            print(day)

        print(f"The temperatures are: {temperatures}")
if __name__ =="__main__":
    main()