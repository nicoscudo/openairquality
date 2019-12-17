Git ## Implementation of an Air Quality data fetching library


In this repository you can find a file named ```openairquality.py``` that implements the ```get_quality(city, parameter)``` function. It queries the [OpenAQ](https://openaq.org) website to fetch the value of some air quality parameter in a world city. This function is used in the ```main.py``` file to obtain the value of air quality parameters (bc, co, no2, o3, pm10, pm25, so2).
It will  give you results similar to the following: 

```
$ python3 main.py nic ad -a 
This is a program that takes from OpenAQ website the value of air quality in some city around the world
Available parameter: bc, co, no2, o3, pm10, pm25, so2
Insert the city London
Insert parameter pm10
6.2105263157894735
```
In order to start using the program you will need to sing-in in. To do that you need to put username and password when you run the program. 

```
$ python3 main.py nic ad -a 

```

'-a' to sing-in, '-p' to log-in. You can also use verbose to change the verbosity of the answers. 



Note that the project requires the ```argparse```, ```os```, ```json```, ```requests``` and ```csv``` module to run. [OpenAQ](https://openaq.org/) is a project that receives air quality data from people and serves them on-line. The APIs are documented in a [API documentation page](https://docs.openaq.org/). 