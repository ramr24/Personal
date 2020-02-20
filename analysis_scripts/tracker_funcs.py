"""
Created on 2/06/2020
By: Ramkumar Rajanbabu

Purpose:
-Read csvs
"""

import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def read_jem(file_path=None, fields=None):
    """"""
    global jem
    file_path = "Z:/Patch-Seq/compiled-jem-data/jem_metadata.csv"
    fields=["date", "organism_name", "name", "container", "rigOperator",
            "status", "roi_major", "roi_minor",
            "extraction.postPatch", "extraction.endPipetteR"]

    jem = pd.read_csv(file_path, usecols=fields, index_col=["date"])
    LOGGER.info("Read jem metadata csv as a pandas dataframe")
    return jem


def read_ephys(csv_path=None, fields=None):
    """"""
    global ephys
    file_path = "C:/Users/ramr/Documents/Github/analysis_projects/csv/mephys_features.csv"
    fields=["b'patched_cell_container'", "b'vrest'", "b'sag'", "b'tau'",
            "b'upstroke_downstroke_ratio_long_square'", "b'latency'", "b'f_i_curve_slope'"]
    
    ephys = pd.read_csv(file_path, usecols=fields)
    LOGGER.info("Read mouse ephys features csv as a pandas dataframe")
    return ephys


def read_shiny(file_path=None, fields=None):
    """"""
    global shiny
    file_path = "//allen/programs/celltypes/workgroups/rnaseqanalysis/shiny/patch_seq/star/mouse_patchseq_VISp_current/mapping.df.with.bp.40.lastmap.csv"
    #fields = ["sample_id", "subclass_label", "cluster_label"]
    shiny = pd.read_csv(file_path, usecols=fields)
    LOGGER.info("Read shiny link as a pandas dataframe")
    return shiny


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


def merge_dfs(df1, df2):
    """"""
    df1.reset_index(inplace=True)
    df3 = pd.merge(left = df1,
                   right = df2,
                   left_on = "container",
                   right_on = "b'patched_cell_container'",
                   how = "inner")
    df3.drop(columns=["b'patched_cell_container'"], inplace=True)
    df3.dropna(subset=["b'vrest'", "b'sag'", "b'tau'", 
                       "b'upstroke_downstroke_ratio_long_square'",
                       "b'latency'", "b'f_i_curve_slope'"], inplace=True) #22 NAns
    df3.set_index(["date"], inplace=True)
    return df3


def sort_df(df, r_users):
    """"""
    #r_users = ["kristenh", "lindsayn", "ramr", "katherineb", "jessicat"] 
    #m_users = ["P1", "P8", "PA", "PE", "PF"]
    #df1 = df1[df1.container.str.contains("|".join(m_users))]
    #c_users = ["PC"]
    
    df1 = df.loc["2020-01-03 10:40:30 -0800":,:]
    
    df1 = df1[df1.index.notnull()]
    df1.dropna(subset=["rigOperator", "container"], inplace=True)
    LOGGER.info("Dropped NaNs from index date, rigOperator and container column")
    
    df1 = df1[df1["status"] == "SUCCESS"]
    df1 = df1[df1.rigOperator.str.contains("|".join(r_users))]
    LOGGER.info("Created dataframe with selected users in container column")
    return df1


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


def run_all_user():
	r_users = ["kristenh", "lindsayn", "ramr", "katherineb", "jessicat"]
