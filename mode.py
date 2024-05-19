import sys
import os
import pandas as pd

sys.path.append(os.path.join(os.path.dirname(__file__), 'Hotels'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Activity'))
                                 
from Activity import recommendActivity
import pandas as pd
from Hotels.final_hotel_recc import recommend_hotel

if __name__ == '__main__':
    
    ## input Activity
    ## ## HERE 
    days = 3
    city = 'Đà Nẵng'
    types = types = ['Du lịch tâm linh' , 'Du lịch văn hóa & nghệ thuật'  ] 
    df =  pd.read_csv('./Activity/data/activity.csv')
    recommend = recommendActivity.ActivityRecommend(days , city , types , df )
    recommend.getListPhase1()
    
    listIDActivity = recommend.lstIDActivity
    spendingActivity = recommend.budgetActivity
    print(listIDActivity , spendingActivity)
    ##input Hotel
    user_id = 1
    amenities_input = [0, 1, 2]  # Assuming the user prefers 'Bữa sáng', 'Wifi miễn phí', 'Bãi đậu xe'
    city = 'Đà Nẵng'
    budget = 100000  # Assuming the user has a budget of 100000

    # Call the recommend_hotel function with the example input
    recommendations = recommend_hotel(user_id, amenities_input, city, budget)
    
    # Print the recommendations
    print(recommendations)

    