import csv

states=["California","Texas","New York","Florida","Illinois","Pennsylvania","Ohio","Michigan","Georgia","North Carolina","New Jersey","Virginia","Washington","Massachusetts","Indiana","Arizona","Tennessee","Missouri","Maryland","Wisconsin","Minnesota","Colorado","Alabama","South Carolina","Louisiana","Kentucky","Oregon","Oklahoma","Connecticut","Iowa","Mississippi","Arkansas","Kansas","Utah","Nevada","New Mexico","West Virginia","Nebraska","Idaho","Hawaii","Maine","New Hampshire","Rhode Island","Montana","Delaware","South Dakota","Alaska","North Dakota","Vermont","District of Columbia","Wyoming"]
cities=[{
        "city": "New York", 
        "growth_from_2000_to_2013": "4.8%", 
        "latitude": 40.7127837, 
        "longitude": -74.0059413, 
        "population": "8405837", 
        "rank": "1", 
        "state": "New York"
    }, 
    {
        "city": "Los Angeles", 
        "growth_from_2000_to_2013": "4.8%", 
        "latitude": 34.0522342, 
        "longitude": -118.2436849, 
        "population": "3884307", 
        "rank": "2", 
        "state": "California"
    }, 
    {
        "city": "Chicago", 
        "growth_from_2000_to_2013": "-6.1%", 
        "latitude": 41.8781136, 
        "longitude": -87.6297982, 
        "population": "2718782", 
        "rank": "3", 
        "state": "Illinois"
    }, 
    {
        "city": "Houston", 
        "growth_from_2000_to_2013": "11.0%", 
        "latitude": 29.7604267, 
        "longitude": -95.3698028, 
        "population": "2195914", 
        "rank": "4", 
        "state": "Texas"
    }, 
    {
        "city": "Philadelphia", 
        "growth_from_2000_to_2013": "2.6%", 
        "latitude": 39.9525839, 
        "longitude": -75.1652215, 
        "population": "1553165", 
        "rank": "5", 
        "state": "Pennsylvania"
    }, 
    {
        "city": "Phoenix", 
        "growth_from_2000_to_2013": "14.0%", 
        "latitude": 33.4483771, 
        "longitude": -112.0740373, 
        "population": "1513367", 
        "rank": "6", 
        "state": "Arizona"
    }, 
    {
        "city": "San Antonio", 
        "growth_from_2000_to_2013": "21.0%", 
        "latitude": 29.4241219, 
        "longitude": -98.49362819999999, 
        "population": "1409019", 
        "rank": "7", 
        "state": "Texas"
    }, 
    {
        "city": "San Diego", 
        "growth_from_2000_to_2013": "10.5%", 
        "latitude": 32.715738, 
        "longitude": -117.1610838, 
        "population": "1355896", 
        "rank": "8", 
        "state": "California"
    }, 
    {
        "city": "Dallas", 
        "growth_from_2000_to_2013": "5.6%", 
        "latitude": 32.7766642, 
        "longitude": -96.79698789999999, 
        "population": "1257676", 
        "rank": "9", 
        "state": "Texas"
    }, 
    {
        "city": "San Jose", 
        "growth_from_2000_to_2013": "10.5%", 
        "latitude": 37.3382082, 
        "longitude": -121.8863286, 
        "population": "998537", 
        "rank": "10", 
        "state": "California"
    }, 
    {
        "city": "Austin", 
        "growth_from_2000_to_2013": "31.7%", 
        "latitude": 30.267153, 
        "longitude": -97.7430608, 
        "population": "885400", 
        "rank": "11", 
        "state": "Texas"
    }, 
    {
        "city": "Indianapolis", 
        "growth_from_2000_to_2013": "7.8%", 
        "latitude": 39.768403, 
        "longitude": -86.158068, 
        "population": "843393", 
        "rank": "12", 
        "state": "Indiana"
    }, 
    {
        "city": "Jacksonville", 
        "growth_from_2000_to_2013": "14.3%", 
        "latitude": 30.3321838, 
        "longitude": -81.65565099999999, 
        "population": "842583", 
        "rank": "13", 
        "state": "Florida"
    }, 
    {
        "city": "San Francisco", 
        "growth_from_2000_to_2013": "7.7%", 
        "latitude": 37.7749295, 
        "longitude": -122.4194155, 
        "population": "837442", 
        "rank": "14", 
        "state": "California"
    }, 
    {
        "city": "Columbus", 
        "growth_from_2000_to_2013": "14.8%", 
        "latitude": 39.9611755, 
        "longitude": -82.99879419999999, 
        "population": "822553", 
        "rank": "15", 
        "state": "Ohio"
    }, 
    {
        "city": "Charlotte", 
        "growth_from_2000_to_2013": "39.1%", 
        "latitude": 35.2270869, 
        "longitude": -80.8431267, 
        "population": "792862", 
        "rank": "16", 
        "state": "North Carolina"
    }, 
    {
        "city": "Fort Worth", 
        "growth_from_2000_to_2013": "45.1%", 
        "latitude": 32.7554883, 
        "longitude": -97.3307658, 
        "population": "792727", 
        "rank": "17", 
        "state": "Texas"
    }, 
    {
        "city": "Detroit", 
        "growth_from_2000_to_2013": "-27.1%", 
        "latitude": 42.331427, 
        "longitude": -83.0457538, 
        "population": "688701", 
        "rank": "18", 
        "state": "Michigan"
    }, 
    {
        "city": "El Paso", 
        "growth_from_2000_to_2013": "19.4%", 
        "latitude": 31.7775757, 
        "longitude": -106.4424559, 
        "population": "674433", 
        "rank": "19", 
        "state": "Texas"
    }, 
    {
        "city": "Memphis", 
        "growth_from_2000_to_2013": "-5.3%", 
        "latitude": 35.1495343, 
        "longitude": -90.0489801, 
        "population": "653450", 
        "rank": "20", 
        "state": "Tennessee"
    }, 
    {
        "city": "Seattle", 
        "growth_from_2000_to_2013": "15.6%", 
        "latitude": 47.6062095, 
        "longitude": -122.3320708, 
        "population": "652405", 
        "rank": "21", 
        "state": "Washington"
    }, 
    {
        "city": "Denver", 
        "growth_from_2000_to_2013": "16.7%", 
        "latitude": 39.7392358, 
        "longitude": -104.990251, 
        "population": "649495", 
        "rank": "22", 
        "state": "Colorado"
    }, 
    {
        "city": "Washington", 
        "growth_from_2000_to_2013": "13.0%", 
        "latitude": 38.9071923, 
        "longitude": -77.0368707, 
        "population": "646449", 
        "rank": "23", 
        "state": "District of Columbia"
    }, 
    {
        "city": "Boston", 
        "growth_from_2000_to_2013": "9.4%", 
        "latitude": 42.3600825, 
        "longitude": -71.0588801, 
        "population": "645966", 
        "rank": "24", 
        "state": "Massachusetts"
    }, 
    {
        "city": "Nashville-Davidson", 
        "growth_from_2000_to_2013": "16.2%", 
        "latitude": 36.1626638, 
        "longitude": -86.7816016, 
        "population": "634464", 
        "rank": "25", 
        "state": "Tennessee"
    }, 
    {
        "city": "Baltimore", 
        "growth_from_2000_to_2013": "-4.0%", 
        "latitude": 39.2903848, 
        "longitude": -76.6121893, 
        "population": "622104", 
        "rank": "26", 
        "state": "Maryland"
    }, 
    {
        "city": "Oklahoma City", 
        "growth_from_2000_to_2013": "20.2%", 
        "latitude": 35.4675602, 
        "longitude": -97.5164276, 
        "population": "610613", 
        "rank": "27", 
        "state": "Oklahoma"
    }, 
    {
        "city": "Louisville/Jefferson County", 
        "growth_from_2000_to_2013": "10.0%", 
        "latitude": 38.2526647, 
        "longitude": -85.7584557, 
        "population": "609893", 
        "rank": "28", 
        "state": "Kentucky"
    }, 
    {
        "city": "Portland", 
        "growth_from_2000_to_2013": "15.0%", 
        "latitude": 45.5230622, 
        "longitude": -122.6764816, 
        "population": "609456", 
        "rank": "29", 
        "state": "Oregon"
    }, 
    {
        "city": "Las Vegas", 
        "growth_from_2000_to_2013": "24.5%", 
        "latitude": 36.1699412, 
        "longitude": -115.1398296, 
        "population": "603488", 
        "rank": "30", 
        "state": "Nevada"
    }, 
    {
        "city": "Milwaukee", 
        "growth_from_2000_to_2013": "0.3%", 
        "latitude": 43.0389025, 
        "longitude": -87.9064736, 
        "population": "599164", 
        "rank": "31", 
        "state": "Wisconsin"
    },{
        "city": "Albuquerque", 
        "growth_from_2000_to_2013": "23.5%", 
        "latitude": 35.0853336, 
        "longitude": -106.6055534, 
        "population": "556495", 
        "rank": "32", 
        "state": "New Mexico"
    }, 
    {
        "city": "Tucson", 
        "growth_from_2000_to_2013": "7.5%", 
        "latitude": 32.2217429, 
        "longitude": -110.926479, 
        "population": "526116", 
        "rank": "33", 
        "state": "Arizona"
    }, 
    {
        "city": "Fresno", 
        "growth_from_2000_to_2013": "18.3%", 
        "latitude": 36.7468422, 
        "longitude": -119.7725868, 
        "population": "509924", 
        "rank": "34", 
        "state": "California"
    }, 
    {
        "city": "Sacramento", 
        "growth_from_2000_to_2013": "17.2%", 
        "latitude": 38.5815719, 
        "longitude": -121.4943996, 
        "population": "479686", 
        "rank": "35", 
        "state": "California"
    }, 
    {
        "city": "Long Beach", 
        "growth_from_2000_to_2013": "1.5%", 
        "latitude": 33.7700504, 
        "longitude": -118.1937395, 
        "population": "469428", 
        "rank": "36", 
        "state": "California"
    }, 
    {
        "city": "Kansas City", 
        "growth_from_2000_to_2013": "5.5%", 
        "latitude": 39.0997265, 
        "longitude": -94.5785667, 
        "population": "467007", 
        "rank": "37", 
        "state": "Missouri"
    }, 
    {
        "city": "Mesa", 
        "growth_from_2000_to_2013": "13.5%", 
        "latitude": 33.4151843, 
        "longitude": -111.8314724, 
        "population": "457587", 
        "rank": "38", 
        "state": "Arizona"
    }, 
    {
        "city": "Virginia Beach", 
        "growth_from_2000_to_2013": "5.1%", 
        "latitude": 36.8529263, 
        "longitude": -75.97798499999999, 
        "population": "448479", 
        "rank": "39", 
        "state": "Virginia"
    }, 
    {
        "city": "Atlanta", 
        "growth_from_2000_to_2013": "6.2%", 
        "latitude": 33.7489954, 
        "longitude": -84.3879824, 
        "population": "447841", 
        "rank": "40", 
        "state": "Georgia"
    }, 
    {
        "city": "Colorado Springs", 
        "growth_from_2000_to_2013": "21.4%", 
        "latitude": 38.8338816, 
        "longitude": -104.8213634, 
        "population": "439886", 
        "rank": "41", 
        "state": "Colorado"
    }, 
    {
        "city": "Omaha", 
        "growth_from_2000_to_2013": "5.9%", 
        "latitude": 41.2523634, 
        "longitude": -95.99798829999999, 
        "population": "434353", 
        "rank": "42", 
        "state": "Nebraska"
    }, 
    {
        "city": "Raleigh", 
        "growth_from_2000_to_2013": "48.7%", 
        "latitude": 35.7795897, 
        "longitude": -78.6381787, 
        "population": "431746", 
        "rank": "43", 
        "state": "North Carolina"
    }, 
    {
        "city": "Miami", 
        "growth_from_2000_to_2013": "14.9%", 
        "latitude": 25.7616798, 
        "longitude": -80.1917902, 
        "population": "417650", 
        "rank": "44", 
        "state": "Florida"
    }, 
    {
        "city": "Oakland", 
        "growth_from_2000_to_2013": "1.3%", 
        "latitude": 37.8043637, 
        "longitude": -122.2711137, 
        "population": "406253", 
        "rank": "45", 
        "state": "California"
    }, 
    {
        "city": "Minneapolis", 
        "growth_from_2000_to_2013": "4.5%", 
        "latitude": 44.977753, 
        "longitude": -93.2650108, 
        "population": "400070", 
        "rank": "46", 
        "state": "Minnesota"
    }, 
    {
        "city": "Tulsa", 
        "growth_from_2000_to_2013": "1.3%", 
        "latitude": 36.1539816, 
        "longitude": -95.99277500000001, 
        "population": "398121", 
        "rank": "47", 
        "state": "Oklahoma"
    }, 
    {
        "city": "Cleveland", 
        "growth_from_2000_to_2013": "-18.1%", 
        "latitude": 41.49932, 
        "longitude": -81.6943605, 
        "population": "390113", 
        "rank": "48", 
        "state": "Ohio"
    }, 
    {
        "city": "Wichita", 
        "growth_from_2000_to_2013": "9.7%", 
        "latitude": 37.688889, 
        "longitude": -97.336111, 
        "population": "386552", 
        "rank": "49", 
        "state": "Kansas"
    }, 
    {
        "city": "Arlington", 
        "growth_from_2000_to_2013": "13.3%", 
        "latitude": 32.735687, 
        "longitude": -97.10806559999999, 
        "population": "379577", 
        "rank": "50", 
        "state": "Texas"
    }, 
    {
        "city": "New Orleans", 
        "growth_from_2000_to_2013": "-21.6%", 
        "latitude": 29.95106579999999, 
        "longitude": -90.0715323, 
        "population": "378715", 
        "rank": "51", 
        "state": "Louisiana"
    }, 
    {
        "city": "Bakersfield", 
        "growth_from_2000_to_2013": "48.4%", 
        "latitude": 35.3732921, 
        "longitude": -119.0187125, 
        "population": "363630", 
        "rank": "52", 
        "state": "California"
    }, 
    {
        "city": "Tampa", 
        "growth_from_2000_to_2013": "16.0%", 
        "latitude": 27.950575, 
        "longitude": -82.4571776, 
        "population": "352957", 
        "rank": "53", 
        "state": "Florida"
    }, 
    {
        "city": "Honolulu", 
        "growth_from_2000_to_2013": "-6.2%", 
        "latitude": 21.3069444, 
        "longitude": -157.8583333, 
        "population": "347884", 
        "rank": "54", 
        "state": "Hawaii"
    }, 
    {
        "city": "Aurora", 
        "growth_from_2000_to_2013": "24.4%", 
        "latitude": 39.7294319, 
        "longitude": -104.8319195, 
        "population": "345803", 
        "rank": "55", 
        "state": "Colorado"
    }, 
    {
        "city": "Anaheim", 
        "growth_from_2000_to_2013": "4.7%", 
        "latitude": 33.8352932, 
        "longitude": -117.9145036, 
        "population": "345012", 
        "rank": "56", 
        "state": "California"
    }, 
    {
        "city": "Santa Ana", 
        "growth_from_2000_to_2013": "-1.2%", 
        "latitude": 33.7455731, 
        "longitude": -117.8678338, 
        "population": "334227", 
        "rank": "57", 
        "state": "California"
    }, 
    {
        "city": "St. Louis", 
        "growth_from_2000_to_2013": "-8.2%", 
        "latitude": 38.6270025, 
        "longitude": -90.19940419999999, 
        "population": "318416", 
        "rank": "58", 
        "state": "Missouri"
    }, 
    {
        "city": "Riverside", 
        "growth_from_2000_to_2013": "22.5%", 
        "latitude": 33.9533487, 
        "longitude": -117.3961564, 
        "population": "316619", 
        "rank": "59", 
        "state": "California"
    }]
city_filter = "datum.city == 'New York' || datum.city == 'Los Angeles' || datum.city == 'Chicago' ||datum.city == 'Houston' ||datum.city == 'Philadelphia' ||datum.city == 'San Antonio' ||datum.city == 'San Diego' ||datum.city == 'Dallas' ||datum.city == 'Austin'"

city_filter_2 = "datum.city == 'New York'|| datum.city == 'Los Angeles'|| datum.city == 'Chicago'|| datum.city == 'Houston'|| datum.city == 'Philadelphia'|| datum.city == 'Phoenix'|| datum.city == 'San Antonio'|| datum.city == 'San Diego'|| datum.city == 'Dallas'|| datum.city == 'San Jose'|| datum.city == 'Austin'|| datum.city == 'Indianapolis'|| datum.city == 'Jacksonville'|| datum.city == 'San Francisco'|| datum.city == 'Columbus'|| datum.city == 'Charlotte'|| datum.city == 'Fort Worth'|| datum.city == 'Detroit'|| datum.city == 'El Paso'|| datum.city == 'Memphis'|| datum.city == 'Seattle'|| datum.city == 'Denver'|| datum.city == 'Washington'|| datum.city == 'Boston'|| datum.city == 'Nashville-Davidson'|| datum.city == 'Baltimore'|| datum.city == 'Oklahoma City'|| datum.city == 'Louisville/Jefferson County'|| datum.city == 'Portland'|| datum.city == 'Las Vegas'|| datum.city == 'Milwaukee'"
city_filter_3 = "datum.city == 'New York' || datum.city ==  'Los Angeles' || datum.city ==  'Chicago' || datum.city ==  'Houston' || datum.city ==  'Philadelphia' || datum.city ==  'Phoenix' || datum.city ==  'San Antonio' || datum.city ==  'San Diego' || datum.city ==  'Dallas' || datum.city ==  'San Jose' || datum.city ==  'Austin' || datum.city ==  'Indianapolis' || datum.city ==  'Jacksonville' || datum.city ==  'San Francisco' || datum.city ==  'Columbus' || datum.city ==  'Charlotte' || datum.city ==  'Fort Worth' || datum.city ==  'Detroit' || datum.city ==  'El Paso' || datum.city ==  'Memphis' || datum.city ==  'Seattle' || datum.city ==  'Denver' || datum.city ==  'Washington' || datum.city ==  'Boston' || datum.city ==  'Nashville-Davidson' || datum.city ==  'Baltimore' || datum.city ==  'Oklahoma City' || datum.city ==  'Louisville/Jefferson County' || datum.city ==  'Portland' || datum.city ==  'Las Vegas' || datum.city ==  'Milwaukee' || datum.city ==  'Albuquerque' || datum.city ==  'Tucson' || datum.city ==  'Fresno' || datum.city ==  'Sacramento' || datum.city ==  'Long Beach' || datum.city ==  'Kansas City' || datum.city ==  'Mesa' || datum.city ==  'Virginia Beach' || datum.city ==  'Atlanta' || datum.city ==  'Colorado Springs' || datum.city ==  'Omaha' || datum.city ==  'Raleigh' || datum.city ==  'Miami' || datum.city ==  'Oakland' || datum.city ==  'Minneapolis' || datum.city ==  'Tulsa' || datum.city ==  'Cleveland' || datum.city ==  'Wichita' || datum.city ==  'Arlington' || datum.city ==  'New Orleans' || datum.city ==  'Bakersfield' || datum.city ==  'Tampa' || datum.city ==  'Honolulu' || datum.city ==  'Aurora' || datum.city ==  'Anaheim' || datum.city ==  'Santa Ana' || datum.city ==  'St. Louis' || datum.city ==  'Riverside'"
print([c.get('city') for c in cities])

# provinces = {}

# with open('Datafiniti_Pizza_Restaurants_and_the_Pizza_They_Sell_May19.csv') as csv_file:
    
#     f = list(csv.reader(csv_file, delimiter=','))

# with open('pizza_count_by_state.csv', mode='w') as new_file:
#     write_file = csv.writer(new_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
#     columns = 'province,restaurant_count'.split(',')
#     write_file.writerow(columns)
#     i=0
#     for row in f[1:]:
#         if len(row) == 0: continue

#         province = row[-1]
#         res_id = row[0]

#         if province in provinces:
#             entry = provinces.get(province)
#             entry[res_id] = 1
#             provinces[province] = entry

#         else:
#             entry = {}
#             entry[res_id] = 1
#             provinces[province] = entry
            

#     print([k for k,v in sorted(provinces.items(), key=lambda item: len(item[1]), reverse=True)])
#     for key in provinces:
#         item = provinces.get(key)
#         write_file.writerow([key,sum(item.values())])



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
    
    


        



        