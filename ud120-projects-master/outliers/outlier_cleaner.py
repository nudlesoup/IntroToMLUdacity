#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []
    error=abs(predictions-net_worths)
    a=list(zip(ages,net_worths,error))
    a.sort(key=lambda tup: tup[2])
    k= len(a)*0.9
    cleaned_data=a[0:int(k)]
    #print a
    
    ### your code goes here

    
    return cleaned_data

