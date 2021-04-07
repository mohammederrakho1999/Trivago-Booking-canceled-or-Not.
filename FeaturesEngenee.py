import numpy as np
import pandas as pd





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
    
if 1:
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 0, 'stays_in_weekend_nights_0'] = 0
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 2, 'stays_in_weekend_nights_2'] = 2
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 1, 'stays_in_weekend_nights_1'] = 1
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 4, 'stays_in_weekend_nights_4'] = 4
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 3, 'stays_in_weekend_nights_3'] = 3
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 6, 'stays_in_weekend_nights_6'] = 6
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 5, 'stays_in_weekend_nights_5'] = 5
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 8, 'stays_in_weekend_nights_8'] = 8
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 7, 'stays_in_weekend_nights_7'] = 7
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 9, 'stays_in_weekend_nights_9'] = 9
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 10, 'stays_in_weekend_nights_10'] = 10
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 12, 'stays_in_weekend_nights_12'] = 12
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 13, 'stays_in_weekend_nights_13'] = 13
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 16, 'stays_in_weekend_nights_16'] = 16
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 14, 'stays_in_weekend_nights_14'] = 14
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 18, 'stays_in_weekend_nights_18'] = 18
    Trivago_data.loc[Trivago_data["stays_in_weekend_nights"] == 19, 'stays_in_weekend_nights_19'] = 19
  
    # Drop garbage column
    
    
    col = ["stays_in_weekend_nights_0",
           "stays_in_weekend_nights_2",
           "stays_in_weekend_nights_1",
           "stays_in_weekend_nights_4",
           "stays_in_weekend_nights_3",
           "stays_in_weekend_nights_6",
           "stays_in_weekend_nights_5",
           "stays_in_weekend_nights_8",
           "stays_in_weekend_nights_7",
           "stays_in_weekend_nights_9",
           "stays_in_weekend_nights_10",
           "stays_in_weekend_nights_12",
           "stays_in_weekend_nights_13",
           "stays_in_weekend_nights_16",
           "stays_in_weekend_nights_14",
           "stays_in_weekend_nights_18",
           "stays_in_weekend_nights_19"]
    
    for colname in col:
        Trivago_data[colname] = Trivago_data[colname].fillna(0)
        
    Trivago_data.drop(["stays_in_weekend_nights"],axis = 1,inplace = True)
 

if 1:
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "A") , "class"] = "BBA"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "A") , "class"] = "HBA"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "A") , "class"] = "SCA"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "A") , "class"] = "UA"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "A") , "class"] = "FBA" 
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "D") , "class"] = "BBD"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "D") , "class"] = "HBD"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "D") , "class"] = "SCD"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "D") , "class"] = "UD"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "D") , "class"] = "FBD" 
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "E") , "class"] = "BBE"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "E") , "class"] = "HBE"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "E") , "class"] = "SCE"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "E") , "class"] = "UE"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "E") , "class"] = "FBE"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "F") , "class"] = "BBF"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "F") , "class"] = "HBF"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "F") , "class"] = "SCF"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "F") , "class"] = "UF"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "F") , "class"] = "FBF"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "G") , "class"] = "BBG"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "G") , "class"] = "HBG"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "G") , "class"] = "SCG"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "G") , "class"] = "UG"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "G") , "class"] = "FBG"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "C") , "class"] = "BBC"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "C") , "class"] = "HBC"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "C") , "class"] = "SCC"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "C") , "class"] = "UC"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "C") , "class"] = "FBC"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "B") , "class"] = "BBB"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "B") , "class"] = "HBB"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "B") , "class"] = "SCB"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "B") , "class"] = "UB"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "B") , "class"] = "FBB"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "H") , "class"] = "BBH"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "H") , "class"] = "HBH"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "H") , "class"] = "SCH"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "H") , "class"] = "UH"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "H") , "class"] = "FBH"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "I") , "class"] = "BBI"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "I") , "class"] = "HBI"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "I") , "class"] = "SCI"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "I") , "class"] = "UI"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "I") , "class"] = "FBI"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "K") , "class"] = "BBK"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "K") , "class"] = "HBK"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "K") , "class"] = "SCK"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "K") , "class"] = "UK"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "K") , "class"] = "FBK"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "P") , "class"] = "BBP"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "P") , "class"] = "HBP"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "P") , "class"] = "SCP"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "P") , "class"] = "UP"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "P") , "class"] = "FBP"
    
    Trivago_data.loc[(Trivago_data["meal"] == "BB") & (Trivago_data["assigned_room_type"] == "L") , "class"] = "BBP"
    Trivago_data.loc[(Trivago_data["meal"] == "HB") & (Trivago_data["assigned_room_type"] == "L") , "class"] = "HBP"
    Trivago_data.loc[(Trivago_data["meal"] == "SC") & (Trivago_data["assigned_room_type"] == "L") , "class"] = "SCP"
    Trivago_data.loc[(Trivago_data["meal"] == "Undefined") & (Trivago_data["assigned_room_type"]== "L") , "class"] = "UP"
    Trivago_data.loc[(Trivago_data["meal"] == "FB") & (Trivago_data["assigned_room_type"] == "L") , "class"] = "FBP"
    
    Trivago_data.drop(["meal","assigned_room_type"], axis = 1, inplace = True)
    
if 1:
    Trivago_data["Family-Size"] = Trivago_data["adults"] + Trivago_data["children"] + Trivago_data["babies"]
    Trivago_data['IsAlone'] = 1
    Trivago_data.loc[Trivago_data['Family-Size'] > 1, "IsAlone"] = 0
    # drop garbage column
    Trivago_data.drop(["adults","children","babies"],axis = 1, inplace = True)
    
Trivago_data.to_csv("cleanedData.csv")
