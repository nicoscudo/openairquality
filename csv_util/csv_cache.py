import csv
import os

class CsvUtil(object):
    def __init__(self):
        self.csv_file = open('cache.csv','w+')
        self.csv_reader = csv.reader(self.csv_file, delimiter=',')
        self.csv_writer = csv.writer(self.csv_file, delimiter=',')
        self.csv_writer.writerow(['City','BC', 'CO', 'NO2', 'O3', 'PM10', 'PM2.5', 'SO2'])
        self.parameters = ['bc', 'co', 'no2', 'o3', 'pm10', 'pm25', 'so2']

    def add_city(self, city):
        l = []
        
        if city:
            l.append(city[0]['city'])
            for parameter in self.parameters:
                p_value=0
 
                for station in city:
                    measurements = station['measurements']
                    p_value += measurements[parameter]['value']
                l.append(str(p_value/len(city)))

        self.csv_writer.writerow(l)

    def get_data(self, city, parameter):
        index = self.parameters.index(parameter.lower())
        if index:
            for row in self.csv_reader:
                if row[0].lower() == city.lower():
                    return row[index+1]
        else:
            return None

    def delete_cache(self):
        os.remove('cache.csv')