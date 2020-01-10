import csv
import os

class CsvUtil(object):

    ''' 
    CsvUtil class does the following:
    - creates a csv file 
    - writes city information on that file
    - reads that information from that file 
    - deletes that file 
    '''

    def __init__(self):
        self.csv_file = open('cache.csv', 'w+')
        self.csv_reader = csv.reader(self.csv_file, delimiter=',')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',')
        self.csv_writer.writerow(['City', 'BC', 'CO', 'NO2', 'O3',
                                  'PM10', 'PM2.5', 'SO2'])
        self.parameters = ['bc', 'co', 'no2', 'o3', 'pm10', 'pm25', 'so2']

    def add_city(self, city):
        city_city = []

        # Checking if the request is not empty
        if city:
            '''
            For each parameter we take the mean of the measurement of each station 
            in the given city. 
            As a first thing we select a parameter. We then iterate through all stations
            in the city and we add its value for that parameter to all previous 
            values. Finally we take the average.
            We repeat the process for all other parameters.
            '''
            city_city.append(city[0]['city'])
            for parameter in self.parameters:
                p_value = 0

                for station in city:
                    measurements = station['measurements']
                    for n in measurements:
                        if n['parameter'] == parameter:
                            p_value += n['value']
                city_city.append(str(p_value / len(city)))

            self.csv_writer.writerow(city_city)
            self.csv_file.flush()


    # Getting a parameter value given a city 
    def get_data(self, city, parameter):
        
        # Checking input parameters exists  
        if parameter in self.parameters:
            index = self.parameters.index(parameter.lower())
        else:
            index = None

        if index:
            # Setting reader to the start of the file
            self.csv_file.seek(0)
            for row in self.csv_reader:
                if row[0].lower() == city.lower():
                    return row[index + 1]
        else:
            return None

    def delete_cache(self):
        os.remove('cache.csv')

    def close(self):
        self.csv_file.close()
