import os
path=r"C:\MyPython\aaa"

if os.path.exists(path)==True:
    os.rmdir(path)
    print("成功刪除")
else:
    print("目錄不存在")