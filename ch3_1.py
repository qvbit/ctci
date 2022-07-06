class FixedMultiStack:
    def __init__(self, stack_size: int, num_stacks: int = 3):
        self.stack_size = stack_size
        self.num_stacks = num_stacks
        self.values = [0]*(self.num_stacks*self.stack_size)
        self.sizes = [0]*self.num_stacks

    def index_of_top(self, stack_num: int) -> int:
        offset = stack_num*self.stack_size
        size = self.sizes[stack_num]
        return offset + size - 1
    
    def push(self, stack_num: int, value: int) -> None:
        if self.is_full(stack_num):
            raise Exception("Stack is full; cannot push new value!")
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value
    
    def pop(self, stack_num: int) -> int:
        if self.is_empty(stack_num):
            return Exception("Stack is empty; cannot pop from it!")
        top_value = self.values[self.index_of_top(stack_num)]
        self.sizes[stack_num] -= 1
        return top_value

    def peek(self, stack_num: int) -> int:
        if self.is_empty(stack_num):
            return Exception("Stack is empty; cannot peek!")
        return self.values[self.index_of_top(stack_num)]

    def is_full(self, stack_num: int):
        return self.sizes[stack_num] == self.stack_size

    def is_empty(self, stack_num: int):
        return self.sizes[stack_num] == 0


if __name__ == "__main__":
    """ Test run the multistack """
    fms = FixedMultiStack(100)
    fms.push(0, 69)
    fms.push(0, 420)
    fms.push(2, 94)
    fms.push(1, 493)
    print(fms.pop(2))
    print(fms.is_empty(2))
    print(fms.pop(0))
    print(fms.is_empty(0))
    fms.push(0, 40102)
    print(fms.peek(0))

    

        
