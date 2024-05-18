import pandas as pd
import ast

def clean_benefits(benefits_str):
    # Check for NaN values
    if pd.isna(benefits_str):
        return ''
    
    try:
        # Convert string representation of list to actual list
        benefits_list = ast.literal_eval(benefits_str)
        # Remove items with "+.."
        cleaned_benefits = [benefit.strip() for benefit in benefits_list if not benefit.strip().startswith('+')]
        # Convert list to comma-separated string
        return ', '.join(cleaned_benefits)
    except (ValueError, SyntaxError):
        # If there's an error in conversion, return an empty string
        return ''

def clean_hotel_data(file_path):
    # Load the data
    df = pd.read_csv(file_path)
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Remove the "đ" character from the Price column but keep it as string
    df['Price'] = df['Price'].str.replace('đ', '').str.strip()
    
    # Apply the clean_benefits function to clean the benefits column
    df['Benefits'] = df['Benefits'].apply(clean_benefits)
    
    # Add a Hotel ID column
    df.reset_index(drop=True, inplace=True)
    df['HotelID'] = df.index + 1
    
    # Add a Location column
    # df['Location'] = 'Đà Nẵng'
    
    # Save the cleaned data to a new CSV without the index column
    cleaned_file_path = "cleaned_hotel_data17.csv"
    df.to_csv(cleaned_file_path, index=True)
    
    return df, cleaned_file_path

# Example usage
# file_path = r'E:\Grab Final Prj\cleaned_hotel_data.csv'  # Use raw string
# df = pd.read_csv(file_path)
# df['Rating'] = df['Rating'].astype(str).str.replace(',', '.').str.strip()
# df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
# cleaned_file_path = "cleaned_hotel_data19.csv"
# df.to_csv(cleaned_file_path, index=False)

# # # or file_path = 'E:\\Grab Final Prj\\TRAVELPLANNING\\Hotels\\Hotel_data_DN.csv'  # Use double backslashes

# # df, cleaned_file_path = clean_hotel_data(file_path)
# # print(df.head())
# # print(f"Cleaned data saved to {cleaned_file_path}")


