# Udacity Project: Post Your Work on GitHub
## Date created
February 26, 2024

## Project Title
Explore US Bikeshare Data

## Description
In this project, I used Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. I wrote code to import the data and answer interesting questions about it by computing descriptive statistics. I also wrote a script that takes in raw input to create an interactive experience in the terminal to present these statistics.

### Project Details
#### Bike Share Data
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. Bicycle-sharing systems allow users to rent bicycles on a very short-term basis for a price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd like to just go for a ride. Regardless, each bike can serve several users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return bicycles. These technologies also provide a wealth of data that can be used to explore how these bike-sharing systems are used.

#### The Datasets
Randomly selected data for the first six months of 2017 are provided for all three cities. All three of the data files contain the same core six (6) columns:
- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)  

The Chicago and New York City files also have the following two columns:
- Gender
- Birth Year

#### Statistics Computed
1. Popular times of travel (i.e., occurs most often in the start time)
- most common month
- most common day of week
- most common hour of day

2. Popular stations and trip
- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration
- total travel time
- average travel time

4. User info
- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)


## Files used
- chicago.csv
- new_york_city.csv
- washington.csv

## Credits
Udacity repository:  
https://github.com/udacity/pdsnd_github/  
Chicago dataset:  
https://divvybikes.com/system-data  
New York City dataset:  
https://citibikenyc.com/system-data  
Washington dataset:  
https://capitalbikeshare.com/system-data
