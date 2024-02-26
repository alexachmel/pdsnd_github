import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    while True:
        txt = '\nWould you like to filter the data for Chicago, New York, or Washington?\n'
        city = input(txt)
        city = city.strip().lower()
        if city in ['chicago', 'new york', 'washington']:
            msg = f'Looks like you want to hear about {city.title()}! If this is not true, restart the program now!'
            print(msg)
            city = 'new york city' if city == 'new york' else city
            break

    while True:
        txt = '\nWould you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n'
        time_filter = input(txt)
        time_filter = time_filter.strip().lower()
        if time_filter not in ['month', 'day', 'none', 'all']:
            continue
            
        if time_filter in ['month', 'day']:
            print(f'We will make sure to filter by {time_filter}!')
        elif time_filter in ['none', 'all']:
            print('We will not apply a time filter!')
        break
    
    if time_filter == 'month':
        while True:
            txt = '\nWhich month? January, February, March, April, May, or June? Please type out the full month name.\n'
            month = input(txt)
            month = month.strip().lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                break
    else:
        month = 'all'

    if time_filter == 'day':
        while True:
            txt = '\nWhich day? Please type a day Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday.\n'
            day = input(txt)
            day = day.strip().lower()
            if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
    else:
        day = 'all'

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print('Just one moment... loading the data')

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['Month'] = df['Start Time'].dt.month
    df['Day'] = df['Start Time'].dt.day_name().str.lower()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['Month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Day'] == day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    month = df['Month'].mode()[0]
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[month - 1].title()
    print(f'Most popular month for traveling: {popular_month}')

    # Display the most common day of week
    popular_day = df['Day'].mode()[0]
    print(f'Most popular day for traveling: {popular_day.title()}')

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print(f'Most popular hour of the day to start your travels: {popular_hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'Most popular start station: {popular_start_station}')

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'Most popular end station: {popular_end_station}')

    # Display most frequent combination of start station and end station trip
    popular_trip = df[['Start Station', 'End Station']].apply(tuple, axis=1).mode()[0]
    print('Most popular trip from start to end:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_duration = df['Trip Duration'].sum()
    print(f'Total travel time: {total_duration}')

    # Display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print(f'Average travel time: {mean_duration}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    users = df['User Type'].value_counts()
    print('What is the breakdown of users?')
    print(users)

    # Display counts of gender
    if 'Gender' not in df.columns:
        print('\nNo gender data to share.')
    else:
        gender = df['Gender'].value_counts()
        print('\nWhat is the breakdown of gender?')
        print(gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('\nNo birth year data to share.')
    else:
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        popular_year = df['Birth Year'].mode()[0]
        print(f'\nEarliest year of birth: {earliest_year:.0f}')
        print(f'Most recent year of birth: {recent_year:.0f}')
        print(f'Most common year of birth: {popular_year:.0f}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
def display_data(df):
    """Displays some rows of data upon request."""
    
    answer = input('\nDo you want to see 5 rows of data? Enter yes or no.\n')
    answer = answer.strip().lower()
    
    start_loc = 0
    while answer == 'yes':
        if start_loc >= df.shape[0]:
            break
        end_loc = min(start_loc + 5, df.shape[0])
        print(df.iloc[start_loc:end_loc])
        start_loc += 5
        answer = input('\nDo you want to see the next 5 rows of data? Enter yes or no\n')
    
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
