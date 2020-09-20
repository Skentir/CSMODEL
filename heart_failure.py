import numpy as np
import pandas as pd

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

    def get_month(self, data):
        """ This function returns the month, which parameter is given by days

        Arguments:
            data {Series} - a column Series
        Returns:
            String value of month
        """

        # Declaring an array for saving the string using numpy
        result = np.empty(len(data),dtype=object)

        # Iterate over the elements and Checking what 
        # month does the time belong in the 2015
        for x in range(len(data)):
            if(data[x] >= 1 and data[x] <= 31):
                result[x] = "Jan"
            elif (data[x] >= 32 and data[x] <= 59):
                result[x] = "Feb"
            elif (data[x] >= 60 and data[x] <= 90):
                result[x] = "March"
            elif (data[x] >= 91 and data[x] <= 120):
                result[x] = "April"
            elif (data[x] >= 121 and data[x] <= 151):
                result[x] = "May"
            elif (data[x] >= 152 and data[x] <= 181):
                result[x] = "June"
            elif (data[x] >= 182 and data[x] <= 212):
                result[x] = "July"
            elif (data[x] >= 213 and data[x] <= 244):
                result[x] = "Aug"
            elif (data[x] >= 245 and data[x] <= 274):
                result[x] = "Sept"
            elif (data[x] >= 275 and data[x] <= 305):
                result[x] = "Oct"
            elif (data[x] >= 306 and data[x] <= 335):
                result[x] = "Nov"
            elif (data[x] >= 336 and data[x] <= 366):
                result[x] = "Dec"
        return result