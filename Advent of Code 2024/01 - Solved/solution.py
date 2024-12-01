filnavn = ["data0.txt", "data1.txt", "data2.txt"]
data = []
for fil in filnavn:
    with open(fil, 'r') as file:
        data.append(file.read())

print("Størrelsen på inndata:")
for i, x in enumerate(data):
    print(i, len(x))

# # Problem 1

# ## Intermediate Steps 1

import pandas as pd


def preprocess_data(data_in, sort_columns=True):
    d = data_in.split("\n")
    
    left, right = [], []
    for pair in d:
        pair_list = pair.split('   ')
        left.append(pair_list[0])
        right.append(pair_list[1])
    
    left = pd.DataFrame(left, columns=['left'], dtype='float')
    right = pd.DataFrame(right, columns=['right'], dtype='float')

    if sort_columns:
        left  = left.sort_values('left').reset_index(drop=True)
        right = right.sort_values('right').reset_index(drop=True)
    
    return pd.concat([left, right], axis=1)


def calculate_diff(df):
    df['diff'] = abs(df['left'] - df['right'])
    return df['diff'].sum()


# %%timeit
df = preprocess_data(data[1])
ans = calculate_diff(df)

# ## Solution 1

print(int(ans))


# # Problem 2

# ## Intermediate Steps 2

def calculate_score(df):

    right_counts = df['right'].value_counts().reset_index()
    
    final = pd.merge(
        df,
        right_counts,
        left_on='left',
        right_on='right',
        how='inner'
    )
    
    final['score'] = final['left'] * final['count']
    return final['score'].sum()


# %%timeit
df = preprocess_data(data[1])
ans = calculate_score(df)

# ## Solution 2

print(int(ans))
