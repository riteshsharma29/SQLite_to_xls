#!/usr/bin/python
# -*- coding: utf-8 -*-

import pandas as pd
from pandas import ExcelWriter
import pandas as pd
import sys,os
from openpyxl import load_workbook
import sqlite3
from openpyxl import __version__

currentpath = os.getcwd()
if os.path.isfile("log.txt"):
	os.remove("log.txt")

	
if len(sys.argv) < 2:
	os.system('echo SQlite db file name not passed as first parameter >> log.txt')
	os.system('echo SQlite db file not present with the tool >> log.txt')		
	os.system('')
	os.system('')		
	os.system('echo Keep SQlite db file with the tool and pass it as a first parameter >> log.txt')		
	os.system('echo Please Try again >> log.txt')
	sys.exit()
elif len(sys.argv) < 3:
	os.system('echo Second parameter not passed >> log.txt')
	os.system('echo Second parameter needs to be either view OR table >> log.txt')		
	os.system('')
	os.system('')		
	os.system('echo Pass Second parameter as view OR table >> log.txt')		
	os.system('echo Please Try again >> log.txt')
	sys.exit()
	
if not os.path.isfile(sys.argv[1]):	
	os.system('echo SQlite db passed as first parameter not found >> log.txt')
	os.system('echo Please keep SQlite db with the tool ..... try again >> log.txt')		
	os.system('')
	os.system('')	
	sys.exit()		
	
dbtbltype = sys.argv[2]

if os.path.isfile(dbtbltype + '.xlsx'):	
	os.system('echo export xlsx found >> log.txt')
	os.system('echo export in progress ... please wait .... till next message appears >> log.txt')		
	os.system('')
	os.system('')		
if not os.path.isfile(dbtbltype + '.xlsx'):	
	os.system('echo export xlsx not found >> log.txt')
	os.system('echo Please keep table.xlsx if second parameter is table & Please keep view.xlsx if second parameter is view ..... try again >> log.txt')		
	os.system('')
	os.system('')	
	sys.exit()	




		
con = sqlite3.connect(sys.argv[1])
cursor = con.cursor()
cursor.execute("SELECT name from sqlite_master WHERE type ='" + dbtbltype + "';")
tblviews = (cursor.fetchall())
#print tblviews

def pandas_dbexcel(viewname,con):

	book = load_workbook(dbtbltype + '.xlsx')
	writer = ExcelWriter(dbtbltype + '.xlsx', engine='openpyxl') 	
	writer.book = book
	writer.sheets = dict((ws.title, ws) for ws in book.worksheets)

	df = pd.read_sql_query("SELECT * from " + viewname, con)

	#verify that result of SQL query is stored in the dataframe
	#print(df)

	df.to_excel(writer,sheet_name=viewname,encoding='utf8')

	writer.save()

for tblvno,tblview in enumerate(tblviews):

	viewname = str(tblview).replace("(u'","").replace("',)","")

	pandas_dbexcel(viewname,con)
	
if __name__ == "__main__":
	os.system('echo Database views / tables exported into export xlsx file found based on the second parameter passed>> log.txt')

		
	
