class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

class ExpressionConverter:

    def __init__(self, expression):
        self.expression = expression

    def precedence(self, op):
        if op == '(':
            return 0
        elif op in '+-':
            return 1
        elif op in '*/%':
            return 2
        elif op == '^':
            return 3
        return 0

    def infix_to_postfix(self):
        st = Stack()
        postfix = []
        number = ""

        for symbol in self.expression:

            if symbol.isdigit():
                number += symbol 

            else:
                if number:
                    postfix.append(number)
                    number = ""

                if symbol in " \t":
                    continue

                elif symbol == '(':
                    st.push(symbol)

                elif symbol == ')':
                    while st.peek() != '(':
                        postfix.append(st.pop())
                    st.pop()  # remove '('

                elif symbol in "+-*/%^":
                    while (not st.is_empty() and
                           self.precedence(st.peek()) > self.precedence(symbol)):
                        postfix.append(st.pop())
                    st.push(symbol)

        if number:
            postfix.append(number)

        while not st.is_empty():
            postfix.append(st.pop())

        return postfix

class PostfixEvaluator:

    def evaluate(self, postfix):
        st = Stack()

        for token in postfix:

            if token.isdigit():
                st.push(int(token))

            else:
                x = st.pop()
                y = st.pop()

                if token == '+':
                    st.push(y + x)
                elif token == '-':
                    st.push(y - x)
                elif token == '*':
                    st.push(y * x)
                elif token == '/':
                    st.push(y / x)
                elif token == '%':
                    st.push(y % x)
                elif token == '^':
                    st.push(y ** x)

        return st.pop()

while True:
    expression = input("Enter infix expression (q to quit): ")

    if expression.lower() == 'q':
        break

    converter = ExpressionConverter(expression)
    postfix = converter.infix_to_postfix()

    print("Postfix expression:", " ".join(postfix))

    evaluator = PostfixEvaluator()
    result = evaluator.evaluate(postfix)

    print("Value of expression:", result)
    print()
