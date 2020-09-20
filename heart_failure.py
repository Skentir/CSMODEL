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

    def get_month(self, data, dropped):
        """ This function returns the month, which parameter is given by days

        Arguments:
            data {Series} - a column Series
        Returns:
            String value of month
        """

        # Declaring an array for saving the string using numpy
        result = []

        # Iterate over the elements and Checking what 
        # month does the time belong in the 2015
        # We need to + 2 since we dropped 2 rows
        total_size = len(data)

        for x in range(total_size) :
            if x in dropped:
                x = x + 1

            if data.loc[x].item() >= 1 and data.loc[x].item() <= 31:
                result.append("Jan")
            elif data.loc[x].item() >= 32 and data.loc[x].item() <= 59:
                result.append("Feb")
            elif data.loc[x].item() >= 60 and data.loc[x].item() <= 90:
                result.append("March")
            elif data.loc[x].item() >= 91 and data.loc[x].item() <= 120:
                result.append("April")
            elif data.loc[x].item() >= 121 and data.loc[x].item() <= 151:
                result.append("May")
            elif data.loc[x].item() >= 152 and data.loc[x].item() <= 181:
                result.append("June")
            elif data.loc[x].item() >= 182 and data.loc[x].item() <= 212:
                result.append("July")
            elif data.loc[x].item() >= 213 and data.loc[x].item() <= 244:
                result.append("Aug")
            elif data.loc[x].item() >= 245 and data.loc[x].item() <= 274:
                result.append("Sept")
            elif data.loc[x].item() >= 275 and data.loc[x].item() <= 305:
                result.append("Oct")
            elif data.loc[x].item() >= 306 and data.loc[x].item() <= 335:
                result.append("Nov")
            elif data.loc[x].item() >= 336 and data.loc[x].item() <= 366:
                result.append("Dec")

        return pd.Series(result)