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
f = open("data.txt", "r")
datastr = f.read()

def contain_no_repeats(s):
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True

def first_start_of_msg_marker_of_size_n(n):
    for i in range(n,len(datastr)+1):
        if contain_no_repeats(datastr[i-n:i]):
            print(i, i-n, datastr[i-n:i])
            break

print(first_start_of_msg_marker_of_size_n(4))
print(first_start_of_msg_marker_of_size_n(14))

# %%
