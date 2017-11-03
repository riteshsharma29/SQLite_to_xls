# SQLite_to_xls
#Python Pandas based SQlite database to excel export tool

TASK / PURPOSE : Python script for Automating export of all tables from SQlite database into excel workbook.

Language : Python

USAGE :

Keep excel workbook and the python script togather in the same path.

Command :

./pd_sqlite_eg <SQlite Databasename> table

example if eg.db then from command line :

./pd_sqlite_eg eg.db table

./pd_sqlite_eg db.sqlite3 table

All SQlite tables will be downloaded in excel workbook

Python Dependencies :

Pandas
openpyxl
sqlite3,sys,os


