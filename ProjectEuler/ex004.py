import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.function
def is_palindrome(n: int) -> bool:
    n_str = str(n)

    return n_str == n_str[::-1]


@app.cell
def _():
    nums = [i for i in range(100, 1000)]

    pals = []
    for i in nums:
        for j in nums:
            prod = i*j
            if is_palindrome(prod):
                pals.append(prod)

    max(pals)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
