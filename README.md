# BCG Analysis

I built this package with the objective of measuring in a simple, fast, but effective way, the impact of the key features of an app/webpage over the conversion.

It is a feature importance analysis, using BCG (Growth-Share) matrix.

This analysis helps to identify key features, grouping or clustering them into 4 different categories, as the BCG matrix states (see link at the bottom for more information).

To install the package, run this command in the terminal: pip install bcganalysis

We are going to see the following example.

# Example

We are going to use the toy dataset that is in the **example** folder. This is a dataframe which columns are **user_id** - **converted** - **event** - **datetime**.

The meaning of the columns are:
- user_id: the ID of the user.
- converted: stating if the user converted or not.
- event: the kind of feature that the user used and that we want to see its impact overt the conversion.
- datetime: day and time that this event was made.

Let's upload the toy dataset and start the analysis:

```
import pandas as pd

file_path = 'toy_dataset_sept.csv'

df = pd.read_csv(file_path).iloc[:,1:]

df.head(5)
```

<img src="https://raw.githubusercontent.com/Mateil04/bcg_analysis/master/example/000_dataset_example.PNG" width="500">

Great, so we have the table with all the events done per user. Now let's analyze which features are common among the users that have converted. First, we build a pivot table, so we know which actions (and how many times) were done per user:

```
# we import the package first
from bcg_analysis import Generate_BCG

# then we instantiate the object for the analysis 
features = Generate_BCG(df)

# and we get the pivot table
features.get_pivot(index=['user_id','converted'],columns='event')

# we find the pivot table in the attribute df_pivot
df_pivot = features.df_pivot

# let's see what we get
df_pivot.head(6)
```
<img src="https://raw.githubusercontent.com/Mateil04/bcg_analysis/master/example/000_df_pivot_example.png" width="700">

Then we want to see which actions were the most important to produce a conversion, and by how many users were those actions made (penetration). So if a particular action has high conversion but low penetration, we would like to make the feature more visible, to penetration increases and so does conversion. Let's see:

```
# then we generate the chart with penetration and conversion
features.generate_chart(threshold=1)

# we find the pivot table in the attribute df_pivot
df_chart = features.df_chart

# let's see what we get
df_chart.head(3)
```

<img src="https://raw.githubusercontent.com/Mateil04/bcg_analysis/master/example/000_df_chart.png" width="300">

# A deeper explanation

https://towardsdatascience.com/analyzing-feature-importance-user-behaviour-and-ux-performance-cbf32d55eff8

# About BCG / Growth-Share matrix
https://en.wikipedia.org/wiki/Growth%E2%80%93share_matrix

https://www.feedough.com/what-is-a-bcg-matrix-examples-how-to-guide/


# Questions / concact

Please send an email to:
mat.eil1991@gmail.com
