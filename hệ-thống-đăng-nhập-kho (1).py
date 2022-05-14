class login:
    def __init__(self, id ,pas ):
        self.id=id
        self.pas=pas

    def check(self,id,pas):
        print self .id
        if self.id==id and self.pas == pas:
            print ('dang nhap thanh cong')


log=login('admin','admin')
log.check(raw_input('enter login ID:'),raw_input('enter password: '))

