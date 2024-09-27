class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        signs = ["+", "-", "*", "/"]
        ints = []
        total = 0
        first = True
        for token in tokens:
            if token not in signs:
                ints.append(int(token))
            else:
                if first:
                    total = self.evaluate(ints.pop(-1), ints.pop(-1), token)
                    first = False
                else:
                    total = self.evaluate(total, ints.pop(-1), token)
        return total

    def evaluate(self, num1: int, num2: int, sign: str):
        if sign == "+":
            return num1 + num2
        if sign == "-":
            return num1 - num2
        if sign == "*":
            return num1 * num2
        if sign == "/":
            return int(num2 / num1)
        return 0


if __name__ == "__main__":
    s = Solution()
    assert s.evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert s.evalRPN(["10", "6", "9", "3", "+", "-11", "*",
                      "/", "*", "17", "+", "5", "+"]) == 22
    assert s.evalRPN(["18"]) == 18
    assert s.evalRPN(["3", "11", "+", "5", "-"]) == 9
    assert False
