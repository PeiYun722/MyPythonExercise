file=open("1111.txt",encoding="utf8")
# eof=False
# while eof==False:
#     data=file.readline()
#     if data!='\n':
#         if data !="":
#             print(data)
#     else:
#         print("結束")
#         eof=True
#         file.close()

data=file.readlines()
print(data)