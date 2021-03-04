# Create your views here.

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

context = {}
def front_insert(request):
    return render(request, 'front_insert.html', context=context)

def insert_into(request):
    """
    if request.method == "POST":
        login = request.POST.get("login")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        date_of_birth = request.POST.get("date_of_birth")

        return HttpResponse(f"<h2>login, {login} {name=}, {surname=},{date_of_birth=}</h2>")
    """
    if request.method == "POST":
        login = request.POST.get("login")
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        date_of_birth = request.POST.get("date_of_birth")

        #=====================================================
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
        add_Users = ("INSERT INTO Users "
                     "(login, name, surname, date_of_birth) "
                     "VALUES (%s, %s, %s, %s)")

        # data_Users = ('Vishnu', 'Krishna', 'Vasudeva', date(-3228, 7, 19))
        #  19 июля 3228 до н.э.
        """
          File "my_one_03_insert.py", line 89, in <module>
            data_Users = ('Vishnu', 'Krishna', 'Vasudeva', date(-3228, 7, 19))
        ValueError: year -3228 is out of range
        """
        # data_Users = ('Vishnu', 'Krishna', 'Vasudeva', date(3228, 7, 19))
        import datetime as dt
        # text = "2021-03-26"
        date_of_birth2 = dt.datetime.strptime(date_of_birth, '%Y-%m-%d').date()

        data_Users = (login, name, surname, date_of_birth2)

        # Insert new User
        cursor.execute(add_Users, data_Users)

        # Make sure data is committed to the database
        cnx.commit()

        # ======================================================
        cursor.close()
        print("\n cursor.close() ---> !!")
        # ======================================================
        cnx.close()
        print("\n закрыл соединениё --> DIS connect к БД --> !!")

        return HttpResponse(f"Записал в базу: <h2> {login=} <br> {name=} <br>\
                            {surname=} <br> {date_of_birth=} <br> </h2>")


