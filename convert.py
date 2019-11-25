import csv
import sys

def main():
    try:
        filename = sys.argv[1]
        csvfile = open(filename)
    except IndexError:
        print("Error: Please give a filename to convert as first argument")
        sys.exit(1)
    
    dialect = csv.Sniffer().sniff(csvfile.read(2048))
    csvfile.seek(0)
    
    outfile = open(filename + '_converted.csv', 'w')
    writer = csv.writer(outfile, delimiter=',', quoting=csv.QUOTE_ALL)
    for line in csv.reader(csvfile, dialect):
        writer.writerow(line)
    
    
    
if __name__ == '__main__':
    main()