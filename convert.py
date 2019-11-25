import csv
import sys
import io

def main():
    try:
        filename = sys.argv[1]
        csvfile = io.open(filename, encoding="utf-8")
    except IndexError:
        print("Error: Please give a filename to convert as first argument")
        sys.exit(1)
    
    outfile = io.open(filename + '_converted.csv', 'w', encoding="utf-8")
    writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)
    for line in csv.reader(csvfile, delimiter=','):
        writer.writerow(line)
    
    
if __name__ == '__main__':
    main()