import marimo

__generated_with = "0.23.15"
app = marimo.App(width="medium")


@app.cell
def _():
    from datetime import datetime
    from datetime import timedelta

    return datetime, timedelta


@app.cell
def _():
    # print("\n".join([d for d in dir(datetime) if not d.startswith("_")]))
    return


@app.cell
def _(datetime, timedelta):
    from_date = datetime(1901, 1, 1)
    to_date = datetime(2000, 12, 31)

    count = 0
    curr_date = from_date
    while(curr_date != to_date):
        if curr_date.weekday() == 6 and curr_date.day == 1:
            count += 1    
        curr_date += timedelta(days=1)

    print("Answer:", count)
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
