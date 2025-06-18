class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if not self.isInteger(token):
                second = stack.pop()
                first = stack.pop()
                value = self.calculate(first, second, token)
                stack.append(value)
            else:
                stack.append(int(token))

        return stack[-1]

    def calculate(self, operand1: int, operand2: int, operator: str) -> int:
        match operator:
            case '+':
                return operand1 + operand2
            case '-':
                return operand1 - operand2
            case '*':
                return operand1 * operand2
            case '/':
                return int(operand1 / operand2)

    def isInteger(self, input: str) -> bool:
        try:
            int(input)
            return True
        except ValueError:
            return False

        
        
                