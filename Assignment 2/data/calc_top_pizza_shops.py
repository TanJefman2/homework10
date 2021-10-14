import csv
import re
shops = {}

with open('Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv') as csv_file:
    
    f = list(csv.reader(csv_file, delimiter=','))

with open('top_pizza_shop.csv', mode='w') as new_file:
    write_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
    columns = 'restaurant,count'.split(',')
    write_file.writerow(columns)
    i=0
    for row in f[1:]:
        if len(row) == 0: continue

        shop = row[-6]
        id = row[0]

        if re.search('^papa john.*',shop.lower()): shop = "Papa John's Pizza"
        if re.search('^papa murphy.*',shop.lower()): shop = "Papa Murphy's Pizza"
        if re.search('^jets.*',shop.lower()): shop = "Jet's Pizza"
        if re.search('^california.*',shop.lower()): shop = "California Pizza Kitchen"
        if re.search('^jets.*',shop.lower()): shop = "Jet's Pizza"
        if re.search('^hungry howie.*',shop.lower()): shop = "Hungry Howie's Pizza"
        if re.search('^little caesar.*',shop.lower()): shop = "Little Caesar's Pizza"
        if re.search('^rocky rococo.*',shop.lower()): shop = "Rocky Rococo"
        if re.search('^barro.*',shop.lower()): shop = "Barro's Pizza"
        if re.search('^johnny.*',shop.lower()): shop = "Johnny's Pizza"
        if re.search('^larosa.*',shop.lower()): shop = "LaRosa's Pizzeria"
        if re.search('^doubledave.*',shop.lower()): shop = "DoubleDave's Pizza Works"
        if re.search('^mazzio.*',shop.lower()): shop = "Mazzio's Pizza"
        if re.search('^zpizza.*',shop.lower()): shop = "Zpizza"
        if re.search('^rosati.*',shop.lower()): shop = "Rosati's Pizza"
        if re.search('^giordano.*',shop.lower()): shop = "Giordano's Pizza"
        if re.search('^grimaldi.*',shop.lower()): shop = "Grimaldi's Pizza"
        if re.search('^romeo.*',shop.lower()): shop = "Romeo's Pizza"

        if shop in shops:
            entry = shops.get(shop)
            if id not in entry: entry.append(id)
            shops[shop] = entry

        else:
            entry = [id]
            shops[shop] = entry
            

    shops = {k: v for k, v in sorted(shops.items(), key=lambda item: len(item[1]), reverse=True)}
    print(shops)
    i=8
    total=0
    for key in shops:
        item = shops.get(key)
        if i==0:
            total+= len(item)
        else:
            write_file.writerow([key, len(item)])
            i-=1
        
    #write_file.writerow(["other", total])


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
    
    


        



        
