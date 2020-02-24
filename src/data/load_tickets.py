import pandas as pd
from .utils import read_sql
from skbox.connectors.bigquery import BigQuery
from skbox.connectors.teradata import Teradata
import os
import sys
import time
import logging as log

#PATH = ""
PATH = './data/'

SOURCE_DICT = {'ticket_line': PATH + 'load_ligtickets.sql',
               'remise': PATH + 'load_remises.sql'
               }               
class LoadTickets():
    """
    """
    def __init__(self, data_source, year, typtrn, codtypv):
        self.data_source = data_source
        sql_req = read_sql(SOURCE_DICT[self.data_source])
        sql_req = sql_req.replace('\n', ' ').replace('\r', ' ').replace('var_year', year)
        sql_req = sql_req.replace('var_typtrn', typtrn).replace('var_codtypv', codtypv)
        bq = BigQuery()
        df_BQ = bq.select(sql_req)
        self.dataframe = df_BQ


class LoadRemise():
    """
    """
    def __init__(self, data_source, year):
        self.data_source = data_source
        sql_req = read_sql(SOURCE_DICT[self.data_source])
        sql_req = sql_req.replace('\n', ' ').replace('\r', ' ').replace('var_year', year)
        bq = BigQuery()
        df_BQ = bq.select(sql_req)
        self.dataframe = df_BQ
