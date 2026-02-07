class node():
    def __init__(self,data):
        self.Data = data
        self.next = None

class Linked_List():
    def __init__(self):
        self.head = None
        self.size = 0
        self.max_size = 10


    def insert(self,x):   #متد ساختن لیست 
        if self.size >= self.max_size :
            print("foll")
            return
        
        if self.head is None:
            a=node(x)
            self.head = a
            return a
        else:
            c=self.head
            while c.next :
                c=c.next
            c.next = node(x)
            return c.next
        
        self.size +=1


    def insert_first(self,x):
        if self.head is None:
            self.head = node(x)     

        a = node(x) 
        a.next = self.head
        self.head = a  

    def insert_last(self,x):
        if self.head is None:
            self.head = node(x)  

        a = node(x)    #نود با نام بساز
        c = self.head # یک کپی از هد میگیریم و اسمش رو سی میازاریم
        while c.next :  #تا نود یکی مونده به اخر میریم  
            c=c.next
        c.next = a      #نود بعد برابر با نود ساخته شده

    def insert_after(self,x,y): #insert node y to node x
        if self.head is None:
            print('emty')
            return

        c=self.head # khone haye aval dar nazar
        while c:
            if c.Data == x:
                a = node(y)
                a.next = c.next  # etesal gere bad az c be node y
                c.next =a # c vasl be node y
                #return          avalin ro faght jabeja
            c = c.next  #mire badi
        print ("x not found")

    def insert_befor(self,x,y):
        if self.head is None:
            print('emty')
            return
        
        if self.head.Data ==x :
            self.insert_first(y)

        c=self.head
        while c.next:
            if c.next.Data == x :
                a = node(y)
                a.next=c.next
                c.next = a
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


    def del_last(self):
        if self.head is None :
            print("empty")
            return    
                
        if self.head.next is None :
            self.del_last()   

        else:
            c = self.head
            while c.next.next :
                c = c.next
            del c.next
            c.next = None


    def del_after(self,x):
        if self.head is None : 
            print("empty")
            return

        if self.head.next is None :
            print("error") 


        c=self.head
        while c.next:
            if c.Data == x :
                if c.next :  
                    a = c.next  #onsori ke pak mikonim
                    c.next = c.next.next # az rosh miparim
                    del a
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
        
        if self.head.next is None :
            print ("error 1 onsor ")

        if self.head.next.data == x :
            self.del_first()
            return

        if self.head.next.next is None :
            print ('error 2 onsor') 
            return  
        
        c=self.head
        while c.next.next :
            if c.next.next.data ==x:
                a = c.next
                c.next = a.next
                del a
                return 
            c = c.next
        print("x is not found")   


    def del_x (self,x):
        if self.head is None : 
            print("error")
            return

        if self.head.Data == x:
            self.del_first()
            return
        
        if self.head.next is None :
            print ("error 1 onsor ")

        c=self.head
        while c.next :
            if c.next.data == x :
                a = c.next
                c.next = a.next
                del a
                return

            c =c.next
        print('x not found')


    def del_all(self):
        while self.head:
            a = self.head
            self.head =a.next
            del a


    def print_list(self):
        c = self.head
        l=[]
        while c:
            l.append(str(c.Data))
            c=c.next
        print('->'.join(l))

             