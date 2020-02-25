"""
Created on 2/07/2020
By: Ramkumar Rajanbabu

Script written by: Agata

Purpose:
-Functions used to open LIMS, make a query and then close LIMS
"""

import pandas as pd
import pg8000


def _connect(user="limsreader", host="limsdb2", database="lims2", password="limsro", port=5432):
    """
    Args:
        user:
        host:
        database:
        password:
        port:
    Returns:
        conn, conn.cursor()
    """
    conn = pg8000.connect(user=user, host=host, database=database, password=password, port=port)
    return conn, conn.cursor()


def _select(cursor, query):
    """
    Args:
        cursor:
        query:
    Returns:
    """
    cursor.execute(query)
    columns = [ d[0] for d in cursor.description ]
    return [ dict(zip(columns, c)) for c in cursor.fetchall() ]


def limsquery(query, user="limsreader", host="limsdb2", database="lims2", password="limsro", port=5432):
    """A function that takes a string containing a SQL query, connects to the LIMS database 
    and outputs the result.
    Args:
    Returns:
    """
    conn, cursor = _connect(user, host, database, password, port)
    try:
        results = _select(cursor, query)
    finally:
        
        #THESE ARE IMPORTANT!!!!!!
        #Every query needs to be closed when done
        cursor.close()             
        conn.close()
    return results


#this last function will take our query results and put them in a dataframe so that they are easy to work with
def get_lims_dataframe(query):
    """Return a dataframe with lims query
    Args:
    Returns:
    """
    result = limsquery(query)
    try:
        data_df = pd.DataFrame(data=result, columns=result[0].keys())
    except IndexError:
        print("Could not find results for your query.")
        data_df = pd.DataFrame()
    return data_df
