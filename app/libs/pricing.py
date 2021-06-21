import pandas as pd

def get_price(plan, grp_size = "01 to 100"):
    df_price = pd.read_excel("app/data/pricing.xlsx",keep_default_na=False)
    df_price.set_index("GROUP SIZE", inplace=True)
    price = df_price.loc[grp_size][plan]
    return price
