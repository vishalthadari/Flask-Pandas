import pandas as pd
import numpy as np

def childDataset(data):

    PC = data[data['Accepted Compound ID'].str.endswith(' PC')==True]
    LPC = data[data['Accepted Compound ID'].str.endswith('LPC')==True]
    Plasmalogen = data[data['Accepted Compound ID'].str.endswith('plasmalogen')==True]

    PC.to_excel("./Results/result1.xlsx")
    LPC.to_excel("./Results/result2.xlsx")
    Plasmalogen.to_excel("./Results/result3.xlsx")
    return True



def retentionTime(data):
    data['Retention Time Roundoff (in mins)']=np.rint(data['Retention time (min)'])
    data.to_excel("./Results/result4.xlsx")
    return True


def mean(data):
    data['Retention Time Roundoff (in mins)']=np.rint(data['Retention time (min)'])
    task3_df = data.groupby('Retention Time Roundoff (in mins)').mean()
    columns = ['m/z', 'Retention time (min)']
    task3_df = task3_df.drop(columns, axis=1)
    task3_df.reset_index(inplace=True)

    task3_df.to_excel("./Results/result5.xlsx")
    return True
