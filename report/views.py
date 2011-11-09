import csv
csv_file = csv.writer(open('eggs.csv', 'wb'), delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
spamWriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])
