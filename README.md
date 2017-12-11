# chart_success.py
A script to calculate the chart success of an artist, writer or producer on a billboard chart over the years. 

The simple metric calculated is as follows: A no. 1 song is valued as 100, a no. 2 song is valued as 99, etc., a no. 100 song is valued as 1. All song values of each chart of each year are added together.

This is a improved version of [calculate-chart-success](https://github.com/3ngthrust/calculate-chart-success) with better accuracy. Here not only song titles are compared, but also the artist names. Therefore two lists are necessary instead of only one in the previous version.

Usage
-----
1. Go to the discography of the person you want to evaluate on Wikipedia. Select the whole table with the songs (Ctrl+C). Copy the table to libre office (Ctrl+V). Make shure each song has its corresponding cell with the name of the artist. Split the artist cells horizontaly if necessary. Select the column with the song titles in libre office. Copy them in libre and paste them into an an editor. Remove empty lines (Regex to find the lines: ^\n) and ". The result should be a list like the example 'Max_Martin_Songs_10-12-17' here. Do the same with the artist collum the result could look like 'Max_Martin_Artists_10-12-17'. Make shure every song is unique in the lists, duplicates are not removed.  
Hint: Use a shortcut in libre office to split the artist cells: Libre Office -> Tools -> Customize -> Keyboard-Tab -> Select Key Combinaton (e.g. F4) -> Select Table, Split Cells -> Click Modify -> Ok 

2. Create a database of charts with the function 'create_chart_database(chart_name, min_year, database_filename)'. See the docstring of the function in chart_success.py for more information.

3. Use the function 'calculate_success(database_filename, songlist_filename, artistlist_filename)' to calculate the metric for each year. See the docstring of the function in chart_success.py for more information.

3. Plot the results with the function plot_data(max_value, min_year, max_year, title, data). See the docstring of the function in chart_success.py for more information.

Dependencies
------------
This script uses [billboard.py](https://github.com/guoguo12/billboard-charts) by [guoguo12](https://github.com/guoguo12) and [fuzzywuzzy](https://github.com/seatgeek/fuzzywuzzy).

Example
-------
All the songs Max Martin contributed to (according to his Wikipedia discography from 10.12.17) are listed in 'Max_Martin_Songs_10-12-17' and the corresponding artists in 'Max_Martin_Artists_10-12-17'. The result is shown below.

![](https://raw.githubusercontent.com/3ngthrust/calculate-chart-success-2/master/Chart_Success_of_Max_Martin.png)

The added values for this example can be seen in 'Max_Martin_Output_10-12-17'. The output seems accurate. Of course errors are still possible since song titles and artist names can be similar.

