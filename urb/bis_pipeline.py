
import os
import json
from urb.urb import processBuffer
from resources.shapefile_helper import getGeoJsonFromShapefile

json_schema = None
try:
    with open(os.path.join(os.path.dirname(__file__), './SFR_schema.json'), 'r') as json_schema_file:
        json_schema = json.load(json_schema_file)
except FileNotFoundError as e:
    pass


def process_1(
    path,
    file_name,
    ch_ledger,
    send_final_result,
    send_to_send_to_stage,
    previous_stage_result,
):
    count = 0
    file_name = file_name.split(".")[0]  # remove the .zip if applicable
    buffer = getGeoJsonFromShapefile(path + file_name)

    for b in buffer:
        data = processBuffer(b, change_log_function=ch_ledger.log_change_event)
        result = get_json_doc(data)
        send_final_result(result)
        count += 1

    return count


def get_json_doc(data):
    return {
        "data": {
            "feature_id": data["properties"]["feature_id"],
            "feature_name": data["properties"]["feature_name"],
            "feature_description": data["properties"]["feature_description"],
            "feature_class": data["properties"]["feature_class"],
        },
        "row_id": data["properties"]["feature_id"],
        "geometry":  data["geometry"]
    }
