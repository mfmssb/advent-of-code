import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import pandas as pd
    import numpy as np

    return np, pd


@app.cell
def _():
    data = """75
    95 64
    17 47 82
    18 35 87 10
    20 04 82 47 65
    19 01 23 75 03 34
    88 02 77 73 07 63 67
    99 65 04 28 06 16 70 92
    41 41 26 56 83 40 80 70 33
    41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
    70 11 33 28 77 73 17 78 39 68 17 57
    91 71 52 38 17 14 91 43 58 50 27 29 48
    63 66 04 68 89 53 67 30 73 16 69 87 40 31
    04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
    return (data,)


@app.cell
def _(data, np, pd):
    def parse_data(data: str) -> np.array:
        d = [x.split(" ") for x in data.split("\n")]
        d = [[int(x) for x in l] for l in d]
    
        max_length = max([len(line) for line in d])
        padded_d = [
            row + [0] * (max_length - len(row))
            for row in d
        ]
    
        return np.array(padded_d)

    def reduce_grid(data: str) -> np.array:
        d = parse_data(data)
    
        for j in range(len(d)-1):
            to_row = d[-2-j][:]
            from_row = d[-1-j][:]
            for i in range(len(to_row)-1):
                if to_row[i] != 0:
                    candidates = from_row[i:i+2]
                    to_row[i] += max(candidates)
        return d

    d = reduce_grid(data)
    print("Answer:", d[0][0])

    pd.DataFrame(d)
    return


if __name__ == "__main__":
    app.run()
