from openpyxl import load_workbook


def add_items(items: dict):
    a = []
    for key in items:
        a.append(items[key])
    fn = "example.xlsx"
    wb = load_workbook(fn)
    ws = wb["Лист1"]
    ws.append(items)
    wb.save(fn)
    wb.close()
