import numpy as np
import pandas as pd




def make_dataset():

    if 1:
        
        Trivago_data.loc[Trivago_data["market_segment"] == "Complementary","market_segments"] = "CO"
        Trivago_data.loc[Trivago_data["market_segment"] == "Aviation","market_segments"] = "A"
        Trivago_data.loc[Trivago_data["market_segment"] == "Online TA" ,"market_segments"] = "TA"
        Trivago_data.loc[Trivago_data["distribution_channel"] == "TA/TO","market_segments"] = "TA/TO"
        Trivago_data.loc[Trivago_data["market_segment"] == "Groups","market_segments"] = "G"
        Trivago_data.loc[Trivago_data["distribution_channel"] == "Direct","market_segments"] = "D"
        Trivago_data.loc[Trivago_data["distribution_channel"] == "Corporate","market_segments"] = "C"
        Trivago_data.loc[Trivago_data["distribution_channel"] == "Undefined","market_segments"] = "U"
        Trivago_data.loc[Trivago_data["distribution_channel"] == "GDS","market_segments"] = "GD" 
        Trivago_data.loc[Trivago_data['market_segments'].isnull(), 'market_segments'] = "U"
    
    
        Trivago_data.drop(["market_segment","distribution_channel"], axis = 1,inplace = True)