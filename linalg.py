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
        self.data = arr

    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.data[i][j],end=" ")
            print()
    def submatrix(self,k,l):
        subarr = []
        for i in range(self.m):
            row = []
            for j in range(self.n):
                if 


if __name__ == "__main__":
    
    mat1 = Matrix([
        [1,2,3],
        [3,4,5],
        [4,5,6]
    ])
    mat1.display()
    mat2 = Matrix([
        [3,4,5],
        [4,5,6],
        [7,8,9]
    ])

    

    
    
    
    