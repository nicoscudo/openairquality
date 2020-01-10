# OpenAirquality project

## Introducing the project 
Considering that one of the main issues we are facing is Air Pollution, that has a great impact on our health, we decided to offer a little help to the cause. 
 
## The purpose of our project 
This program send requests to OpenAQ web site in order to obtain information about the major cities in the world. 

## The implementation of our project 
Note that the project requires the ```argparse```, ```os```, ```json```, ```requests``` and ```csv``` modules to run. 

Our project queries the [OpenAQ](https://openaq.org) website to fetch the value of some air quality parameter in a specific world city. The parameters that are made available by the OpenAQ initiative  are: BC, CO, NO2, O3, PM10, PM2.5, SO2. 
The results of the query are saved in a csv file that works as cache and finally showed to the user.

## Example 
```
$ python3 main.py nic ad -a 
This is a program that takes from OpenAQ website the value of air quality in some city around the world
Available parameter: bc, co, no2, o3, pm10, pm25, so2
Insert the city London
Insert parameter pm10
6.2105263157894735
```

## Getting started 
In order to start using the program you will need to sing-in in. To do that you need to put username and password when you run the program. 

Use -a to add a new user
```
$ python3 main.py nic ad -a 

```
Use -p to log-in to an existing user
```
$ python3 main.py nic ad -p 
```

Use -d to delete the database
```
$ python3 main.py nic ad -d
```

Use -v to activate verbosity
Once verbosity is activated more information about the request are given
```
$ python3 main.py nic ad -a -v
```

## Testing 
To test that the project behaves correctly, the user can run:
```
$ python3 -m unites -v -b tests/test.py

```

## Additional information
[OpenAQ](https://openaq.org/) is a project that receives air quality data from people and serves them on-line. The APIs are documented in a [API documentation page](https://docs.openaq.org/). 