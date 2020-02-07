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

def read_jem_csv(fields=None):
    """
    Finds and read jem metadata csv.
    
    Args: 
        directory_name: file directory path of jem matadata file
        jem_file: jem metadata file name

    Returns:
        jem: a pandas dataframe with jem metadata
    """
    global jem  # Define as global to return outside of function
    
    csv_path = "Z:/Patch-Seq/compiled-jem-data/"
    csv_file = "jem_metadata.csv"
    fields=["date", "organism_name", "name", "container", "rigOperator",
            "status", "roi_major", "roi_minor",
            "extraction.postPatch", "extraction.endPipetteR"]
    
    jem = pd.read_csv(csv_path + csv_file, usecols=fields, index_col=["date"])
    LOGGER.info("Read jem metadata csv (date: 2/04/2020)")
    
    return jem

def sort_df(df, r_users=None, m_users=None):
    """
    Args:
        df:
        r_users:
        m_users:
            
    Returns:
        df_2020:
    """
    r_users = ["kristenh", "lindsayn", "ramr", "katherineb", "jessicat"] 
    m_users = ["P1", "P8", "PA", "PE", "PF"]
    #c_users = ["PC"]
    
    df_2020 = df.loc["2020-01-03 10:40:30 -0800":,:]
    LOGGER.info("Date Range: 2020-01-03 to Present 2020")
    
    
    df_2020 = df_2020[df_2020.index.notnull()]
    LOGGER.info("Dropped NaNs from index date column")
    
    df_2020.dropna(subset=["rigOperator", "container"], inplace=True)
    LOGGER.info("Dropped NaNs from rigOperator and container column")
    
    df_2020 = df_2020[df_2020["status"] == "SUCCESS"]
    df_2020 = df_2020[df_2020.rigOperator.str.contains("|".join(r_users))]
    df_2020 = df_2020[df_2020.container.str.contains("|".join(m_users))]
    LOGGER.info("Created dataframe with selected users in container column")
    
    return df_2020


def create_cond_df(df, col_name, cond):
    """"""
    df1 = df[df[col_name] == cond]
    LOGGER.info("Created a conditional dataframe based on jem_2020")
    return df1

def list_counts():
    print()


if __name__ == "__main__":
    JEM = read_jem_csv()
    JEM_2020 = sort_df(JEM)
    MJEM_2020 = create_cond_df(JEM_2020, "organism_name", "Mouse")
    HJEM_2020 = create_cond_df(JEM_2020, "organism_name", "Human")
        