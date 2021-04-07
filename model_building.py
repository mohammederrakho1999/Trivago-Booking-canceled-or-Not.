import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import auc, classification_report, roc_auc_score
from sklearn.model_selection import train_test_split
import xgboost as xgb
from utils import tobinary as bi




for col_cat in ['hotel','country','reserved_room_type','deposit_type',"company","customer_type","reservation_status"]:
        newcols = bi.toBinary(col_cat, Trivago_data)
        Trivago_data.drop([col_cat], axis = 1, inplace = True)
    # drop missing values       
    Trivago_data.dropna(inplace = True)
    
Trivago_data.drop(["arrival_date_month","reservation_status_date"], axis = 1, inplace = True)

bi.toBinary("class",Trivago_data)
bi.toBinary("market_segments",Trivago_data)
Trivago_data.drop(["market_segments","class"],axis = 1,inplace = True) 



# TARGET VARIABLES AND FEATURES
Target_Variable = Trivago_data["is_canceled"]
Predictor_Variables = Trivago_data.drop(["is_canceled"], axis = 1, inplace = False)

# SPLITTING THE DATA
x_train, x_test, y_train, y_test = train_test_split(Predictor_Variables, Target_Variable ,test_size = .3,random_state = 0)

#MODELING
model=xgb.XGBClassifier()
model.fit(x_train, y_train)

# Make predictions
y_pred = model.predict_proba(x_test)[:, 1]

# Check the auc score of the model
print(f'RandomForest AUC score on the X_test is: {roc_auc_score(y_test, y_pred)}\n')
print(classification_report(y_test, [1 if x >= 0.5 else 0 for x in y_pred]))
