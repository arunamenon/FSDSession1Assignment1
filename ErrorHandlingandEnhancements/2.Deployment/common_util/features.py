import math


#Write a command to create 5 the feature that create log(log_Peatal_Width)
#Will need to retrain the model on 5 features and create new model.pkl file

def process(data):
    feature_engineering_dict = {
     'Add log of petal length' : 1
    }
    
    for u,v in feature_engineering_dict.items():
        if v==1:
            data = add_log_petal_len(data)
    return data
def add_log_petal_len(data):
    if float(data['Petal_Length'])>0:
        data['log(Petal_length)'] = math.log(float(data['Petal_Length']))
    else:
        data['log(Petal_length)'] = 0
    return data