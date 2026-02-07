class dnode():
    def __init__(self,data):
        self.Data = data
        self.next = None
        self.back = None

class dLinked_List():
    def __init__(self):
        self.head = None
        self.size = 0
        self.max_size = 10

    def insert(self,x):
        if self.size >= self.max_size :
            print("foll")
            return
        
        if self.head is None :
            a = dnode(x)
            self.head =a
            return a

        else:
             c=self.head
             while c.next :
                c=c.next
             a = dnode(x)
             c.next = a
             a.back =c
             return a
        
        self.size +=1
        


    def insert_first(self,x):
        if self.head is None:
            self.head = dnode(x)     

        a = dnode(x) 
        a.next = self.head
        self.head.back = a  #flash payeen ezafe 
        self.head = a 

    def insert_last(self,x):
        if self.head is None:
            self.head = dnode(x)  

        a = dnode(x)    
        c = self.head 
        while c.next :   
            c=c.next
        c.next = a 
        a.back =c   #flash payeen ezafe 

    def insert_after(self,x,y): 
        if self.head is None:
            print('emty')
            return

        c=self.head 
        while c:
            if c.Data == x:
                if c.next :
                    a = dnode(y)
                    a.next = c.next  
                    c.next.back =a     #
                    c.next =a 
                    a.back =c          #
                    #return          avalin ro faght jabeja
                self.insert_last(y)
                return    
            c = c.next  
        print ("x not found")

    def insert_befor(self,x,y):
        if self.head is None:
            print('emty')
            return
        
        if self.head.Data ==x :
            self.insert_first(y)

        c=self.head
        while c:
            if c.Data == x :
                a = dnode(y)
                a.next=c
                c.back.next = a
                a.back =c.back
                c.back = a
                # return
            c = c.next
        print("x not found")   


    def del_first(self):
        if self.head is None :
            print("empty")
            return   
        c = self.head
        self.head = c.next
        del c
        if self.head:
            self.head.back = None


    def del_last(self):
        if self.head is None :
            print("empty")
            return    
                
        if self.head.next is None :
            self.del_last()  

        else:
            c = self.head
            while c.next :
                c = c.next
            c.back.next = None   
            del c


    def del_after(self,x):
        if self.head is None :
            print("empty")
            return

        c=self.head
        while c:
            if c.Data == x :
                if c.next :  
                    a = c.next  
                    c.next = c.next.next 
                    if c.next:
                        c.next.back = c #khat bargasht
                    del a
                print("x is last")
                return
            c = c.next
        print("x not found")


    def del_befor(self,x):
        if self.head is None : 
            print("error")
            return

        if self.head.Data == x:
            print("error x is first")
            return
        
        c=self.head
        while c :
            if c.data ==x:
                if c.back :
                    a = c.back
                    c.back = a.back
                    if c.back :
                        c.back.next =c #khat bargasht
                    else:
                        self.head = self.head.next    
                    del a
                    return 
                print("x is first")
                return
            c = c.next
        print("x is not found")   


    def del_x(self,x):
        if self.head is None : 
            print("error")
            return

        if self.head.Data == x:
            self.del_first()
            return
        
        c =self.head
        while c :
            if c.Data == x:
                if c.next is None:
                    self.del_last
                    return
                c.back.next = c.next
                c.next.back = c.back
                del c
                return
            c=c.next
        print("x is not found")


    def del_all(self):
        while self.head:
            self.del_first()   


    def print_list(self):
        c = self.head
        l=[]
        while c:
            l.append(str(c.Data))
            c=c.next
        print('->'.join(l))
