"""
time:2023/12/12
contributors:Liujian 2103, Yang Shihao
Refrigeration and cryogenic engineering
"""

import pandas as pd
import numpy as np

df = pd.read_excel("Thermocouple.xlsx", header=None)

print("T型热电偶的分度表范围-220~400℃")

def query(values, type="C"):
    results = []  #stores results
    
    if type == "E":
        print("centigrade_degree:")
    else:
        print("elec_potential:")
    
    for value in values:
        if type == "C":
            x = df.iloc[:,1].values  # temp
            y = df.iloc[:,0].values  # elec_potential
            result = np.interp(value, x, y)
            results.append(result)
            print(f"{result:.3f}")
            
        elif type == "E":
            x = df.iloc[:,0].values  # elec_potential
            y = df.iloc[:,1].values  # temp
            result = np.interp(value, x, y)
            results.append(result)
            print(f"{result:.3f}")
            
        elif type == "K":
            value = value - 273.15   # transform Kelvin_degree to centigrade_degree
            x = df.iloc[:,1].values  # temp
            y = df.iloc[:,0].values  # elec_potential
            result = np.interp(value, x, y)
            results.append(result)
            print(f"{result:.3f}")
            
        else:
            print("Data type error")
    
    
    # writing to result.xlsx
    df_result = pd.DataFrame({'Result': results})
    df_result.to_excel(r'E:\Users\DELL\Desktop\result.xlsx', index=False)


data_type = input("data type（C/K/E）：")
result = [float(i) for i in input("data：").split(',')]
query(result, data_type)
