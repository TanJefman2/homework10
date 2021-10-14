import csv

# provinces = {}

with open('Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv') as csv_file:
    
    f = list(csv.reader(csv_file, delimiter=','))

with open('type_of_pizza_price_per_city.csv', mode='w') as new_file:
    write_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    columns = 'city,province,pizza_type,price'.split(',')
    write_file.writerow(columns)
    i=0
    for row in f[1:]:
        if len(row) == 0: continue

        city = row[6]
        province = row[-1]
        pizza = row[17]
        amountMax = row[12]
        amountMin = row[13]
        # print(amountMin,amountMax)
        if amountMin != amountMax: continue
        # print(pizza)
        
        if 'hawaiian' in pizza.lower(): write_file.writerow([city,province,'hawaiian',amountMin])
        if 'cheese' in pizza.lower(): write_file.writerow([city,province,'cheese',amountMin])
        if 'veggie' in pizza.lower(): write_file.writerow([city,province,'veggie',amountMin])
        if 'pepperoni' in pizza.lower(): write_file.writerow([city,province,'pepperoni',amountMin])
        if 'meat' in pizza.lower(): write_file.writerow([city,province,'meat',amountMin])
        if 'margherita' in pizza.lower(): write_file.writerow([city,province,'margherita',amountMin])
        if 'bbq chicken' in pizza.lower(): write_file.writerow([city,province,'bbq chicken',amountMin])
        if 'buffalo' in pizza.lower(): write_file.writerow([city,province,'buffalo',amountMin])

        # write_file.writerow([city,province,pizza,amountMin])
        

        # province = row[-1]
        # res_id = row[0]

        # if province in provinces:
        #     entry = provinces.get(province)
        #     entry[res_id] = 1
        #     provinces[province] = entry

        # else:
        #     entry = {}
        #     entry[res_id] = 1
        #     provinces[province] = entry
            

    # print(provinces)
    # for key in provinces:
    #     item = provinces.get(key)
        # write_file.writerow([key,sum(item.values())])



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
    
    


        



        
