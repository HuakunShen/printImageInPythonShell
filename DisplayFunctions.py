import csv
import time


def print_image(csv_reader):
    counter1 = 0
    for line in csv_reader:
        line_text = ''
        counter2 = 0
        for element in line:
            if counter2 == 7:
                if int(element) >= 6:
                    line_text += ' '
                else:
                    line_text += '*'
                counter2 = 0
            counter2 += 1
        if counter1 == 16:
            print(line_text)
            counter1 = 0
        counter1 += 1


def display(filename: str, wait_time: int):
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        print_image(csv_reader)
    time.sleep(wait_time)
