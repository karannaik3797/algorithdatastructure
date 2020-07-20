#python3
import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.maxval = -sys.maxsize 

    def Push(self, a):
        if self.__stack == []:
            self.__stack.append(a)
            self.maxval = a
        elif a >=self.maxval:
            temp = 2*a - self.maxval
            self.maxval = a
            self.__stack.append(temp)
        else:
            self.__stack.append(a)

    def Pop(self):
        if self.__stack == []:
            return 
        else:
            a = self.__stack.pop()
            if a>=self.maxval: 
                temp= 2*self.maxval - a
                self.maxval = temp
            
                
    
    def Max(self):
        return self.maxval


if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
