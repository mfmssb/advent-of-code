# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
f = open("data.txt", "r")
datastr = f.read()
datalines = datastr.split("\n")


# %%
class Monkey:
    def __init__(self, index, items, operation, test, throwlogic):
        self.index = index
        self.items = items
        
        self.operation = operation   # string value to be evaluated by eval "old + 3"
        self.test = test             # string value to be evaluated by eval "x % 13 == 0"
        self.throwlogic = throwlogic # [if true throw to monkey, if false throw to monkey ]

        self.num_inspected_items = 0

    def inspect_item(self, old):
        new = eval(self.operation)
        return new
    
    def apply_test(self, x):
        return eval(self.test)



# %%
# parsing indata
def parse_monkey_data():
    monkeys = []
    for i in range(1,round(len(datalines) / 7)+1):
        a = datastr.split("Monkey ")[i]
        operation = a.split("\n")[2].replace("  Operation: new = ", "")
        a = a.replace("  Operation: new = " + operation + "\n", "")

        a = a.replace(",", "").replace("\n", "").replace(":", "").split(" ")
        a = [x for x in a if x.isdigit()]

        index = int(a[0])
        items = a[1:-3]
        items = [int(x) for x in items]
        
        divby = f"x % {a[-3]} == 0"
        throwlogic = [int(a[-2]), int(a[-1])]

        monkeys.append(Monkey(index, items, operation, divby, throwlogic))
    return monkeys

monkeys = parse_monkey_data()


# %%
def print_all_monkeys():
    for m in monkeys:
        # print(m.index, "items:", m.items, ". Number of inspections: ", m.num_inspected_items)
        print(m.index, ". Number of inspections: ", m.num_inspected_items)

        # print(vars(m))


# %%
def inspect_all_items(monkey,part):
    for x in monkey.items:
        # do monkey operation
        new = monkey.inspect_item(x)

        # boredom operation
        if part == 1:
            new = new // 3
        elif part == 2:
            # multiplying all the divisibility tests and throws away multiples of this number
            # to avoid huge numbers
            new = new % (19*2*13*5*7*11*17*3) 

        # item to new monkey depending on logic
        if monkey.apply_test(new):
            throw_to_num = monkey.throwlogic[0]
        else:
            throw_to_num = monkey.throwlogic[1]

        # update monkey's itemlists
        monkeys[throw_to_num].items.append(new)

        # increase num_inspected_items
        monkey.num_inspected_items += 1

    # print_all_monkeys()
    monkey.items = []


# %%
def do_n_rounds(n, part):
    for i in range(n):
        for i in range(len(monkeys)):
            inspect_all_items(monkeys[i],part)


# %%
do_n_rounds(20,1)


# %%
nums = []
for m in monkeys:
    nums.append(m.num_inspected_items)
    
nums.sort()
print(nums[-2]*nums[-1])

# %% [markdown]
# Part 2

# %%
monkeys = parse_monkey_data()

# %%
do_n_rounds(10000,2)

# %%
nums = []
for m in monkeys:
    nums.append(m.num_inspected_items)
    
nums.sort()
print(nums[-2]*nums[-1])

# %%
print_all_monkeys()
