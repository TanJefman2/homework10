import csv

provinces = {}

with open('Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv') as csv_file:
    
    f = list(csv.reader(csv_file, delimiter=','))

with open('pizza_statistic_by_province.csv', mode='w') as new_file:
    write_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    columns = 'province,restaurant_count,avg_pizza_price,avg_min_spend'.split(',')
    write_file.writerow(columns)
    i=0
    for row in f[1:]:
        if len(row) == 0: continue

        province = row[-1]
        res_id = row[0]
        amountMax = float(row[12])
        amountMin = float(row[13])
        priceRangeMin = float(row[-3])
        priceRangeMax = float(row[-2])

        
        if amountMax != amountMin or priceRangeMin == 0 or priceRangeMax == 0: continue

        if province in provinces:
            entry = provinces.get(province)
            entry[0].append(amountMin)
            entry[1][res_id] = priceRangeMin
            provinces[province] = entry

        else:
            # province, pizza prices, restaurants
            entry = [[amountMin], {}]
            entry[1][res_id] = priceRangeMin
            provinces[province] = entry
            
    from statistics import mean

    print(provinces)
    for key in provinces:
        item = provinces.get(key)

        write_file.writerow([key,len(item[1].values()), round(mean(item[0]),2), round(mean(item[1].values()),2)])



##import csv
##
##with open('sleepdata.csv') as csv_file:
##    
##    f = list(csv.reader(csv_file, delimiter=';'))
##
##with open('cleaned_data.csv', mode='w') as new_file:
##    write_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
##
##    
##    
##    columns = ['Time', 'Time type', 'Sleep quality', 'Time in bed', 'Wake up']
##    new = ['Drank coffee','Ate late','Stressful day','Worked out','Drank tea']
##    print(columns+new)
##    write_file.writerow(columns+new)
##        
##    for row in f[1:]:
##        if len(row) == 0: continue
##
##        print(row)
##        record=['']*10
##        start_time='2014-12-30 '+row[0][11:] if int(row[0][11])>1 else '2014-12-31 '+row[0][11:]
##        end_time='2014-12-31 '+row[1][11:] if int(row[1][11])<1 else '2014-12-30 '+row[1][11:]
##        record[2]=int(row[2][:-1])
##        
##        p=list(map(int,row[3].split(':')))
##        record[3]=(p[0]*60)+p[1]
##
##        record[4]=row[4]
##        record[5:] = ['False']*5
##
##        l=row[5].split(':')
##        for c in l:
##            if c == '': continue
##            if c not in new: raise Exception(c)
##            record[5+new.index(c)]='True'
##        
##        print(record)
##        write_file.writerow([start_time,'start']+record[2:])
##        write_file.writerow([end_time,'end']+record[2:])
    
    


        



        
