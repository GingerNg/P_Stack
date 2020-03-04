from pdfrw import PdfReader
x = PdfReader('./cases/case5.pdf')
# for k in x.keys():
#     print(k)
# print(x.Info)  # meta_info of pdf
# print(x.Root.keys()) # ['/Names', '/Outlines', '/Pages', '/Type']
# print(x.pages[0].Contents)  # {'/Filter': '/FlateDecode', '/Length': '248'}
page = x.pages[0].Contents
bstream = bytes(page.stream)
print(page.stream)