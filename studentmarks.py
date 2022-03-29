import csv
import numpy as np


def getDataSource(data_path):
    Days_Present = []
    Average_score = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Days_Present.append(float(row["Days Present"]))
            Average_score.append(float(row["\tAverage score of a student per days of presence"]))

    return {"x" : Days_Present, "y": Average_score}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between days of absence and average score of a student :-  \n--->",correlation[0,1])

data_path  = "Student Marks vs Days Present.csv"
datasource = getDataSource(data_path)
findCorrelation(datasource)