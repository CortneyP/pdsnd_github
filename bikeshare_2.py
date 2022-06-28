import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago','new york city','washington']

MONTHS = ['january','february','march','april','may','june']

DAYS = ['monday', 'tuesday','wednesday','thursday','friday', 'saturday','sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
               city = input('Would you like to see date for Chicago, New York City or Washington? \n> ').lower()
               if city in CITIES:
                    break


    # get user input for month (all, january, february, ... , june)
    while True:
                month = input('What month would you like to filter by? or type \'all\' to apply no month filter. \n (please note january, february, march, april, may, june are the only available months to select from) \n> ').lower()
                if month in MONTHS:
                    break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
                day = input('What day would you like to filter by? or type \'all\' to apply no day filter. \n (e.g. all, monday, tuesday, wednesday, thursday, friday, saturday, sunday) \n> ').lower()
                if day in DAYS:
                    break

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
   # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
        month = MONTHS.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: " , common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day is: " ,common_day)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: " ,str(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most common start station is: ",common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most common end station is: ",common_end_station)

    # display most frequent combination of start station and end station trip
    frequent_combination = (df['Start Station'] + df['End Station']).mode()[0]
    print("The most frequent combination of start station and end station is: " ,frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time is: ",total_travel_time)

    #  display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("The mean travel time is: ",mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("The count for user types is:\n", user_types)

    # Display counts of gender
    try:
        gender_type = df['Gender'].value_counts(dropna=False)
        print("The count for gender types is:\n", gender_type)
    except:
        print("There is no 'Gender' column in this file")

    # Display earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print("The earliest birth year is: \n",earliest_year)
        print("The most recent birth year is: \n",recent_year)
        print("The most common year of birth is: \n",common_year)
    except:
        print("There is no 'Birth Year' column in this file")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Prompt to ask user if they would like to see 5 rows of raw data and continue to see +5 rows of data each time their input is 'yes'."""
    print(df.head())
    add_raw_data = 0
    while True:
            raw_data = input("Would you like to see the next 5 rows of data? Answer with 'yes' or 'no'.\n")
            if raw_data.lower() != 'yes':
                 return
            add_raw_data = add_raw_data +5
            print(df.iloc[add_raw_data:add_raw_data+5])

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

""" The following github repo was used as a reference point in building code for this project -  https://github.com/beingjainparas/Udacity-Explore_US_Bikeshare_Data/blob/master/bikeshare_2.py"""
