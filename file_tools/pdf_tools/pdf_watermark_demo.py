



# fr = open("/home/ginger/case5.pdf","rb")
fr = open("/home/ginger/waterproof.pdf","rb")
obj = fr.read().decode()
print(obj)
# for line in fr.readlines():
#     print(line)

# import pdfparanoia
#
# pdf = pdfparanoia.scrub(open("/home/ginger/cases/case5_1.pdf","rb"))
#
# with open("output.pdf", "wb") as file_handler:
#     file_handler.write(pdf)