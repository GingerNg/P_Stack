
if __name__ == "__main__":
    tests = [[[0, 4], '平庄能源'], [[5, 7], '万科']]
    sent = "平庄能源和靖远煤电的法人是谁？"
    for uv, e in tests:
        print(uv,e)
    entls1 = {str(uv[0]): e for uv, e in tests}
    print(entls1)
    entls = {sent[uv[0]:uv[1]]: e for uv, e in tests}
    print(entls)
    print(entls.keys())

    entconcat = '|%s|' % ('|'.join(entls.keys()))
    print(entconcat)