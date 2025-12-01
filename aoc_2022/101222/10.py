# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.18.1
# ---

# %%
f = open("test.txt", "r")
datastr = f.read()
datalines = datastr.split("\n")

# %%
X = 1
cnum = 1
signal_strengths = []

# %% [markdown]
# - addx V takes two cycles to complete. After two cycles, the X register is increased by the value V. (V can be negative.)
# - noop takes one cycle to complete. It has no other effect.

# %%
for instruction in datalines:
    signal_strengths.append(cnum*X)
    if instruction == 'noop':
        cnum += 1
    else:
        a = instruction.split(" ")
        num = int(a[1])
        cnum += 1
        signal_strengths.append(cnum*X)
        X += num
        cnum += 1

# %%
cycle_check = [20,60,100,140,180,220]

sum = 0
for i in cycle_check:
    sum += signal_strengths[i-1]
print(sum)

# %% [markdown]
# #### Part 2

# %%
W = 40
H = 6
X = 1
cnum = 1
register_vals = []
screen = "-" * W * H


# %%
def draw_sprite_at(screen, n):
    if (n-1>=0): screen = change_letter(screen, "#", n-1)
    if (n+1<W*H): screen = change_letter(screen, "#", n+1)
    screen = change_letter(screen, "#", n)
    return screen

def change_letter(s, letter, index): 
    return s[:index] + letter + s[index+1:]

def draw_screen(screen):
    screen_arr = []
    for i in range(0,H):
        screen_arr.append(screen[i*W:(i+1)*W])

    for s in screen_arr:
        print(s)


# %%
for instruction in datalines:
    register_vals.append([cnum, X])
    if instruction == 'noop':
        cnum += 1
    else:
        a = instruction.split(" ")
        num = int(a[1])
        cnum += 1
        X += num
        screen = draw_sprite_at(screen, X)
        register_vals.append([cnum, X])
        cnum += 1
# draw_screen(screen)

# %%
screen

# %%
draw_screen(screen)


