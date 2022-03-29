import csv
import numpy as np


def getDataSource(data_path):
    sleep_in_hours = []
    cups_of_coffee = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            sleep_in_hours.append(float(row["sleep in hours"]))
            cups_of_coffee.append(float(row["\tAverage amount of coffee drank(cups)"]))

    return {"x" : sleep_in_hours, "y": cups_of_coffee}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between amount of sleep and average amount of cups of coffee consumed :-  \n--->",correlation[0,1])

data_path  = "Cups of coffee & Hours of sleep.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)