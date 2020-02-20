"""
Created on 2/13/2020
By: Ramkumar Rajanbabu

Purpose: Create a count tracker for all mouse regions, human acute, 
human culture recordings that have a patched cell container label. Then, return
a file that outputs the results for all users.
"""

import pandas as pd
import csv
import logging
from tracker_funcs import read_jem, read_ephys, read_shiny, \
sort_df, create_cond_df, create_region_col, merge_dfs, choice

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

csv_path = "C:/Users/ramr/Documents/Github/analysis_projects/csv/"
excel_path = "C:/Users/ramr/Documents/Github/analysis_projects/excel/"


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


if __name__ == "__main__":
    main()
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