class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


class ParenthesisChecker:
    def __init__(self, expression):
        self.expression = expression
        self.stack = Stack()

    def match_parentheses(self, left, right):
        pairs = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        return pairs.get(left) == right

    def is_valid(self):
        for ch in self.expression:
            if ch in '({[':
                self.stack.push(ch)

            elif ch in ')}]':
                if self.stack.is_empty():
                    print("Right parentheses are more than left parentheses")
                    return False

                left = self.stack.pop()
                if not self.match_parentheses(left, ch):
                    print("Mismatched parentheses are", left, "and", ch)
                    return False

        if self.stack.is_empty():
            print("Balanced Parentheses")
            return True
        else:
            print("Left parentheses are more than right parentheses")
            return False

while True:
    expression = input("Enter expression (q to quit): ")

    if expression.lower() == 'q':
        break

    checker = ParenthesisChecker(expression)

    if checker.is_valid():
        print("Valid Expression\n")
    else:
        print("Invalid Expression\n")
