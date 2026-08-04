import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from random import random
    from random import randint

    return randint, random


@app.cell
def _(randint, random):
    class Husholdning:
        def __init__(self, ant_pers: int, utdanning: bool, er_strukturert: bool, id_: int):
            self.ant_pers = ant_pers
            self.utdanning = utdanning
            self.er_strukturert = er_strukturert
            self.id_ = id_
            self.kvitteringer = []

        def __repr__(self):
            return f"""
            Ant pers: {self.ant_pers}
            Utdanning: {self.utdanning}
            Strukturert: {self.er_strukturert}
            Ant kvitteringer: {len(self.kvitteringer)}
            Tot pris: {self.get_tot_pris()} kroner
            """

        def get_tot_pris(self):
            return sum([k.pris for k in self.kvitteringer])

        def handletur(self, dag: int):
            if self.er_strukturert:
                r = random()
                if r < 0.1:
                    ant_varer = randint(10, 100)
                    pris = randint(50, 150) * ant_varer * max(int(self.ant_pers*0.8), 1)
                    self.kvitteringer.append(
                        Kvittering(ant_varer=ant_varer, pris=pris, id_= f"{self.id_}-{dag}")
                    )
            else:
                r = random()
                if r < 0.75:
                    ant_varer = randint(5, 15)
                    pris = randint(50, 150) * ant_varer * max(int(self.ant_pers*0.8), 1)
                    self.kvitteringer.append(
                        Kvittering(ant_varer=ant_varer, pris=pris, id_= f"{self.id_}-{dag}")
                    )

    return (Husholdning,)


@app.class_definition
class Kvittering:
    def __init__(self, ant_varer: int, pris: int, id_: int):
        self.ant_varer = ant_varer
        self.pris = pris
        self.id_ = id_


@app.cell
def _(Husholdning, random):
    N_BEF = 5*10**3
    hush = []
    for n in range(N_BEF // 2):
        r = random()
        if r < 0.5:
            ant_pers = 1
        elif r < 0.75:
            ant_pers = 2
        elif r < 0.9:
            ant_pers = 3
        else:
            ant_pers = 4

        r = random()
        if r < 0.5:
            utdanning = False
        else:
            utdanning = True

        r = random()
        if r < 0.75:
            er_strukturert = False
        else:
            er_strukturert = True

        hush.append(Husholdning(
            ant_pers=ant_pers,
            utdanning=utdanning,
            er_strukturert=er_strukturert,
            id_=n
        ))
    return (hush,)


@app.cell
def _(hush):
    for day in range(365):
        for h in hush:
            h.handletur(day)
    return


@app.cell
def _(hush):
    print(hush[10])
    return


@app.cell
def _():
    import pandas as pd

    return (pd,)


@app.cell
def _(hush):
    alla_kvittos = {}
    for hny in hush:
        for kny in hny.kvitteringer:
            alla_kvittos[kny.id_] = [kny.ant_varer, kny.pris]
    return (alla_kvittos,)


@app.cell
def _(alla_kvittos, pd):
    df = pd.DataFrame(alla_kvittos)
    return


if __name__ == "__main__":
    app.run()
