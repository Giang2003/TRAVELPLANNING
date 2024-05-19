import pandas as pd
import geopy.distance

def nightOpenTime(df , city):
    night = []
    timeNight = [0,1]
    df = df[ df['city'] == city]
    df =   df[(df['openTime'].isna() == False) | (df['closeTime'].isna() == False) ]
    
    for i , val in enumerate(df['openTime']):
        getTime,_ = str(val).split(':')
        if int(getTime) >= 16:
            night.append(df['idActivity'][i])

    for i , val in enumerate(df['closeTime']):
        getTime,_ = str(val).split(':')
        if int(getTime) > 17 or int(getTime) in timeNight:
            night.append(df['idActivity'][i])
            
    return night


def getListPhase1( types = ['Du lịch tâm linh' , 'Du lịch văn hóa & nghệ thuật'  ]  , city ='Hồ Chí Minh'  ): 
    
    df = pd.read_csv('data/activity.csv')
    getDF = pd.DataFrame(columns=df.columns)
    for val in types:
        getDF2 =  df[(df['typeActivity'] == val) & (df['city'] == city )  ]
        getDF  = pd.concat([getDF,getDF2])

    weight_rating = 0.06
    weight_comments = 0.04
 
    lstRateActivity    = getDF['rateActivity'].apply(lambda x: x * weight_rating  if x != 'nan' else 3* weight_rating)  
    lstCommentActivity =  getDF['numComment'].apply(lambda x:  x * weight_rating  if x != 'nan' else 100* weight_comments) 
    getDF['popularity'] = [sum(i) for i in zip(lstRateActivity,lstCommentActivity)]
    getDF.sort_values(by='popularity' , ascending=False  , inplace=True)
    return getDF

def getDistance2Point(point1, point2):
    if point1 == "(0, 0)" or point2 == "(0, 0)":
        return 1000
    _,lat1 , _ , lon1,*_ = point1.split("'")
    _,lat2 , _ , lon2,*_ = point2.split("'")
    coords_1 = (lat1,lon1)
    coords_2 = (lat2,lon2)  
    print(geopy.distance.geodesic(coords_1, coords_2).km)

    
