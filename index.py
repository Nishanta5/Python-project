import csv
import time

def add(a,b):
    return a+b

def writeToCsv():
    for i in range(1,21):
        sum = add(i * 100, (i + 5) * 1000)
        with open(rf'sample.csv', 'a') as f:
            writer = csv.writer(f)
            writer.writerow([i, sum])
        time.sleep(2)
    f.close()

writeToCsv()