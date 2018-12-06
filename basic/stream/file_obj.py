import chardet

def prn_obj(obj):
    print ('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))


def read_file(file_path):
    file_object = open(file_path,'r')
    try:
        all_the_text = file_object.read()
        return all_the_text
    finally:
        file_object.close()


if __name__ == "__main__":
    file_obj_0 = open("test_file.txt","r")  # #要有"rb"，如果没有这个的话，默认使用gbk读文件
    print(type(file_obj_0))   # _io.TextIOWrapper



    # ctt_0 = file_obj_0.read()

    # print(ctt_0)
    #
    # print(type(ctt_0))            # str

    file_obj_1 = open("test_file.txt","rb")  # BufferedReader
    print(type(file_obj_1))
    ctt_1 = file_obj_1.read()
    print(type(ctt_1))              # bytes

    print(chardet.detect(ctt_1))


    # bytes ---> decode--> str

    print(type(ctt_1.decode("utf-8")))

    print(ctt_1.decode("utf-8"))

    # property
    prn_obj(file_obj_1)


