class Solution(object):
    def to_stack(self, num, op):
        nonlocal stack

        if op == "+":
            stack.append(num)
        if op == "-":
            stack.append(num)
        if op == "*":
            stack.append(stack.pop() * num)
        if op == "/":
            stack.append(stack.pop() / num)

    def calculate(self, s):
        for c in s:
            if c.isdigit():
                cur_sum = cur_sum * 10 + int(c)
        #return cal

if __name__ == "__main__":
    test = Solution()
    input = "3+2*2"

    check = test.calculate(input)
    print(check)