import pandas as pd

def gen_fil(df, col, cond):
    '''
    Filters the column with a certain condition
    df: dataframe
    col: column
    cond: condition
    '''
    filtered = df[df[col] == cond]
    return filtered

def gen_cat(df, col):
    '''
    Assigns astype to the column
    df: dataframe
    col: column
    '''    
    category = df[col].astype('category')
    return category

def P_total(df, P_num):
    '''
    Counts number of Lims tube id based on P# as number of cells
    df = dataframe
    count() = counts number    
    Prints cell_count 
    '''
    user = df[df['Lims tube id'].str.contains(P_num)]
    user_count = user['Lims tube id'].count()
    print("Total cells:", user_count)