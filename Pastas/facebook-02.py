from time import sleep
import xlsxwriter
import csv
import pandas as pd

import facebook

graph = facebook.GraphAPI(access_token="EAAVfFbEB8m4BAGFgZCZAY3EQMEI77piZBO2NZCli9qJgCnwZCkaacKK77GWFmtVtBEIDVWVDEKvId383ZCTcKILLqZCR8fS40uSfMBeZCznP0JyYKyz5Yb6TqdLQAwUlvV3EpppdU5RsXK1vZAGqzY28fpsR2qyFxuCAZD")

# Search for places near 1 Hacker Way in Menlo Park, California.
##data={'Restaurant':[],'Rating':[],'Telefono':[],'Zona':[],'Direccion':[], 'Web':[], 'URL':[]}

data={'Restaurant':[],'Rating':[],'Telefono':[],'Zona':[],'Direccion':[]}



##print dir(graph.search)
places = graph.search(type='place', q= 'resto',
                      center='-34.7242956,-58.2817395,13',distance=10000,
                      fields='name,phone, location, rating_count',limit=500)

##places = graph.search(type='place', q= 'quilmes cafe bar',
##                      fields='name,phone, location, rating_count',limit=500)

# Each given id maps to an object the contains the requested fields.
##print places
for place in places['data']:
    data['Restaurant'].append(place['name'])
    data['Rating'].append(place['rating_count'])
    
##    print('%s, %s ' % (place['name'],place['id']))

    if place.has_key('phone'):
        data['Telefono'].append(place['phone'])
    else:
        data['Telefono'].append('No tiene')

    data['Direccion'].append(place['location'].get('street'))
    data['Zona'].append(place['location'].get('city'))  

##    sleep(0.5)
##    print data

df = pd.DataFrame(data)

df=df[['Restaurant','Rating','Telefono','Zona','Direccion']]
##df.transpose()

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('g:/facebook.Quilmes.Resto.xlsx', engine='xlsxwriter')

# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# Close the Pandas Excel writer and output the Excel file.
writer.save()
