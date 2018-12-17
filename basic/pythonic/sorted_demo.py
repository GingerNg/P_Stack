

if __name__ == "__main__":
    hits = [{"test":"test"},{"test1":"test2"}]
    for hit in hits:
        dhits = {}
        for k,v in hit.items():
            dhits[k] = v