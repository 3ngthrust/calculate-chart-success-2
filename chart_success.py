#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: 3ngthrust
"""
from collections import OrderedDict
from fuzzywuzzy import fuzz
import matplotlib.pyplot as plt
import billboard
import time
import pickle


def song_value(songtitle, artist, chart):                                         
# Run through one billboard chart objekt and return the "value" of the song 
# with the specified Title and Artist in this chart.
# The returned value for a no. 1 song is 100, the value of a no. 2 song is 99,
# etc., the value of a no. 100 song is 1. If the song is not on the chart 0 is
# returend.
# Example: song_value('Song Title', 'Artistname', chart)
    
    for chart_pos, song in enumerate(chart):                              
        if (fuzz.partial_ratio(str.lower(songtitle), str.lower(song.title)) >= 90) and (fuzz.partial_ratio(artist, song.artist) >= 90):
            return 100-chart_pos
        
    return 0
   
    
def add_value_to_year(year, value, value_per_year):
# Adds a value to a year in the dict value_per_year

    if year in value_per_year:
        value_per_year[year] = value_per_year[year] + value
    else:
        value_per_year[year] = value


def create_chart_database(chart_name, min_year, database_filename):
# Get all charts from the billboard chart with chart_name up to and including
# the charts from min_year and save the database as database_filename.pkl
# Example: create_chart_database('hot-100', 1993, 'hot-100-1993')

    chart = billboard.ChartData(chart_name)
    year = int(chart.date[:4])
    chart_database = OrderedDict()
     
    while year >= min_year:     
        # Output to give feedback on the progress
        print(chart.date)        
        print(year)
        
        # Include in Database
        chart_database[chart.date] = chart

        # Get older chart
        older_chart = billboard.ChartData('hot-100', date=chart.previousDate)
        while len(older_chart) != 100:
            print('Could not download the chart, trying agian in 2 seconds.')
            time.sleep(2)
            older_chart = billboard.ChartData('hot-100', date=chart.previousDate)
            
        chart = older_chart
        year = int(chart.date[:4])

    # Save database
    pickle.dump(chart_database , open(database_filename+".pkl", "wb"))
    
    
def plot_data(max_value, min_year, max_year, title, data):
# Plot the data calculated with the function 'calculate success'.
# Example: plot_data(25000, 1995, 2017, 'Chart Success of Max Martin', data)

    years = list(range(min_year, max_year+1, 1))
    values = []
    for y in years:
        if y not in data:
            values.append(0)
        else:
            values.append(data[y])

    fig = plt.figure(1)
    plt.plot(years, values, marker='o', label="Max Martin") 
    
    plt.ylim(None, max_value)
    #plt.grid(True)
    plt.title(title)
    plt.xlabel('Year')
    plt.ylabel('Chart Success (Accumulated Song Values)')
    #plt.legend(loc='upper left')
    
    fig.savefig(title + '.png', dpi = 300)
    
    plt.show()
    
    
def calculate_success(database_filename, songlist_filename, artistlist_filename):
# Adds the song values of the songs in songlist_filename with the corresponding
# artists in artistlist_filename in the charts in database_filename together
# Example: calculate_success('database_filename,pkl', 'songlist_filename', 'artistlist_filename')
    
    # Import chart_database
    chart_database = pickle.load(open(database_filename, "rb"))  
    
    # Import songlist and artistlist
    songlist = open(songlist_filename).read().split('\n')
    artistlist = open(artistlist_filename).read().split('\n')
                  
    value_per_year = dict()
    
    for chart_date, chart in chart_database.items():
        
        print(chart_date + ":" + "\n")
        
        year = int(chart_date[:4])
        
        for i, song in enumerate(songlist):   
            value = song_value(song, artistlist[i], chart)
        
            if value:
                add_value_to_year(year, value, value_per_year)
                print('"' + song + '"' + ' by ' + artistlist[i] + ' ' + str(value) + "\n")
                
    print(value_per_year)
    return value_per_year
    
        
if __name__ == "__main__":
    
    # create_chart_database('hot-100', 1993, 'hot-100-1993')
    calculate_success('../hot-100-1993.pkl', 'Max_Martin_Songs_06-12-17' , 'Max_Martin_Artists_06-12-17')
