import pickle
import pandas as pd

    
def get_plan(type, data):
    if type == 'Individual':
        ind_col = pickle.load(open("app/models/ind_colname.pkl", "rb"))
        model = pickle.load(open("app/models/in_model.pkl", "rb"))
        df = pd.DataFrame(data, index=[0])
        df = df[ind_col]
        pred_plan = model.predict(df)[0]
        # if [df['Are you planning to have kids in the next 12 month'] == 'yes' or df['Are you a nursing mother'] == 'yes']:
        #     note = 'You can also check out the Paediatric or/and Obstetric Plan'
        note = None
    elif type == 'Family':
        fam_col = pickle.load(open("app/models/fam_colname.pkl", "rb"))
        model = pickle.load(open("app/models/fam_model.pkl", "rb"))
        df = pd.DataFrame(data, index=[0])
        df = df[fam_col]
        pred_plan = model.predict(df)[0]
        # if [df['Number of dependents below the age of 18'] > 0 or df['Are you planning to have kids in the next 12 month'] == 'yes' or df['Are you a nursing mother'] == 'yes']:
        #     note = 'You can also check out the Paediatric or/and Obstetric Plan'
        note = None
    else:
        grp_col = pickle.load(open("app/models/grp_colname.pkl", "rb"))
        pred_plan = 'Six'
        note = None
    return pred_plan, note