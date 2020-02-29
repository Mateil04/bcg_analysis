# BCG Analysis

A feature importance analysis, using BCG (Growth-Share) matrix.

This analysis help to identify key features, and groping or clustering them into 4 different categories, as the BCG matrix states (see link at the bottom for more information).

To install the package, run this command in the terminal: pip install bcganalysis

We are going to see the following example.

# Example
```
import pandas as pd
from bcg_analysis.bcg_analysis import Generate_BCG

# you can find the toy_dataset.csv file in the repo directory
df_example = pd.read_csv('toy_dataset.csv',sep=';')

df = Generate_BCG(df_example)

# generate the plot
df.plot_bcg()

# generate the table 
df.df_bcg()
```

# About BCG / Growth-Share matrix

https://en.wikipedia.org/wiki/Growth%E2%80%93share_matrix

https://www.feedough.com/what-is-a-bcg-matrix-examples-how-to-guide/

bachmidi
An analysis of Bach's works using midi files
In this analysis, we rank the notes and chords used in the works of J.S Bach. Furthermore, we identify the most used progressions of chords. Finally, we group works in clusters, according to their chords. For a discussion of the results of this code, please take a look at this article

The creat-csv.sh script converts a .midi file to a .csv file with the help of mid2asc script. The code of mid2asc was copied from this site. Only the compiled file is included here.

The midi files should be put in the midi folder. The files were downloaded from The Mutopia Project. Only a few example files are included here.

The make_all_csv.sh scripts converts all the .midi files to .csv files and produces summary files for the notes, the chords and the chord progression of each midi files. In the end, the files are concatanated to summary files.

These summary files are analyzed in the jupyter notebook process_total_files. The notebook also uses the keys.csv file, which includes the music key of each work of Bach (indexed by their Bach works catalogue number) as scrapped from Wikipedia.
