import re
from collections import Counter
import csv


def reader(filename):

    pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

    with open(filename) as f:
        log = f.read()

        ip_list = re.findall(pattern, log)

    return ip_list

def count(ip_list):
    count = Counter(ip_list)

    return count

def write_csv(count):

    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['IP', 'Requests']
        writer.writerow(header)

        for item in count:
            writer.writerow((item, count[item]))





if __name__ == '__main__':
    write_csv(count(reader('log.log')))
