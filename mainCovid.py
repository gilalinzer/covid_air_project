from getCounties import *
from covidData import *


# returns a set of county objects
def make_covid_objects():
    # create an airdata object for each us county
    objects = {}
    counties = get_county_list()
    for county in counties:
        # create a covid data object
        title = covidData(county)
        # add to our set of objects
        objects[county] = title
    print('made covid objects')
    return objects

class covidDataCombiner(object):
    def __init__(self):
        self.county_objects = make_covid_objects()


    def loadData(self):
        header = True
        with open('covid_data.csv') as file:
            for line in file:
                if line.strip() != "date,county,state,fips,cases,deaths":
                    a = line.split(",")
                    # assign all the fields
                    try:
                        date, county, state, fips, cases, deaths = a
                    except:
                        print(f'{line} is bad data')
                    # find correct object to use
                    try:
                        obj = self.county_objects[county.upper() + ' ' + state.upper()]
                    except:
                        pass
                    obj.fillLine(cases,deaths)
            file.close()
            return True

    # calculate death rate for each county object
    def load_death_rates(self):
        for v in self.county_objects.values():
            v.calculate_death_rate()
        return True
# done



