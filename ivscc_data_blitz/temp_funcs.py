# -*- coding: utf-8 -*-
"""temp_funcs.py: Temp functions python script

__author__ = "Ramkumar Rajanbabu"
__date__ = "3.16.2020"
__status__ = "Temporary"
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


def merge_dataframes(left_df, right_df, left_col, right_col, join_how):
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
                        how = join_how)
    LOGGER.info("Merged two pandas dataframe into one dataframe")
    return merge_df


def drop_cols(df, drop_col):
    """Drop unnessary columns from dataframe
    Args:
        df: a pandas dataframe
        drop_col(lst): column names to drop from dataframe
    Return:
        df: a pandas dataframe without certain columns
    """
    LOGGER.info(f"Dropped columns: {drop_col}")
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
    LOGGER.info(f"Dropped NaNs from these columns: {drop_na_col}")
    df.dropna(subset=drop_na_col, inplace=True)
    return df


def filter_date_range(df, date_col):
    """Filters and sorts the date column by specific date range in the dataframe.
    Args:
        df: a pandas dataframe
        date_col(string): column name with date information
    Returns:
        df: a pandas dataframe with a filtered date range
    """
    start_date = "2017-01-01"
    end_date = "2021-12-31"

    mask = (df[date_col] > start_date) & (df[date_col] <= end_date)
    df = df.loc[mask]
    df.sort_values([date_col], inplace=True)
    LOGGER.info(f"Filtered dataframe: {start_date} - {end_date}")
    return df


def filter_df(df, fil_col, fil_val):
    """Creates a dataframe based on values from a single column
     Args:
        df: a pandas dataframe
        fil_col(string): column name from dataframe
        fil_val(string): values to restrict dataframe by
    Return:
        df: a pandas dataframe created by values from a single column
    """
    df = df[df[fil_col] == fil_val]
    LOGGER.info(f"Filtered dataframe based on {fil_col} == {fil_val}")
    return df


def create_container_col(df, col_label):
    """Creates container label based on rig operator names
    Args:
        df: a pandas dataframe
        col_label(string): a column name with the container label information
    Return:
        df: a pandas dataframe with a new column with container labels
    """
    rig_user_dictionary ={"kristenh" : "P1", 
                          "rustym": "P2", 
                          "lindsayn": "P8", 
                          "lisak": "P9",
                          "ramr": "PA", 
                          "dijonh": "PB",
                          "katherineb": "PE", 
                          "jessicat": "PF"} 

    df["patch_container_label"] = df[col_label].map(rig_user_dictionary)
    LOGGER.info("Created a patch_container_label column to show(ex.'PA')")
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
    LOGGER.info(f"Created a conditional dataframe based on {col} containing {val}")
    return df


def create_container_df(df, container_col):
    """Creates container label based on original container column
    Args:
        df: a pandas dataframe
        container_col: a column name with the container label information
    Return:
        df: a pandas dataframe with a new column with container labels
    """
    df["collaborator_label"] = df[container_col].str[0:2]
    return df
