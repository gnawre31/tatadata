#import yahoo_finance
#import numpy
#import mathplotlib
#import sklearn
import csv
		
cur_yr = 2017
count = 0
with open('NBTC_Tata_Challenge.csv', 'rb') as csvfile: #open desired file
	with open('results.csv', 'wb') as csvwrite:	
		file = csv.reader(csvfile, delimiter=',') #file object
		file2 = csv.writer(csvwrite, delimiter = ',')
		comp_name = []
		comp_sales = []
		num_games = []
		avg = []
		for row in file: #loop through file object referencing file with employee postal code4	
	#		print(count)	
			if row[9] == 'Global_Sales' :
				continue
				
			if row[4] not in comp_name:
				comp_name.append(row[4])
				comp_sales.append(float(row[9]))
				num_games.append(1)
				avg.append(0)
			elif row[4] in comp_name:
				num_games[comp_name.index(row[4])] += 1
				comp_sales[comp_name.index(row[4])] += float(row[9])
				avg[comp_name.index(row[4])] = (comp_sales[comp_name.index(row[4])] / num_games[comp_name.index(row[4])])
	#		count += 1
		
		for name in comp_name:
#			print(count)
			file2.writerow([name, comp_sales[comp_name.index(name)], avg[comp_name.index(name)]])
#			count += 1


		
#		print(row) #row is an array, row[0] is column 1, row[1] is column 2		
		
#import csv
#with open('eggs.csv', 'wb') as csvfile:
#    spamwriter = csv.writer(csvfile, delimiter=' ',
#                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
#    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])