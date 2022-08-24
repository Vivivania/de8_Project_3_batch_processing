#!/usr/bin/python3

import os
import json
import sqlparse
import psycopg2

import pandas as pd
import numpy as np

import connection #import connection.py
import conn_warehouse #import conn_warehouse.py
if __name__ == '__main__':
    print(f"[INFO] Service ETL is Starting .....")
    conn_dwh, engine_dwh  = conn_warehouse.conn()
    cursor_dwh = conn_dwh.cursor()
    #mennyambung ke data warehouse digitalskola

    conf = connection.config('postgresql')
    conn, engine = connection.psql_conn(conf)
    cursor = conn.cursor()
    #menyambung ke database digitalskola

    path_query = os.getcwd()+'/query/'
    query1 = sqlparse.format(
        open(
            path_query+'query.sql','r'
            ).read(), strip_comments=True).strip()
    #membaca query join : query1.sql

    query2 = sqlparse.format(
        open(
            path_query+'query2.sql','r'
            ).read(), strip_comments=True).strip()
    #membaca query join : query2.sql

    query3 = sqlparse.format(
        open(
            path_query+'query3.sql','r'
            ).read(), strip_comments=True).strip()
    #membaca query join : query3.sql

    query_dwh = sqlparse.format(
        open(
            path_query+'dwh_design.sql','r'
            ).read(), strip_comments=True).strip()
    #membaca query create table : dwh_design.sql

    try:
        print(f"[INFO] Service ETL is Running .....")

        cursor_dwh.execute(query_dwh)
        conn_dwh.commit()
        #execute query dwh_design di table dwh_digitalskola

        df1 = pd.read_sql(query1, engine)
        df2 = pd.read_sql(query2, engine)
        df3 = pd.read_sql(query3, engine)
        #membaca sebagai dataframe

        df1.to_sql('dim_orders', engine_dwh, if_exists='append', index=False)
        df2.to_sql('dim_users', engine_dwh, if_exists='append', index=False)
        df3.to_sql('fact_orders', engine_dwh, if_exists='append', index=False)

        print(f"[INFO] Service ETL is Success .....")
        #jika sukses, table dim_orders, dim_users, dan fact_orders di database dwh_digitalskola akan terisi
    except:
        print(f"[INFO] Service ETL is Failed .....")

    

    