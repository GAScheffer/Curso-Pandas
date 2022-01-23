import pandas as pd

df = pd.read_csv("https://cdncontribute.geeksforgeeks.org/wp-content/uploads/nba.csv")
print(df)

forma = df.shape
print(f'\nFORMA:')
print(forma)

stack_df = df.stack()
print(f'\nPRINT DO DF.STACK:')
print(stack_df)

unstack = stack_df.unstack()
print(f'\nPRINT DO DF.UNSTACK:')
print(unstack)