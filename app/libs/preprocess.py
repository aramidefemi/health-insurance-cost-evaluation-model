import pickle
import json


def prep(data):
    # data = json.load(response)
    ind_col = pickle.load(open("app/models/ind_colname.pkl", "rb"))
    fam_col = pickle.load(open("app/models/fam_colname.pkl", "rb"))
    grp_col = pickle.load(open("app/models/grp_colname.pkl", "rb"))
    if data['undefined'] == 'Individual':
        df = { key:value for key,value in data.items() if key in ind_col}
        int_col = ['how long have you been married', 'Duration of time spent in the hospital in days']
        for key in int_col:
            if df[key] == None:
                df[key] = -1
            else:
                df[key] = int(df[key])
        for key,value in df.items():
            if key not in int_col and df[key] == None:
                df[key] = 'n/a'
    elif data['undefined'] == 'Family':
        df = { key:value for key,value in data.items() if key in fam_col}
        int_col = ["Number of dependents", "Number of dependents below the age of 18", 'Duration of time spent in the hospital in days']
        for key in int_col:
            if df[key] == None:
                df[key] = -1
            else:
                df[key] = int(df[key])
        for key,value in df.items():
            if key not in int_col and df[key] == None:
                df[key] = 'n/a'
    else:
        df = { key:value for key,value in data.items() if key in grp_col}
    return data['undefined'], df