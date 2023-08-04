import re
import csv
from datetime import datetime


...

# each county will be an airData object with dictionaries keeping track of it's data
class airData(object):
    def __init__(self,county):
        self.county = county
        # keep track of total values there are for each pollutant
        self.OzoneVals = 0
        self.NO2Vals = 0
        self.COVals = 0
        self.PM10Vals = 0
        self.PM25Vals = 0
        # number of values for each
        self.OzoneNum = 0
        self.NO2Num = 0
        self.CONum = 0
        self.PM10Num = 0
        self.PM25Num = 0
        # computed averages
        self.OzoneAverage = 0
        self.NO2Average = 0
        self.COAverage= 0
        self.PM10Average = 0
        self.PM25Average = 0

    # mutatator that updates the val and nums dictionaries for a line but does not return anything
    def fillVals(self, AQI, parameter):
        # update the number of values so we can calculate average
        if parameter == "PM2.5":
            self.PM25Vals+= float(AQI)
            self.PM25Num+=1
        elif parameter== 'Ozone':
            self.OzoneVals += float(AQI)
            self.OzoneNum += 1
        elif parameter== 'NO2':
            self.NO2Vals += float(AQI)
            self.NO2Num += 1
        elif parameter== 'CO':
            self.COVals += float(AQI)
            self.CONum += 1
        elif parameter== 'PM10':
            self.PM10Vals += float(AQI)
            self.PM10Num += 1

        return True


    # this method is ONLY meant to be called once the other dictionaries have been filled
    # with the data from all lines of the file

    def calculateAverages(self):
        # calculate averages for each pollutant type
        for parameter in ["PM2.5","Ozone","NO2","CO","PM10"]:
            if parameter == "PM2.5":
                if self.PM25Num:
                    self.PM25Average = float(self.PM25Vals)/float(self.PM25Num)
                else:
                    self.PM25Average =0.0
            elif parameter == "Ozone":
                if self.OzoneNum:
                    self.OzoneAverage = float(self.OzoneVals)/float(self.OzoneNum)
                else:
                    self.OzoneAverage =0.0
            elif parameter == "NO2":
                if self.NO2Num:
                    self.NO2Average = float(self.NO2Vals)/float(self.NO2Num)
                else:
                    self.NO2Average =0.0
            elif parameter == "CO":
                if self.CONum:
                    self.COAverage = float(self.COVals)/float(self.CONum)
                else:
                    self.COAverage =0.0
            elif parameter == "PM10":
                if self.PM10Num:
                    self.PM10Average = float(self.PM10Vals)/float(self.PM10Num)
                else:
                    self.PM10Average =0.0


        return True















