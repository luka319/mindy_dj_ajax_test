from django.db import models

# Create your models here.

import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta

config = {
      'user': 'Mindy',
      'password': 'qazwsx',
      'host': '127.0.0.1',
      'database': 'mindy_test',
      'raise_on_warnings': True
      }

      # cnx = mysql.connector.connect(**config)

      # cnx.close()

try:
            cnx = mysql.connector.connect(**config)
            print("\n connect к БД --> успешно!!\n")
            cursor = cnx.cursor()
            print("\n cursor ---> успешно!!")

except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("\n Не торт юзер или его пароль!!!  \
                   Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("\n Нет вашей базы данных! Database does not exist")
            else:
                print(err)
else:
            # cnx.close()
            pass

# ========================
# DB_NAME = 'mindy_test'

# CREATE TABLE `Users` IF NOT EXISTS ( \

TABLES = {}
TABLES['mindy_test'] = ("\
            CREATE TABLE `Users` ( \
              `id` integer  PRIMARY KEY AUTO_INCREMENT,\
              `login` Varchar(50),\
              `name` Varchar(50),  \
              `surname` Varchar(50),\
              `date_of_birth` date  \
            ) ENGINE=InnoDB\
            "
            )

for table_name in TABLES:
            table_description = TABLES[table_name]
            try:
                print("\n Создаю таблиццу {0} --> Creating table {0}: \n".format(table_name), end='')
                cursor.execute(table_description)
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("\n эта таблица уже есть already exists.\n")
                else:
                    print(err.msg)
            else:
                print("OK")
        # ======================================================
"""
from datetime import date, datetime, timedelta
import mysql.connector

cnx = mysql.connector.connect(user='scott', database='employees')
cursor = cnx.cursor()

tomorrow = datetime.now().date() + timedelta(days=1)
"""
