class Stack:
    """
    Implementation of a stack data strucure
    with the item being added and removed to the end of a list.
    """
    def __init__(self):
        """ (Stack) -> NoneType

        Instantiates an empy stack.

        >>> s = Stack()
        """
        self.items = []

    def is_empty(self):
        """ (Stack) -> bool

        Returns a True if the stack is empty.

        >>> s = Stack()
        >>> s.is_empty()
        True
        >>> s.push('test')
        >>> s.is_empty()
        False
        """
        return self.items == []

    def push(self, item):
        """ (Stack, Object) -> NoneType

        Adds the item to the top of the stack

        >>> s = Stack()
        >>> s.push('this')
        >>> s.items
        ['this']
        >>> s.push('is')
        >>> s.items
        ['this', 'is']
        """
        self.items.append(item)

    def pop(self):
        """ (Stack) -> Object

        Returns and removes the last item added to the stack. If list is empty,
        will produce an error.
        
        >>> s = Stack()
        >>> s.push('this')
        >>> s.items
        ['this']
        >>> s.push('is')
        >>> s.items
        ['this', 'is']
        >>> s.pop()
        'is'
        >>> s.pop()
        'test'
        """
        if self.is_empty():
            raise EmptyStackException
        return self.items.pop()

    def peek(self):
        """ Stack -> Object

        Does not modify the stack. Returns the last object added,
        but does not remove it.

        >>> s = Stack()
        >>> s.push('test2')
        >>> s.peek()
        'test2'
        >>> s.items
        ['test2']
        """
        if self.is_empty():
            raise EmptyStackException
        return self.items[-1]

    def size(self):
        """ (Stack) -> int

        Return the numbers of items in the stack

        >>> s = Stack()
        >>> s.size()
        0
        >>> s.push('foo')
        >>> s.size()
        1
        """
        return len(self.items)

if __name__ == '__main__':
# Practice problems using a stack    
    
    def rev_string(my_str):
        """ str -> str

        Returns a reverse string using a stack implementation

        >>> rev_string('apple')
        'elppa'
        >>> rev_string('x')
        'x'
        >>> rev_string('1234567890')
        '0987654321'
        """
        s = Stack()
        result = ''

        # add each char to the stack
        for char in my_str:
            s.push(char)
        
        # pop each char from the stack to reverse the order, and then append the
        # string to resuly
        while not s.is_empty():
            result += s.pop()
        
        return result

    def par_checker(symbol_string):
        """ (str) -> bool

        This function, par_checker, assumes that a Stack class is available and
        returns a boolean result as to whether the string of symbols is balanced.

        

        >>> par_checker('{(([]))}')
        True
        >>> par_checker('())]')
        False
        """
        s = Stack()
        balanced = True
        index = 0

        while index < len(symbol_string) and balanced:
            symbol = symbol_string[index]
            if symbol in "([{":
                s.push(symbol)
            elif symbol in "}])":
                if s.is_empty():
                    balanced = False
                else:
                    top = s.pop()
                    if not matches(top, symbol):
                        balanced = False
            index += 1

        if balanced and s.is_empty():
            return True
        else:
            return False
        
    def matches(open, close):
        """ (str, str) -> bool

        Precondition: open must me either '(' or '[' or '{'. close must be ')' or ']' or '}'.
        
        Helper method for par_checker which returns True of the opening symbol matches
        the closing symbol.
        """
        opens = "([{"
        closers = ")]}"
        return opens.index(open) == closers.index(close)

        
    def base_converter(dec_number, base = 2):
        """ (int, int) -> int
        
        Takes a decimal number and a base that returns a converted number. Default base is binary.

        >>> base_converter(25, 2)
        '11001'
        >>> base_converter(25, 2)
        '10000'
        >>> base_converter(25, 8)
        '31'
        >>> base_converter(256, 16) # hexadecimal conversion
        100
        >>> base_converter(26, 26)
        '10'
        """
        digits = "0123456789ABCDEF"
        remstack = Stack()

        while dec_number > 0:
            rem = dec_number % base
            remstack.push(rem)
            dec_number = dec_number // base

        new_string = ""
        while not remstack.is_empty():
            new_string += digits[remstack.pop()]

        return new_string


    def infix_to_postfix(infix_expr):
        """ (str) -> str

        Precondition: variables must be uppercase.

        Converts the infix expression to a postfix expression. Both are represented as strings. MUST BE VARIABLES
        
        >>> infix_to_postfix("( A + B ) * ( C + D )")
        'A B + C D + *'
        >>> infix_to_postfix("( A + B ) * C")
        'A B + C *'
        >>> infix_to_postfix("A + B * C")
        'A B C * +'
        """
        prec = {}
        prec["*"] = 3
        prec["/"] = 3
        prec["+"] = 2
        prec["-"] = 2
        prec["("] = 1
        operator_stack = Stack()
        postfix_list = []
        token_list = infix_expr.split()
        
        # iterate through each token in infix_expr and add to appropriate stack. If end token pop and
        # create the expression.
        for token in token_list:
            if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
                postfix_list.append(token)
            elif token == '(':
                operator_stack.push(token)
            elif token == ')':
                topToken = operator_stack.pop()
                while topToken != '(':
                    postfix_list.append(topToken)
                    topToken = operator_stack.pop()
            else:
                while (not operator_stack.is_empty()) and(prec[operator_stack.peek()] >= prec[token]):
                      postfix_list.append(operator_stack.pop())
                operator_stack.push(token)

        while not operator_stack.is_empty():
            postfix_list.append(operator_stack.pop())
        return " ".join(postfix_list)
    

    def postfix_eval(postfix_expr):
        """ (str) -> int
        Evaluates the postfix expression as a math problem.
        Both are represented as strings.
        """
        operand_Stack = Stack()
        token_list = postfix_expr.split()

        for token in token_list:
            if token in "0123456789":
                operand_Stack.push(int(token))
            else:
                operand2 = operand_Stack.pop()
                operand1 = operand_Stack.pop()
                result = do_math(token, operand1, operand2)
                operand_Stack.push(result)
        return operand_Stack.pop()

    def do_math(op, op1, op2):
        """ (str, num, num) -> int

        Perform the mathmatical expression. Division rounds to the nearest integer.
        

        >>> do_math('*', 5, 5)
        25
        >>> do_math('/', 25, 5)
        5
        >>> do_math('/', 27.5, 5)
        6
        """
        if op == "*":
            return op1 * op2
        elif op == "/":
            return int(round(op1 / op2))
        elif op == "+":
            return op1 + op2
        else:
            return op1 - op2
