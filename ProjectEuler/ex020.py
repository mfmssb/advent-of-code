import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import math

    return (math,)


@app.cell
def _(math):
    def digit_sum(n: int) -> int:
        fn = math.factorial(n)
        fnstr = str(fn)
        return sum([int(c) for c in fnstr])    


    return (digit_sum,)


@app.cell
def _(digit_sum):
    print("Answer: ", digit_sum(100))
    return


if __name__ == "__main__":
    app.run()
