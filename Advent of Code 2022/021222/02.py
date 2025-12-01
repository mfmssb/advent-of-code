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

games = datastr.split("\n")

def regn_poeng(s):
    mot = s[0]
    jeg = s[2]
    p = 0
    if mot == "A":
        match jeg:
            case "X":
                tegnpoeng = 1
                resultat = 3
            case "Y":
                tegnpoeng = 2
                resultat = 6
            case "Z":
                tegnpoeng = 3
                resultat = 0
            case _:
                print("ERROR A")
    if mot == "B":
        match jeg:
            case "X":
                tegnpoeng = 1
                resultat = 0
            case "Y":
                tegnpoeng = 2
                resultat = 3
            case "Z":
                tegnpoeng = 3
                resultat = 6
            case _:
                print("ERROR B")
    if mot == "C":
        match jeg:
            case "X":
                tegnpoeng = 1
                resultat = 6
            case "Y":
                tegnpoeng = 2
                resultat = 0
            case "Z":
                tegnpoeng = 3
                resultat = 3
            case _:
                print("ERROR C")
    return tegnpoeng+resultat

tot = 0
for g in games:
    tot += regn_poeng(g)

print(tot)

# %% [markdown]
# # Round two

# %%
f = open("data.txt", "r")
datastr = f.read()

games = datastr.split("\n")

def regn_poeng2(s):
    mot = s[0]
    jeg = s[2]

    if mot == "A":
        match jeg:
            case "X":
                tegnpoeng = 3
                resultat = 0
            case "Y":
                tegnpoeng = 1
                resultat = 3
            case "Z":
                tegnpoeng = 2
                resultat = 6
    if mot == "B":
        match jeg:
            case "X":
                tegnpoeng = 1
                resultat = 0
            case "Y":
                tegnpoeng = 2
                resultat = 3
            case "Z":
                tegnpoeng = 3
                resultat = 6
    if mot == "C":
        match jeg:
            case "X":
                tegnpoeng = 2
                resultat = 0
            case "Y":
                tegnpoeng = 3
                resultat = 3
            case "Z":
                tegnpoeng = 1
                resultat = 6
    return tegnpoeng+resultat

tot = 0
for g in games:
    tot += regn_poeng2(g)

print(tot)

# %%
