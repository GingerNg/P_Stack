"""
    python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"
"""
# import csv,json
#
# d = list(csv.reader(open('./csv2json/demo.csv')))
#
# fw =open('demo.json','w',encoding='utf-8')
#
# json.dump(d,fw,ensure_ascii=False,indent=4)

# import pandas as pd
# demo_data = pd.read_csv("./csv2json/demo.csv", encoding="utf-8", sep=",")
# demo_data.to_json("./csv2json/demo.json")

import csv
import json


def csv2json(col_name_exist):
    f_j =  open('./csv2json/demo.json', "a")
    with open('./csv2json/demo.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=' ')
        result = []
        for i, rows in enumerate(spamreader):
            if col_name_exist and i == 0:
                col_names = rows
            elif col_name_exist and i> 0:
                if len(rows) == len(col_names):
                    for i in range(len(rows)):
                        result = {}
                        result[col_names[i]] = rows[i]
                    # print(result)
                    f_j.write(str(result)+"\n")
                    #     json.dump(result, f_j, ensure_ascii=False)
            else:
                result.append(rows)

            # col_names =
        # for row in spamreader:
        #     print(', '.join(row))

if __name__ == '__main__':
    csv2json(True)