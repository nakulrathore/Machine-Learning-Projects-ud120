#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        clean away the 10% of points that have the largest
        residual errors (different between the prediction
        and the actual net worth)

        return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error)
    """
    
    ### your code goes here
    errors = abs(predictions - net_worths)
    #print predictions[0][0]
    #print net_worths[0][0]    
    #print errors[0][0]
    #using zip
    not_cleaned_data = zip(ages,net_worths,errors)
    #print cleaned_data
    #sorting ,ref: http://stackoverflow.com/questions/13669252/what-is-key-lambda
    not_cleaned_data.sort(key=lambda tup: tup[2])
    #print not_cleaned_data
    #keeping only 90% data means, 0.9*lenth of net_worths
    cleaned_data = not_cleaned_data[:int(len(net_worths)*0.9)]
    #print cleaned_data
    return cleaned_data