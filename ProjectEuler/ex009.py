import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.function
def is_pythagorean_triplet(triplet: list[int]) -> bool:
    t = sorted(triplet)
    a, b, c = triplet
    return a**2 + b**2 == c**2


@app.cell
def _():
    for a in range(1001):
        for b in range(a, 1001):
            c = 1000 - a - b
            if c < 0 or c <= b:
                continue
            if is_pythagorean_triplet([a, b, c]):
                print(a, b, c)
                print(a*b*c)
                break
    return


if __name__ == "__main__":
    app.run()
