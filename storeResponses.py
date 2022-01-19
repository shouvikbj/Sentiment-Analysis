import json
import shortuuid
import copy


def store(APP_ROOT, url, text, sentiment):
    resp_id = str(shortuuid.uuid())
    with open(f"{APP_ROOT}/db/data.json", "r") as json_file:
        storedData = json.load(json_file)
        backupData = copy.deepcopy(storedData)

    storedData.update({url: {"id": resp_id, "text": text, "sentiment": sentiment}})

    try:
        with open(f"{APP_ROOT}/db/data.json", "w") as json_file:
            json_file.seek(0)
            json.dump(storedData, json_file, indent=2)
        resp = {"status": "ok", "message": "Current analysis stored successfully"}
        return resp
    except Exception:
        with open(f"{APP_ROOT}/db/data.json", "w") as json_file:
            json_file.seek(0)
            json.dump(backupData, json_file, indent=2)
        resp = {"status": "not-ok", "message": "Could not stored current analysis"}
        return resp
