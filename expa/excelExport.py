import os
import xlwt
import json

FILE_TO_ANALYZE = "json"

REALIZED = "total_realized"
FINISHED = "total_finished"
COMPLETED = "total_completed"

wb = xlwt.Workbook()
sheet = wb.add_sheet("DATA")

row=0
sheet.write(row, 0, "ID")
sheet.write(row, 1, "Realized")
sheet.write(row, 2, "Finished")
sheet.write(row, 3, "Completed")

row += 1

for name in os.listdir("./" + FILE_TO_ANALYZE):

    with open("./" + FILE_TO_ANALYZE + "/" + name) as json_file:

        try:
            data = json.load(json_file)
        except:
            print("Error in [" + str(name) + "]")
            continue

        id = name.replace("json-", "")
        id = id.replace(".txt", "")

        sheet.write(row, 0, id)
        sheet.write(row, 1, data['analytics'][REALIZED]['doc_count'])
        sheet.write(row, 2, data['analytics'][FINISHED]['doc_count'])
        sheet.write(row, 3, data['analytics'][COMPLETED]['doc_count'])

    row += 1


wb.save("leto19.xls")