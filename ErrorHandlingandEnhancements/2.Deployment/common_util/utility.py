from schema import Schema, And, Use, SchemaError

#Write code here for exception handling

import numbers

def exceptions(data):
    checks_dict = {
     'Numeric input required' : test_if_input_values_are_numeric(data),
     #'Sum input nmeric values' : sum_numeric_values_in_input(data)
     }
    return checks_dict
    
def test_if_input_values_are_numeric(data):
    list_input = [] 
    for u,v in data.items():
        try:
            list_input += [float(v)]
        except:
            list_input += [v]
    numeric_flags = [1 if isinstance(v, numbers.Number) else 0 for v in list_input]
    non_numeric_input_features = []
    count = 0
    for i in numeric_flags:
        if i==0:
            non_numeric_input_features += [list(data.keys())[count]]
        count += 1
    if (len(non_numeric_input_features)==0) & (len(numeric_flags)>0):
        #return True, 'All numeric values in input'
        return True
    else:
        #return False, 'Provide numeric input values for ' + str(non_numeric_input_features)
        return False
    
def sum_numeric_values_in_input(data):
    return sum([v for u,v in data.items()])
    