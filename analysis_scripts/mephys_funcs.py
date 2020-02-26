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
