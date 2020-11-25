# For function we need to have return keyword at the end otherwise they won't return anything
# One function should do just one thing
# Return keyword always ends the function so if something is after return even with good indentation it wouldn't work

def sum(num1, num2):
    def another_fucn(n1, n2):
        return n1 + n2
    return num1 + num2

print(sum(4,5))

