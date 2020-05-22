import pandas as pd
import numpy as np

df_init = pd.read_excel(input("Enter the 1st excel file name(with .xlsx extension): "))
df_info = pd.read_excel(input("Enter the second excel file name(with .xlsx extension): "))

df_init.columns = df_init.columns.str.strip()
df_info.columns = df_info.columns.str.strip()

x = str(input("Enter the column name from 1st excel doc. :"))

y = str(input("Enter the column name from the 2nd excel doc. for matching with col with 1st excel sheet: "))
z = str(input("Enter the column name from 2nd excel sheet whose value you want to be pulled out: "))

df_init.rename(columns={x:y},inplace=True)

#print(df_init.columns)
#print(df_info.columns)

df_3 = pd.merge(df_init,df_info[[y,z]], on = y,how ='left')
df_init.rename(columns={y:x},inplace=True)

df_3=df_3.replace(np.nan,' ',regex=True)

df_3.to_excel("output.xlsx",index=False)
