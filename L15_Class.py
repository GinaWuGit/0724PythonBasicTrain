#定義類別、類別屬性(封裝在類別中的變數與函式)
#定義一個類別IO，包含兩屬性分別為:supportedSrcs / read
class IO:
    supportedSrcs = ["console", "file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported!")
        else:
            print("Read from:", src)
#使用類別            
print(IO.supportedSrcs)
IO.read("web")
IO.read("file")