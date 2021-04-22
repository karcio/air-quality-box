# air-quality-box

## Pre-requirements
1. Raspberry PI 
1. Enable GPIO in raspberry pi
2. Install dependencies

```
sudo apt-get install python3
sudo apt-get install python3-distutils
sudo apt-get install pigpio python-pigpio python3-pigpio
sudo apt-get install python3-pip
sudo pip3 install RPLCD
sudo pip3 install adafruit-io
```

## Start application
```
python3 app-sensor.py 
```

## R graphs - generate pdf from csv file

```
library(ggplot2)
library("gridExtra")

data=read.csv('file.csv')
time <- as.POSIXct(data$ts, "%Y-%m-%dT%H:%M:%S", tz="IST")

p1 <- ggplot(data, aes(x=time,y=pm25,color = pm25 )) + geom_line() + ggtitle("Readings: PM 2.5") + xlab('Time') + ylab('PM 2.5') + labs(color = 'PM 2.5') + theme_minimal()
p2 <- ggplot(data, aes(x=time,y=pm10,color = pm10 )) + geom_line() + ggtitle("Readings: PM 10") + xlab('Time') + ylab('PM 10') + labs(color = 'PM 10') + theme_minimal()
grid.arrange(p1, p2)

dev.off()
```
