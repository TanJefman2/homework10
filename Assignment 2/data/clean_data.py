import csv

states=[ "AK - Alaska", 
                "AL - Alabama", 
                "AR - Arkansas", 
                "AS - American Samoa", 
                "AZ - Arizona", 
                "CA - California", 
                "CO - Colorado", 
                "CT - Connecticut", 
                "DC - District of Columbia", 
                "DE - Delaware", 
                "FL - Florida", 
                "GA - Georgia", 
                "GU - Guam", 
                "HI - Hawaii", 
                "IA - Iowa", 
                "ID - Idaho", 
                "IL - Illinois", 
                "IN - Indiana", 
                "KS - Kansas", 
                "KY - Kentucky", 
                "LA - Louisiana", 
                "MA - Massachusetts", 
                "MD - Maryland", 
                "ME - Maine", 
                "MI - Michigan", 
                "MN - Minnesota", 
                "MO - Missouri", 
                "MS - Mississippi", 
                "MT - Montana", 
                "NC - North Carolina", 
                "ND - North Dakota", 
                "NE - Nebraska", 
                "NH - New Hampshire", 
                "NJ - New Jersey", 
                "NM - New Mexico", 
                "NV - Nevada", 
                "NY - New York", 
                "OH - Ohio", 
                "OK - Oklahoma", 
                "OR - Oregon", 
                "PA - Pennsylvania", 
                "PR - Puerto Rico", 
                "RI - Rhode Island", 
                "SC - South Carolina", 
                "SD - South Dakota", 
                "TN - Tennessee", 
                "TX - Texas", 
                "UT - Utah", 
                "VA - Virginia", 
                "VI - Virgin Islands", 
                "VT - Vermont", 
                "WA - Washington", 
                "WI - Wisconsin", 
                "WV - West Virginia", 
                "WY - Wyoming"]

states = [i.split(' - ') for i in states]
states_dict = {}
for i in states:
    states_dict[i[0]]=[i[1],0]

with open('test.csv') as csv_file:
    
    f = list(csv.reader(csv_file, delimiter=','))

with open('pizza_count_by_state.csv', mode='w') as new_file:
    write_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    
    
    columns = 'province,count'.split(',')
    write_file.writerow(columns)
    i=0
    for row in f[1:]:
        if len(row) == 0: continue


        province = row[-1]
        g = states_dict.get(province)
        states_dict[province] = [g[0],g[1]+1]

    print(states_dict)
    for idk in states_dict.values():
        
        write_file.writerow(idk)
        



        
