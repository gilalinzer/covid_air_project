from datetime import datetime
# each county will be broken down into a covid data object with two dictionaries
class covidData(object):
    def __init__(self,county):
        self.county = county
        # dictionary for total cases and deaths there are for each year
        # for each year - index 0 is the total followed by each month starting at jan being index 1
        self.numCases = 0
        self.numDeaths = 0
        # once all that data is calculated this dictionary will be used to calculate a monthly death rate
        self.deathRate = 0

    # will be called for each line in the data
    def fillLine(self,cases,deaths):
        # find the correct date
        # increment total cases
        self.numCases += int(cases)

        # now fill in the num deaths
        try:
            deaths = int(deaths)
        except:
            # cut out newline
            deaths = 0
        self.numDeaths += deaths

    #  to be calculated only AFTER the entire file has been entered
    # modifies death rate dictionary and does not return anything
    def calculate_death_rate(self):
            cases = self.numCases
            deaths= self.numDeaths
            # avoid divide by zero error
            if cases:
                    rate = float(deaths) / float(cases)
                    self.deathRate = rate
            else:
                # there were no cases so store float zero - prevents division by zero
                self.deathRate = 0.0








