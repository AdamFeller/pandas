# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 11:23:01 2017

@author: fella
"""
import pandas
import pyodbc 

#----------------------------------------------------------------------------------
cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=BDPRADA;"
                      "Database=ZAP_BETA;"
                      "Trusted_Connection=yes;")

sql='SELECT * FROM fella.Swaption_Compare'

#----------------------------------------------------------------------------------

data = pandas.read_sql(sql, cnxn)

