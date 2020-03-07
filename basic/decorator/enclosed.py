# coding:utf8
# enclosed.py
def wrapper():
    filename = "enclosed.py"
    def show_filename():
        return "filename: %s" % filename # return a string
    return show_filename()


cf = wrapper()

if __name__ == '__main__':
    print (type(cf))
    print (cf)