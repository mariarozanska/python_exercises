'''This exercise is Part 4 of 4 of the birthday data exercise series.
In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
In this exercise, use the bokeh Python library to plot a histogram of which months 
the scientists have birthdays in! Because it would take a long time for you to input 
the months of various scientists, you can use my scientist birthday JSON file. 
Just parse out the months and draw your histogram.'''

import zad34
import zad35
from bokeh.plotting import figure, output_file, show
from bokeh.palettes import Spectral6
from bokeh.models import ColumnDataSource
import calendar

def plotHistMonth(month_dict):
    output_file("plotmonth.html")
    x_categories = [calendar.month_name[i] for i in range(1, 13)]
    months = list(month_dict.keys())
    counts = list(month_dict.values())
    source = ColumnDataSource(data=dict(months=months, counts=counts, color=Spectral6))
    p = figure(x_range=x_categories, 
               plot_width=800, plot_height=400, 
               title='The histogram of which months the people have birthdays in',
               )
    p.vbar(x='months', top='counts', width=0.5, color='color', source=source)
    show(p)

if __name__ == '__main__':  
    birthdayDict = zad34.loadBirthdayDict()
    monthDict = zad35.getMonthDict(birthdayDict)
    plotHistMonth(monthDict)