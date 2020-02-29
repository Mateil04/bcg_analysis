import numpy as np
from matplotlib import pyplot as plt
from matplotlib import transforms
import seaborn as sns
import pandas as pd

class Generate_BCG:
    
    def __init__(self, df, fontsize = 20, dotsize = 180):
        
        self.df_pivot = df
        self.fontsize = fontsize
        self.dotsize = dotsize
        self.df_chart = pd.DataFrame({'event': [],
                                      'penetration': [],
                                      'conversion': []})
        
    def plot_bcg(self):
        
        
        for col in self.df_pivot.columns[2:]:
            
            self.df_pivot[col] = np.where(self.df_pivot[col]>0, 1, 0)

        for col in self.df_pivot.columns[2:]:
  
            ##### ------------ penetration calculation ------------ #####
            
            # how many used this feature at least 1, and how many never used it
            for_penetration = self.df_pivot[col].value_counts()

            # if no user used it, or all of them, we ignore it
            if len(for_penetration) != 2:
                continue

            _penet = for_penetration[1] / (for_penetration[0] + for_penetration[1])

            
            ##### ------------ conversion calculation ------------ #####
            
            converted = self.df_pivot.columns[1]
            
            # how many users, that used this feature, converted and how many didn't
            for_conversion = self.df_pivot[self.df_pivot[col]>0][converted].value_counts()

            # if no user converted, or all of them, we ignore it
            if len(for_conversion) != 2:
                continue

            _conv = for_conversion[1] / (for_conversion[0] + for_conversion[1])

            
            ### we compile the info for each feature in a dataframe

            df_temp = pd.DataFrame({'event': [col],
                                    'penetration': [_penet],
                                    'conversion': [_conv]
                                    })
            
            #print (df_temp)

            self.df_chart = pd.concat([self.df_chart,df_temp])


        # we put the data in np array for plotting them
        x = np.array(self.df_chart.conversion)
        y = np.array(self.df_chart.penetration)
        colors = ['royalblue']*(len(x))
        plt.scatter(y, x, s=self.dotsize, c=colors, alpha=0.9)

        features = np.array(self.df_chart.event)

        for i, txt in enumerate(features):
            plt.annotate(txt, (y[i], x[i]), xytext=(-35,15), textcoords='offset points', fontsize=self.fontsize)

        plt.axvline((1)/2, color='grey',linestyle='--',linewidth=1.5)
        plt.axvline((0)/1, color='grey',linestyle='--',linewidth=1.5)
        plt.axvline((1)/1, color='grey',linestyle='--',linewidth=1.5)

        plt.axhline((1)/2, color='grey',linestyle='--',linewidth=1.5)

        plt.ylabel('conversion',size=25, labelpad=20)
        plt.xlabel('penetration', size=25, labelpad=20)
        plt.tick_params(axis='both', which='major', labelsize = 20)

        plt.xlim(0, 1)
        plt.xticks(np.linspace(0,1.1,11,endpoint=False))

        plt.ylim(0, 1)

        print ('')
        plt.show()
        
    def df_bcg(self):
        
        return self.df_chart[['event','penetration','conversion']]