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
# Central imports (pandas as pd etc.)
import os
import pandas as pd

# %% [markdown]
# ### Demo av importer fra produksjonsnivå

# %%
# Change directory until find project root
notebook_path = os.getcwd()
for folder_level in range(50):
    if "pyproject.toml" in os.listdir(): break
    os.chdir("../")

# %%
# Do local imports here
from src.functions.fizzbuzz import fizzbuzz

# %%
# Reset current working directory after local imports
os.chdir(notebook_path)

# %%
# Example local function import
for x in fizzbuzz(range(1,26)): print(x)
