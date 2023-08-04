# get a list of all states and counties from our dataset
def get_county_list():
    counties = set()
    header = True
    with open('air_data.csv', 'r') as file:
        for line in file:
            if header:
                header = False
            else:
                if line:
                    line = line.replace('\n','')
                    line = line.replace('"', "")
                    a = line.split(",")
                    # unpack the list
                    county,state = a[1],a[0]
                    counties.add(county.upper()+ ' '+state.upper())
    file.close()
    return counties

print(get_county_list())



