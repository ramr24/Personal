# -*- coding: utf-8 -*-
"""

Created on Mon Feb 24 12:17:22 2020

@title: mephys_funcs.py
@author: Ramkumar Rajanbabu
"""

import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def read_file(path, fields=None):
    """Reads file in as pandas dataframe by using pd.read_csv
    Args:
        path: path of file location
    Return:
        df: a pandas dataframe
    """
    global df
    df = pd.read_csv(path, usecols=fields)
    LOGGER.info("Read file in as a pandas dataframe")
    return df


def merge_dataframes(left_df, right_df, left_col, right_col):
    """Merges two dataframes together into one dataframe
    Args:
        left_df: a pandas dataframe on the left
        right_df: a pandas dataframe on the right
        left_col: a column from the left dataframe
        right_col: a column from the right dataframe
    Return:
        merge_df: a merged pandas dataframe
    """
    merge_df = pd.merge(left = left_df,
                        right = right_df,
                        left_on = left_col,
                        right_on = right_col, 
                        how = "inner")
    LOGGER.info("Merged two pandas dataframe into one dataframe")
    return merge_df


def filter_date(df, date_col):
    """Filters and sorts the date column by specific date range
    Args:
        df: a pandas dataframe
        date_col(str): a column name with the date information
    Return:
        df: a pandas dataframe with a filtered date range
    """
    df.set_index([date_col], inplace=True)
    df = df.loc["2020-01-03 10:40:30 -0800":,:]
    df.reset_index(inplace=True)
    LOGGER.info("Sorted date to only display 2020 data")
    return df


def drop_cols(df, drop_col):
    """Drop unnessary columns from dataframe
    Args:
        df: a pandas dataframe
        drop_col(lst): column names to drop from dataframe
    Return:
        df: a pandas dataframe without certain columns
    """
    LOGGER.info("Dropped columns: %s", drop_col)
    df.drop(columns=drop_col, inplace=True)
    return df


def drop_nans(df, drop_na_col):
    """Drop Nans from selected columns
    Args:
        df: a pandas dataframe
        drop_na_col(lst): column names to drop NaNs from 
    Return:
        df: a pandas dataframe without NaNs in certain columns
    """
    LOGGER.info("Dropped NaNs from these columns: %s", drop_na_col)
    df.dropna(subset=drop_na_col, inplace=True)
    return df


def create_cond_df(df, col, val):
    """Creates a dataframe based on values from a single column
     Args:
        df: a pandas dataframe
        col(string): column name from dataframe
        val(list): values to restrict dataframe by
    Return:
        df: a pandas dataframe created by values from a single column
    """
    df = df[df[col].str.contains("|".join(val))]
    LOGGER.info("Created a conditional dataframe based on a list of values")
    return df


def create_container_df(df, container_col):
    """Creates container label based on original container column
    Args:
        df: a pandas dataframe
        container_col: a column name with the container label information
    Return:
        df: a pandas dataframe with a new column with container labels
    """
    df["container_label"] = df[container_col].str[0:2]
    LOGGER.info("Created a container_label column to show(ex.'PA')")
    return df






def date_return(df):
    df = df.reset_index()
    start_date = df["date"].iloc[0][0:10]
    end_date = df["date"].iloc[-1][0:10]
    df = df.set_index(["date"])
    logger.info("Created date")
    return df, start_date, end_date



def print_counts():
    """Prints counts of dataframes"""
    #print(f"Date Range: {start_date} to {end_date}")
    print(f"Overall Total count: {jem_2020.container.count()}")
    print()
    print(f"Mouse Total count: {mjem_2020.organism_name.count()}")
    print(f"-RSPd count: {rspd.organism_name.count()}")
    print(f"-RSPv count: {rspv.organism_name.count()}")
    print(f"-SSp count: {ssp.organism_name.count()}")
    print(f"-ORB count: {orb.organism_name.count()}")
    print(f"-CTXsp count: {ctxsp.organism_name.count()}")
    print(f"-MOp count: {mop.organism_name.count()}")
    print(f"-MOs count: {mos.organism_name.count()}")
    print(f"-HY count: {hy.organism_name.count()}")
    print(f"-HIP count: {hip.organism_name.count()}")
    print(f"-VISP count: {visp.organism_name.count()}")
    print()
    print(f"Human Total count: {hjem_2020.organism_name.count()}")
    print(f"-Human Acute count: {hajem_2020.organism_name.count()}")
    print(f"-Human Culture count: {hcjem_2020.organism_name.count()}")

def main():
    jem_2020 = read_jem()
    logger.info("Imported jem_metadata.csv as a dataframe")
    jem_2020 = choice()
    
    jem_2020["p_container"] = jem_2020.container.str[0:4]
    logger.info("Creating column to check p_container")
    jem_2020.p_container.unique()
    
    #jem_2020 = date_return(jem_2020)
    #print(start_date)

    mjem_2020 = create_cond_df(jem_2020, "organism_name", "Mouse")
    hjem_2020 = create_cond_df(jem_2020, "organism_name", "Human")
    hajem_2020 = hjem_2020[hjem_2020["p_container"] != "PCS4"]
    hcjem_2020 = create_cond_df(hjem_2020, "p_container", "PCS4")

    mjem_2020 = create_region_col(mjem_2020)
    rspd = create_cond_df(mjem_2020, "roi_major", "RSPd")
    rspv = create_cond_df(mjem_2020, "roi_major", "RSPv")
    ssp = create_cond_df(mjem_2020, "roi_major", "SSp")
    orb = create_cond_df(mjem_2020, "roi_major", "ORB")
    ctxsp = create_cond_df(mjem_2020, "roi_major", "CTXsp")
    mop = create_cond_df(mjem_2020, "roi_major", "MOp")
    mos = create_cond_df(mjem_2020, "roi_major", "MOs")
    hy = create_cond_df(mjem_2020, "roi_major", "HY")
    hip = create_cond_df(mjem_2020, "roi_major", "HIP")
    visp = create_cond_df(mjem_2020, "roi_major", "VISP")
    logger.info("Created region pandas dataframes")
    print_counts()



def create_region_col(df):
    """"""
    df["new_region"] = "default_value"
    LOGGER.info("Created a new column(new_region) with default_value")
    
    c_region = ["RSPd", "RSPv", "SSp"] 
    s_region = ["MOs", "MOp", "ORB", "CTXsp"]
    o_region = ["HY", "HIP"]
    v_region = ["VISp"]
    
    df["new_region"][df.roi_major.str.contains("|".join(c_region))] = "coronal_region"
    df["new_region"][df.roi_major.str.contains("|".join(s_region))] = "sagittal_region"
    df["new_region"][df.roi_major.str.contains("|".join(o_region))] = "other_region"
    df["new_region"][df.roi_major.str.contains("|".join(v_region))] = "v1_region"
    LOGGER.info("Filled in new_region column with region labels")
    return df


def choice():
    """"""
    r_users = ["kristenh", "lindsayn", "ramr", "katherineb", "jessicat"]
    r_user = ["ramr"]
    
    global entry

    print("These are all user options: kristenh, lindsayn, ramr, katherineb, jessicat")
    entry = input("Enter single user name or all users (a):")
    if entry == "a":
        jem_2020 = sort_df(jem, r_users)
    elif entry == "kristenh":
        jem_2020 = sort_df(jem, r_users[0])
    elif entry == "lindsayn":
        jem_2020 = sort_df(jem, r_users[1])
    elif entry == "ramr":
        jem_2020 = sort_df(jem, r_users[2])
    elif entry == "katherineb":
        jem_2020 = sort_df(jem, r_users[3])
    elif entry == "jessicat":
        jem_2020 = sort_df(jem, r_users[4])
    else: 
        print("Please choose between option 'a' or 'r'.")
    LOGGER.info("Sorted jem by date range: 1/03/2020 - present")
    return jem_2020

#if __name__ == "__main__":
    
        """jem = read_jem()
    logger.info("Imported jem_metadata.csv as a dataframe")
    jem_2020 = choice()
    
    jem_2020["p_container"] = jem_2020.container.str[0:4]
    logger.info("Creating column to check p_container")
    jem_2020.p_container.unique()
    
    jem_2020 = jem_2020.reset_index()
    start_date = jem_2020["date"].iloc[0][0:10]
    end_date = jem_2020["date"].iloc[-1][0:10]
    jem_2020 = jem_2020.set_index(["date"])
    
    mjem_2020 = create_cond_df(jem_2020, "organism_name", "Mouse")
    hjem_2020 = create_cond_df(jem_2020, "organism_name", "Human")
    hajem_2020 = hjem_2020[hjem_2020["p_container"] != "PCS4"]
    hcjem_2020 = create_cond_df(hjem_2020, "p_container", "PCS4")

    mjem_2020 = create_region_col(mjem_2020)
    rspd = create_cond_df(mjem_2020, "roi_major", "RSPd")
    rspv = create_cond_df(mjem_2020, "roi_major", "RSPv")
    ssp = create_cond_df(mjem_2020, "roi_major", "SSp")
    orb = create_cond_df(mjem_2020, "roi_major", "ORB")
    ctxsp = create_cond_df(mjem_2020, "roi_major", "CTXsp")
    mop = create_cond_df(mjem_2020, "roi_major", "MOp")
    mos = create_cond_df(mjem_2020, "roi_major", "MOs")
    hy = create_cond_df(mjem_2020, "roi_major", "HY")
    hip = create_cond_df(mjem_2020, "roi_major", "HIP")
    visp = create_cond_df(mjem_2020, "roi_major", "VISP")
    logger.info("Created region pandas dataframes")
    
    print_counts()"""
    