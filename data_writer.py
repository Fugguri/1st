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
    a = str(items["id"])
    b = str(items["full_name"])
    c = str(items["phone"])
    d = str(items["age"])
    e = str(items["city"])
    f = str(items["clients"])
    g = str(items["departament"])
    k = " ".join(items["skills"])

    book = openpyxl.open("Emplouers.xlsx")
    sheet = book.active
    sheet.append([str(date), a, b, c, d, e, f, g, k])
    book.save("Emplouers.xlsx")
    book.close
