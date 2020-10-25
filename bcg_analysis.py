import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class Generate_BCG:
    
    def __init__(self, df):
        
        self.df = df
        self_df_pivot = None
        self.df_chart = pd.DataFrame({'event': [],
                                      'penetration': [],
                                      'conversion': []})

    def get_pivot(self, index, columns):

        # create this field in order to create pivot table
        self.df['one'] = 1
        
        # create pivot table now
        self.df_pivot = (pd.pivot_table(self.df
                                ,values=['one']
                                ,columns=columns
                                ,index=index
                                ,aggfunc = {'one':'sum'}))
        
        # from MultiIndex to Index
        self.df_pivot.columns = self.df_pivot.columns.to_series().str.join('_')
        # all in the same level as a flat DataFrame
        self.df_pivot = self.df_pivot.reset_index()
        
        # rename the columns
        for col in self.df_pivot.columns[2:]:
            self.df_pivot = self.df_pivot.rename(columns = {col: col.replace('one_','')})

        # we drop this column that was useful for creating the pivot table
        self.df.drop(['one'],axis=1,inplace=True)
        
        # fill NAs with 0 and making all columns integer type
        self.df_pivot = self.df_pivot.fillna(0)
        for col in self.df_pivot.columns[1:]:
            self.df_pivot[col] = self.df_pivot[col].astype(int)

    def generate_chart(self, threshold):
        
        """
        threshold = if the action was made at least 1 time, 2 times, etc.
        we assume a threshold = 1 for the next comments
        """

        # generate empty chart
        self.df_chart = pd.DataFrame({'event': [],
                                      'penetration': [],
                                      'conversion': []})
        
        # we make and copy and use this one, in order not to alter the original df_pivot
        df_pivot_copy = self.df_pivot.copy()

        # first cols are user_id and conversion (yes or no)
        # for every events column, calculate the conversion and penetration
        for col in df_pivot_copy.columns[2:]:
            
            # it's 1 if the action was made same or more times than the threshold
            df_pivot_copy[col] = np.where(df_pivot_copy[col]>=threshold, 1, 0)

            ##### ------------ penetration calculation ------------ #####
            
            # let's assume now threshold of 1 for the following comments
            
            # how many used this feature at least 1, and how many never used it
            for_penetration = df_pivot_copy[col].value_counts()

            # if no user used it, or all of them, we ignore it
            if len(for_penetration) != 2:
                continue

            # penetration calculation
            _penet = for_penetration[1] / (for_penetration[0] + for_penetration[1])

            
            ##### ------------ conversion calculation ------------ #####
            
            converted = df_pivot_copy.columns[1]
            
            # how many users, that used this feature, converted and how many didn't
            for_conversion = df_pivot_copy[df_pivot_copy[col]>0][converted].value_counts()

            # if no user converted, or all of them, we ignore it
            if len(for_conversion) != 2:
                continue

            # conversion calculation
            _conv = for_conversion[1] / (for_conversion[0] + for_conversion[1])

            
            ### we compile the info for each feature in a dataframe

            df_temp = pd.DataFrame({'event': [col],
                                    'penetration': [_penet],
                                    'conversion': [_conv]
                                    })
            
            # for each column, we concat the results
            self.df_chart = pd.concat([self.df_chart,df_temp])

        # organize the columns
        self.df_chart = self.df_chart[['event','penetration','conversion']]

    def plot_bcg(self, fontsize=12, dotsize=80, text_rotation=20,xytext=(-1,5),
                       color='royalblue', alpha=0.9, zoom=0, 
                       xlabel_size=20, ylabel_size=20, 
                       xlabel_pad=20, ylabel_pad=20,
                       tickslabel_size = 20,
                       x_parameter = 'penetration',
                       grid=False):
        
        # what are going to be the axes
        if x_parameter == 'penetration':
            y_parameter = 'conversion'
        elif x_parameter == 'conversion':
            y_parameter = 'penetration'
        
        # we put the data in np array to plot them
        y = np.array(self.df_chart[y_parameter])
        x = np.array(self.df_chart[x_parameter])
        
        # we do the scatter plot
        plt.scatter(x, y, s=dotsize, c=[color]*(len(x)), alpha=alpha)

        # we get all unique actions
        actions = np.array(self.df_chart.event)

        # we add the labels and all their properties
        plt.xlabel(x_parameter, size = xlabel_size, labelpad = xlabel_pad)
        plt.ylabel(y_parameter, size = ylabel_size, labelpad = ylabel_pad)
        plt.tick_params(axis='both', which='major', labelsize = tickslabel_size)

        # we add all text next to the data points
        for i, txt in enumerate(actions):
            plt.annotate(txt, (x[i], y[i]), xytext=xytext, textcoords='offset points', fontsize=fontsize, rotation=text_rotation)

        # if zoom option is not selected, we plot all conversion and penetration range ([0,1])
        if zoom != 1:

            plt.axhline((1)/2, color='grey',linestyle='--',linewidth=1.5)
            plt.axvline((1)/2, color='grey',linestyle='--',linewidth=1.5)

            plt.xlim(0, 1)
            plt.xticks(np.linspace(0,1.1,11,endpoint=False))

            plt.ylim(0, 1)

        # if zoom option is selected, we plot only the area wher there are data points
        elif zoom==1:

            # re-arrange axes
            x_axis_max = np.round(self.df_chart[x_parameter].max(),1)+0.05
            x_axis_min = max(0,np.round(self.df_chart[x_parameter].min(),1)-0.05)

            y_axis_max = np.round(self.df_chart[y_parameter].max(),1)+0.05
            y_axis_min = max(0,np.round(self.df_chart[y_parameter].min(),1)-0.05)

            plt.xlim(x_axis_min, x_axis_max)
            plt.ylim(y_axis_min, y_axis_max)

            plt.xticks(np.linspace(x_axis_min, x_axis_max, int(np.round((x_axis_max-x_axis_min)/0.05)), endpoint=False))
            
            plt.axvline((x_axis_max+x_axis_min)/2, color='grey',linestyle='--',linewidth=1.5)
            plt.axhline((y_axis_max+y_axis_min)/2, color='grey',linestyle='--',linewidth=1.5)

            
        plt.grid(grid)
        plt.show()
