import csv
rows=[]
with open("Data.csv") as f:
  csvreader=csv.reader(f)
  for row in csvreader:
    rows.append(row)

headers=rows[0]
planetDataRows=rows[1:]
# print(headers)
# print(planetDataRows)

headers[0]="row_num"
# print(headers)

solarSystemPlanetCount={}
for planetData in planetDataRows:
  if solarSystemPlanetCount.get(planetData[11]):
    solarSystemPlanetCount[planetData[11]]+=1

  else:
    solarSystemPlanetCount[planetData[11]]=1

maxsolarSystem=max(solarSystemPlanetCount,
key=solarSystemPlanetCount.get)
# print("solar System {} has maximum planets {} out of all the solar system discovered so far".format(maxsolarSystem,solarSystemPlanetCount[maxsolarSystem]))

koi=[]
for planetData in planetDataRows:
  if maxsolarSystem==planetData[11]:
    koi.append(planetData)
# print(len(koi))
# print(koi)    

tempDataPlanetRows=list(planetDataRows)
for planetData in tempDataPlanetRows:
  planetMass=planetData[3]
  if planetMass.lower()=="unknown":
    planetDataRows.remove(planetData)
    continue

  else:
    planetMassvalue=planetMass.split(" ")[0]
    planetMassref=planetMass.split(" ")[1]
    if(planetMassref=="Jupiters"):
      planetMassvalue=float(planetMassvalue)*317.6
      planetData[3]=planetMassvalue
   
  planetRadius=planetData[7]
  if planetRadius.lower()=="unknown":
    planetDataRows.remove(planetData)
    continue

  else:
    planetRadiusvalue=planetRadius.split(" ")[0]
    planetRadiusref=planetRadius.split(" ")[1]
    if(planetRadiusref=="Jupiter"):
      planetRadiusvalue=float(planetRadiusvalue)*11.2
      planetData[7]=planetRadiusvalue
# print(len(planetDataRows))

koiPlanets=[]
for planetData in planetDataRows:
  if maxsolarSystem==planetData[11]:
    koiPlanets.append(planetData)
# print(len(koiPlanets))
# print(koiPlanets)        

import plotly.express as px
koiPlanetMasses=[]
koiPlanetNames=[]
for planetData in koiPlanets:
    koiPlanetMasses.append(planetData[3])
    koiPlanetNames.appned(planetData[1])

fig=px.bar(x=koiPlanetNames,y=koiPlanetMasses)
fig.show()    

