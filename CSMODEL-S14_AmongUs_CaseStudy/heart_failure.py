import numpy as np
import pandas as pd
import math

class HeartFailure(object):

    def __init__(self):
        """ Class constructor for HeartFailure.
        """

    def check_if_int(self, data):
        """ This function determines whether a column Series contains
        values that are all integers or not. Depending on the answer,
        the return type could change.
        
        Arguments:
            data {Series} - a column Series
        Returns:
            There are two options that can be returned:
                1. Boolean - True or False (If data is all integers).
                2. Boolean and Vector Array (If data contains at least 
                    one non-integer value).
        """
        # Create a temporary blank list.
        temp = []
        
        # Iterate over the elements in data and check whether they are an 
        # integer using the modulo logic. If the data is not an integer,
        # add the index of that element to the list called temp.
        for x in range(len(data)):
            if data[x] % 1 != 0:
                temp.append(x)
        
        # Assume that all values are integers.
        is_int = True
        
        # Check whether the count of temp list exceeds 0. If it does,
        # then it means that there is an element that is not an integer.
        # Then convert the temp list into an array.
        if len(temp) > 0:
            is_int = False
            index = np.array(temp)
        
        # This conditional statement will return only a Boolean value if
        # data is all integers. Otherwise, it will also return an array of 
        # the indeces where there are non-integer values.
        if is_int == True:
            return is_int
        else:
            return [is_int, index]
        
    def drop_outliers(self, data, field):
        """
        """
        
        distance = 1.5 * (np.percentile(data[field], 75) - np.percentile(data[field], 25))
        
        data.drop(data[data[field] > distance + np.percentile(data[field], 75)].index, inplace=True)
        data.drop(data[data[field] < np.percentile(data[field], 25) - distance].index, inplace=True)
        
    def get_mean_difference(self, data):
        """ This function gets the difference between the means of two
        groups.
        
        Arguments:
            data {DataFrame}
        Returns:
            means {Series} - contains the difference of means for the
                groups.
        """
        # Create a temporary blank list.
        temp = []

        # Get the number of columns in the DataFrame.
        col = data.shape[1]

        # Iterate the number of columns and only select the column having
        # the data for means. Since there is only two groups, the subtraction
        # will be hardcoded. There are two possible scenarios where the first
        # mean is larger than the second mean or vise versa. When the difference
        # is acquired, add it to the temporary list.
        for x in range(col):
            if x % 2 == 0:
                if data.loc[0][x] >= data.loc[1][x]:
                    diff = data.loc[0][x] - data.loc[1][x]
                    temp.append(diff)
                elif data.loc[0][x] < data.loc[1][x]: 
                    diff = data.loc[1][x] - data.loc[0][x]
                    temp.append(diff)

        # Convert the list to a Series.
        means = pd.Series(temp)

        return means
    
    def get_month(self, data):
        """ This function returns the month given by days.
        
        Arguments:
            series {Series} - a column Series
            dropped {list}
        Returns:
            result {Series} - a column Series
        """

        # Create two empty list.
        month = []
        
        # Get the length of data.
        total_size = len(data)

        # Iterate over the elements and check what month does the time 
        # belong in the 2015.          
        for x in range(total_size):
            if data.values[x] >= 1 and data.values[x] <= 31:
                month.append(1)
            elif data.values[x] >= 32 and data.values[x] <= 58:
                month.append(2)
            elif data.values[x] >= 59 and data.values[x] <= 89:
                month.append(3)
            elif data.values[x] >= 90 and data.values[x] <= 119:
                month.append(4)
            elif data.values[x] >= 120 and data.values[x] <= 150:
                month.append(5)
            elif data.values[x] >= 151 and data.values[x] <= 180:
                month.append(6)
            elif data.values[x] >= 181 and data.values[x] <= 211:
                month.append(7)
            elif data.values[x] >= 212 and data.values[x] <= 243:
                month.append(8)
            elif data.values[x] >= 244 and data.values[x] <= 273:
                month.append(9)
            elif data.values[x] >= 274 and data.values[x] <= 304:
                month.append(10)
            elif data.values[x] >= 305 and data.values[x] <= 334:
                month.append(11)
            elif data.values[x] >= 335 and data.values[x] <= 365:
                month.append(12)

        # Name the series as 'month' and convert list to a Series.
        month = pd.Series(month)

        return month
