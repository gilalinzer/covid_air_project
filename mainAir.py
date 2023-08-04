from getCounties import *
from airData import *


# returns a set of county objects
def make_air_objects():
    # create an airdata object for each us county
    objects = {}
    counties = get_county_list()
    for county in counties:
        # create a data object
        title = airData(county)
        # add to our set of objects
        objects[county] = title
    print('made air objects')
    return objects

class airDataCombiner(object):
    def __init__(self):
        self.county_objects = make_air_objects()

    def loadData(self):
        header = True
        # used to skip the header line
        with open('air_data.csv') as file:
            for line in file:
                if header:
                    header = False
                else:
                    line = line.replace('"', "")
                    a = line.split(",")
                    # if there is actual data in the list
                    # assign each value in the line to a variable
                    stateName, countyName, stateCode, countyCode, d, AQI, category, parameter, site, nSites = a

                    # find correct object to use
                    try:
                        obj = self.county_objects[countyName.upper() + ' ' + stateName.upper()]
                    except:
                        print(f'invalid county {countyName+stateName}')
                    # update the object for this line
                    obj.fillVals(AQI,parameter)
            file.close()
            return True

    # calculate average for each county object
    def load_averages(self):
        for c in self.county_objects.values():
            c.calculateAverages()
        return True





