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
import pandas as pd

# %%
# fra kurs 091222

# %%
df = (
    pd
    .read_csv("data.txt", header=None, skip_blank_lines=False, names=["calories"])
    .assign(
        delim=lambda rows: rows.isnull(),
        elf_number=lambda rows: rows.delim.cumsum()
    )
    .dropna()
    .groupby("elf_number")
    .agg({"calories": "sum"})
    .reset_index()
)


# %%
def summerer_gruppe(df, group_column, sum_column):
    return df. groupby(group_column).agg({sum_column: "sum"})

df = (
    pd
    .read_csv("data.txt", header=None, skip_blank_lines=False, names=["calories"])
    .assign(
        delim=lambda rows: rows.isnull(),
        elf_number=lambda rows: rows.delim.cumsum()
    )
    .dropna()
    .pipe(summerer_gruppe, group_column="elf_number", sum_column="calories")
)

# %%
