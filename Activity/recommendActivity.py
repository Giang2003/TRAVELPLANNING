import pandas as pd
import numpy as np

class ActivityRecommend:
    def __init__(self, days : int , city , types : list , df : pd.DataFrame ):

        self.days = days
        self.city = city
        self.types = types
        ## Data to 
        self.df = df
        ## Recommend List ID Activity
        self.lstIDActivity = []
        self.budgetActivity = 0


    def getListPhase1(self): 
        
        getDF = pd.DataFrame(columns=self.df.columns)
        getDF1 = self.df[(self.df['city'] == self.city )]
        for val in self.types:
            getDF2 =  self.df[(self.df['typeActivity'] == val) & (self.df['city'] == self.city )  ]
            getDF  = pd.concat([getDF,getDF2])

            weight_rating = 0.06
            weight_comments = 0.04
 
            lstRateActivity    = getDF['rateActivity'].apply(lambda x: x * weight_rating  if x != 'nan' else 3* weight_rating)  
            lstCommentActivity =  getDF['numComment'].apply(lambda x:  x * weight_rating  if x != 'nan' else 100* weight_comments) 
            getDF['popularity'] = [sum(i) for i in zip(lstRateActivity,lstCommentActivity)]
            getDF.sort_values(by='popularity' , ascending=False  , inplace=True)
            numActivity = self.days * 3
            if len(getDF) < numActivity:
                getDF = pd.concat( [getDF,getDF1])
            
            
            self.lstIDActivity =  getDF['idActivity'][:numActivity]
            self.budgetActivity = sum(getDF['priceActivity'][:numActivity])
      
