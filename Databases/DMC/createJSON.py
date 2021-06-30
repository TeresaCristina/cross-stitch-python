# createJSON: creates json files from a DMC database
# Teresa Costa - Jun/2021

import DMC
import json


def create_json_dmc(database):
    data = []
    d_range = len(database)
    for x in range(d_range):
        new_data = {'code': database[x][0], 'name': database[x][1], 'rgb': (database[x][2], database[x][3], database[x][4])}
        data.append(new_data)
        # print(data)
    with open('dmc.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


create_json_dmc(DMC.database_rgb)
