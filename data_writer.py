import openpyxl
import datetime
import os.path


def add_items(items: dict, ):
    if not os.path.exists('Emplouers.xlsx'):  # True
        book = openpyxl.Workbook()
        sheet = book.active
        sheet.append(["Дата", "id", "ФИО", "Телефон", "Возраст", "Город",
                      "Работал с клиентами?", "Отделение", "Опыт"])
        book.save("Emplouers.xlsx")
        book.close

    date = datetime.date.today()
    if items["id"]:
        a = str(items["id"])
    else:
        a = ""
    if items["full_name"]:
        b = str(items["full_name"])
    else:
        b = ""
    if items["phone"]:
        c = str(items["phone"])
    else:
        c = ""
    if items["age"]:
        d = str(items["age"])
    else:
        d = ""
    if items["city"]:
        e = str(items["city"])
    else:
        e = ""
    if items["clients"]:
        f = str(items["clients"])
    else:
        f = ""
    if items["departament"]:
        g = str(items["departament"])
    else:
        g = ""
    if items["skills"]:
        k = " ".join(items["skills"])
    else:
        k = ""

    book = openpyxl.open("Emplouers.xlsx")
    sheet = book.active
    sheet.append([str(date), a, b, c, d, e, f, g, k])
    book.save("Emplouers.xlsx")
    book.close
