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
from random import randint
import pandas as pd


# %%
def spill_kamp(indeks):
    i = indeks[0]
    j = indeks[1]

    max_maal = randint(0,6)

    maal_hjemme = randint(0, max_maal)
    maal_borte = randint(0, max_maal)

    maal[i] += maal_hjemme
    maal[j] += maal_borte

    if maal_hjemme > maal_borte:
        poeng[i] += 3
    elif maal_hjemme == maal_borte:
        poeng[i] += 1
        poeng[j] += 1
    else:
        poeng[j] += 3
    
    t = 100
    while(t > 0):
        if randint(0,100) < 20:
            if randint(0,100 <= 50):
                gule[i] += 1
            else:
                gule[j] += 1
        t -= randint(0,20)
        if randint(0,100) < 4:
            if randint(0,100 <= 50):
                rode[i] += 1
            else:
                rode[j] += 1


def skriv_standings():
    print(gruppe)
    print("poeng", poeng)
    print("maal", maal)
    print("gule", gule)
    print("rode", rode)   


# %%
ant_poeng_for_andreplass = []

for i in range(10000):

    gruppe = ["Japan", "Spania", "Tyskland", "Costa Rica"]
    poeng = [0,0,0,0]
    maal = [0,0,0,0]
    gule = [0,0,0,0]
    rode = [0,0,0,0]

    kamper = [[0,1], [2,3], [0,2], [1,3], [0,3], [1,2]]

    for kamp in kamper:
        spill_kamp(kamp)

    poeng.sort()

    ant_poeng_for_andreplass.append(poeng[2])

    # if poeng[2] == 4:

    #     tbl = pd.DataFrame([gruppe, poeng, maal, gule, rode]).T
    #     tbl.columns = ['navn', 'poeng', 'mål', 'gule', 'røde']
    #     tbl = tbl.sort_values(['poeng', 'mål'], ascending=False)
    #     tbl.poeng.iloc[1]
    #     break

tbl



# %%
print("Antall gruppespill:\t", len(ant_poeng_for_andreplass))
ant = ant_poeng_for_andreplass.count(9)
print("Antall ganger andreplass fikk 9 poeng:\t", ant)
print("Antall prosent: ", ant/len(ant_poeng_for_andreplass)*100)

# %%

# %%

## gitt 4 poeng, hva er sjansen for å gå videre?
kamper_med_firepoengere = [] # 1 hvis gått videre, 0 hvis ikke

for i in range(10000):

    gruppe = ["Japan", "Spania", "Tyskland", "Costa Rica"]
    poeng = [0,0,0,0]
    maal = [0,0,0,0]
    gule = [0,0,0,0]
    rode = [0,0,0,0]

    kamper = [[0,1], [2,3], [0,2], [1,3], [0,3], [1,2]]


    for kamp in kamper:
        spill_kamp(kamp)

    if poeng.__contains__(4):
        poeng.sort()

        if poeng[3] == 4 or poeng[2] == 4:
            kamper_med_firepoengere.append(1)
        else:
            kamper_med_firepoengere.append(0)

    # if poeng[2] == 4:

    #     tbl = pd.DataFrame([gruppe, poeng, maal, gule, rode]).T
    #     tbl.columns = ['navn', 'poeng', 'mål', 'gule', 'røde']
    #     tbl = tbl.sort_values(['poeng', 'mål'], ascending=False)
    #     tbl.poeng.iloc[1]
    #     break


# %%
tot = len(kamper_med_firepoengere)
ant_videre = sum(kamper_med_firepoengere)
prosent = round(ant_videre * 100 / tot,1)

print(f'Antall gruppespill av 10000 som endte med minst et lag på 4 poeng: {tot}')
print(f'Antall ganger et lag med 4 poeng gikk videre: {ant_videre}. Dvs {prosent} %. ')

