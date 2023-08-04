import pickle
import matplotlib.pyplot as plt
import random
import math
from getCounties import get_county_list
covid_file = open('covid_data.obj', 'rb')
covid_data = pickle.load(covid_file)
covid_file.close()

air_file = open('air_data.obj', 'rb')
air_data = pickle.load(air_file)
air_file.close()
covid_data = covid_data.county_objects
air_data = air_data.county_objects

county_list = get_county_list()

# get data objects for each county for each year
x = []
y = []
for county in county_list:
        cd = covid_data[county]
        ad = air_data[county]
        newX = ad.OzoneAverage
        # only plot counties that actually had air data
        if newX>0.01 and cd.deathRate>0.001:
            x.append(newX)
            y.append(cd.deathRate)
# now plot for the year
colors = [random.randint(1,10) for i in range(len(x))]
areas = [math.pi * 4 for i in range(len(x))]
plt.scatter(x,y,c=colors,s=areas,alpha=0.5)
plt.xlabel("PM 2.5 average")
plt.ylabel("Covid death rate")
plt.title(f' Correlation between air pollutants and covid death rate')
plt.show()


#now we can write scripts with the data