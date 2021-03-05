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

        import mindydb.models as models
        # Insert new User
        models.cursor.execute(add_Users, data_Users)

        # Make sure data is committed to the database
        models.cnx.commit()

        # # ======================================================
        # models.cursor.close()
        # print("\n cursor.close() ---> !!")
        # # ======================================================
        # models.cnx.close()
        # print("\n закрыл соединениё --> DIS connect к БД --> !!")
        #
        # return HttpResponse(f"Записал в базу: <h2> {login=} <br> {name=} <br>\
        #                     {surname=} <br> {date_of_birth=} <br> </h2>")

        #============================================
        # select
        query = ("SELECT id, login, name, surname, date_of_birth FROM users ")
        #         "WHERE hire_date BETWEEN %s AND %s")

        # cursor.execute(query, (hire_start, hire_end))
        models.cursor.execute(query)

        cursor = models.cursor
        cursor_list = []
        print("id |login   |name   |surname   |date_of_birth ")
        print("==============================================")
        for (id, login, name, surname, date_of_birth) in cursor:
            print(f"{id} |{login} |{name} |{surname} |{date_of_birth}")
            cursor_list.append([id,login,name,surname,date_of_birth])
        # print(f"{cursor=}")
        print(f"{cursor_list=}")
        # print(f"{type(cursor)=}")
        # ===========================================================
        # Make sure data is committed to the database
        # cnx.commit()

        # ======================================================
        models.cursor.close()
        print("\n cursor.close() ---> !!")
        # ======================================================
        models.cnx.close()
        print("\n закрыл соединениё --> DIS connect к БД --> !!")

        # return HttpResponse(f"Записал в базу: <h2> {login=} <br> {name=} <br>\
        #                              {surname=} <br> {date_of_birth=} <br> \
        #                     {cursor_list=} <br> \
        #                     </h2>")

        return render(request, 'db_output.html', { 'login': login, 'cursor_list':cursor_list})
        # return render_to_response('db_output.html', cursor_list=c_list)