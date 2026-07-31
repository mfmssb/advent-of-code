import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    with open("/home/onyxia/work/marimo-project/advent-of-code/ProjectEuler/ex022.txt", "r") as file:
        data = file.read()
    return (data,)


@app.cell
def _(data):
    d = data.split(",")
    d = [s.replace('"', '') for s in d]
    d.sort()
    return (d,)


@app.cell
def _():
    ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ALPH_VAL = {k: v for k, v in zip(ALPHABET, range(1, len(ALPHABET)+1))}
    return (ALPH_VAL,)


@app.cell
def _(ALPH_VAL):
    def alph_val_for_name(name: str) -> int:
        sum_ = 0
        for c in name:
            sum_ += ALPH_VAL[c]
        return sum_

    return (alph_val_for_name,)


@app.cell
def _(alph_val_for_name, d):
    total = 0
    for i in range(len(d)):
        alphabetical_pos = i + 1
        alphabetical_val = alph_val_for_name(d[i])
        total += alphabetical_pos * alphabetical_val
    print(total)
    return


if __name__ == "__main__":
    app.run()
