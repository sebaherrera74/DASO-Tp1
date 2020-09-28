
class Main:
    def __init__(self,file_name):
        self.set_file_name(file_name)
    
    def set_file_name(self,file_name):
        self.__file_name=file_name
    
    def get_file_name(self):
        return self.__file_name
    
    def main(self):
        with open (self.get_file_name(),"r",encoding="utf-8") as f:
            texto=f.readline()
        return texto


      

m = Main("config.txt")
prueba=m.main()
print(prueba)