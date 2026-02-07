class tree_Node :
    def __init__(self,data):
        self.value = data
        self.right = None
        self.left = None
        
class tree:
    def __init__(self):
        self.root =None

    def insertleft(self,data):
        if self.root is None:
            self.root = tree_Node(data)
        else:
            temp = self.root
            while temp.left:
                temp = temp.left
            temp.left = tree_Node(data)

    def insertright(self,data):
        if self.root :
            temp = self.root
            while temp.right:
                temp = temp.right
            temp.right = tree_Node(data)
        else:
            self.root = tree_Node(data)

    def print_inorder(root):
        if root is None :
            print("")
        else:
            print_inorder(root.left)
            print_inorder(root.value)
            print_inorder(root.right)

    def print_preorder(root):
        if root is None :
            print("")
        else:
             print_preorder(root.value)
             print_preorder(root.left)
             print_preorder(root.right)


    def print_postorder(root):
        if root is None :
            print("")
        else:
            print_postorder(root.left)
            print_postorder(root.right)
            print_postorder(root.value)

    def print_levelorder(self):  #
        list = []
        temp = self.root
        if temp is None:
            return
        list.append(temp)  
        while list :
            k = list.pop(0) 
            print(k.value,end='')

            if k.left:
                list.append(k.left)
            if k.right:
                list.append(k.right)


    def height(root):              #ارتفاع
        if root is None:
            return 0
        return 1+max(height(root.left),height(root.right))
    
    def count_Leaves(root):       #تعداد برگ 
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        return count_Leaves(root.left)+count_Leaves(root.right) 
    
    
    def count_Node(root):         #تعداد گره
        if root is None:
            return 0
        return 1+ count_Node(root.left) + count_Node(root.right)
    
    
    def count_Node1D(root):        # تعداد گره درجه 1
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is None and root.right is not None:
            return  1 + count_Node1D(root.right)
        if root.left is not None and root.right is None:
            return  1 + count_Node1D(root.left) 
        
        return count_Node1D(root.left) + count_Node1D(root.right)
        

    def count_Node2D(root):        # تعداد گره درجه 2
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        if root.left is None and root.right is not None:
            return   count_Node2D(root.right)
        if root.left is not None and root.right is None:
            return   count_Node2D(root.left) 
        
        return  1 + count_Node2D(root.left) + count_Node2D(root.right) 
    
    def build_Bt(preorder,inorder):              #ساخت درخت با استفاده از تعریف درخت 
        if not preorder and not inorder :
            return None
        root =tree_Node(preorder[0])
        index = inorder.index(preorder[0])
        root.left = build_Bt(preorder[1:index+1],inorder[:index])
        root.right = build_Bt(preorder[index+1:],inorder[index+1])
    
    def sum_value(root):
        if root is None :
            return 0
        return sum_value(root.left)+sum_value(root.right)+root.value
             
    def find(root,target):                      #جستجو باینری
        if root is None :
            return False
        if root.value == target :
            return True
        return find(root.left,target) or find(root.right,target)
    
    def max_T2D(root):
        if root is None:
            return float(-inf)
        return max(root.value,root.left,root.right)
    
    def min_T2D(root):
        if root is None:
            return float(+inf)
        return min(root.value,root.left,root.right)

    def rec_Bt(root):                            #معکوس کردن درخت
        if not root:
            return None
        root.left,root.right = root.right , root.left
        rec_Bt(root.left)
        rec_Bt(root.right)