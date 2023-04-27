class Matrix:
    def __init__(self,height,breadth):
        self.m = height
        self.n = breadth
        mat = []
        for i in range(self.m):
            temp = []
            for j in range(self.n):
                temp.append(0)
            mat.append(temp)
        self.data = mat
        
    def __init__(self,arr):
        self.m = len(arr)
        self.n = len(arr[0])
        mat = []
        for i in range(self.m):
            temp = []
            for j in range(self.n):
                temp.append(0)
            mat.append(temp)
        self.data = mat

if __name__ == "__main__":
    n = int(input())
    if n < 0:
        raise Exception("less than zero")
    print(n)


    
    
    
    