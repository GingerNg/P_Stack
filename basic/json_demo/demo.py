import json

if __name__ == '__main__':
    d = {
        "4":"5"
    }
    kwargs = {
        "1":"我",
        "2":{"3":3}
    }
    d["kwargs"] = json.dumps(kwargs)
    dd = json.dumps(d)

    print(dd)
