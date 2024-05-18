from Hotel_MLS import *
import pandas as pd
from pyspark.sql import SparkSession

def create_spark_session():
    return SparkSession.builder \
        .appName("MyApp") \
        .config("spark.local.dir", "E:/SparkTemp") \
        .getOrCreate()


def recommend_hotel(user_id, city):
    csvHotelInfo = r"E:\Grab Final Prj\combined_hotel_data2.csv"
    csvRatingInfo = r"E:\Grab Final Prj\TRAVELPLANNING\Hotels\user_profiling_updated.csv"

    # when entering a new user we do have to retrain the entire model
    ratingsSpark, hotels = initial_files(csvHotelInfo, csvRatingInfo)
    calculateSparsity(ratingsSpark)
    train, test = dataSplit(ratingsSpark)
    best_model = MF_ALS(train, test)
    recommendations_df = recommendations(best_model, user_id, hotels, city)
    recommendations_df.toPandas().to_csv('recommended_hotels.csv', index=False)

    return recommendations_df

recommend_hotel(1, 'Đà Nẵng')


