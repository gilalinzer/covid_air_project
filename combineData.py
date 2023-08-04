
from mainCovid import covidDataCombiner
from mainAir import airDataCombiner
import pickle


def get_objects():
    a = covidDataCombiner()
    if a.loadData():
        print('covid data has been loaded')
    if a.load_death_rates():
        print('covid death rates have been calculated')

    b = airDataCombiner()
    if b.loadData():
        print('air data has been loaded')
    if b.load_averages():
        print('air data averages have been calculated')
    return a,b
covid_data, air_data = get_objects()


# now we are going to save our created data objects into new files by "pickling" them

fileObj = open('covid_data.obj', 'wb')
pickle.dump(covid_data,fileObj)
print("covid objects have been saved to file")
fileObj.close()

air_file = open('air_data.obj','wb')
pickle.dump(air_data,air_file)
print("air objects have been saved to file")
air_file.close()

