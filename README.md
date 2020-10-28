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

<img src="https://raw.githubusercontent.com/Mateil04/bcg_analysis/master/example/000_dataset_example.PNG" width="400">

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

Great, now let's represent this in a plot! In the BCG Matrix.

```
# let's first make sure of importing matplotlib
import matplotlib.pyplot as plt

# also to set a good plot size
fig_size = plt.rcParams["figure.figsize"]
print ("Current size:", fig_size)
# let's make the plots a bit bigger than the default
# set figure width to 14 and height to 6
fig_size[0] = 10
fig_size[1] = 6
plt.rcParams["figure.figsize"] = fig_size

# now yes, let's plot it
features.plot_bcg()
```
<img src="https://raw.githubusercontent.com/Mateil04/bcg_analysis/master/example/000_final_plot.png" width="500">

We can see that the "search" actions has a lot of penetration (image a site like Amazon, everyone that goes to the site, makes a search action). Only 40% of them convert. However, if a user adds something to cart, chances to convert go up to 80%, but it has a low penetration (done by 20% of the users). So one idea might be to make the "add to cart" buttom bigger!

# For a deeper explanation of this methodology plese read my article in Medium

https://towardsdatascience.com/analyzing-feature-importance-user-behaviour-and-ux-performance-cbf32d55eff8

# More resources about BCG / Growth-Share matrix

https://en.wikipedia.org/wiki/Growth%E2%80%93share_matrix

https://www.feedough.com/what-is-a-bcg-matrix-examples-how-to-guide/


# Need help, or have any questions?

Please send an email to:
mat.eil1991@gmail.com

# How to cite

Please cite BCG Analysis by Matias Eiletz if it helps your research. You can use the following BibTeX entry:

@inproceedings{
  author    = {Matias Eiletz},
  title     = {Feature importance analysis with BCG Matrix},
  year      = {2020}
}

# Development

Pull requests are welcome.

