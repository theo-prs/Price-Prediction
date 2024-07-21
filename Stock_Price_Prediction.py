import numpy as np
import pandas as pd
import os

def get_points_from_date(file, start_date):
    df = pd.read_csv(file, header=None)
    df.columns = ['code', 'date', 'price']
    df['date'] = pd.to_datetime(df['date'], format='%d-%m-%Y')
 
    df = df.sort_values(by='date').reset_index(drop=True)
 
    start_date = pd.to_datetime(start_date)
   
    start_index = df[df['date'] >= start_date].index[0]
 
    if start_index + 10 > len(df):
        raise ValueError("Not enough data points starting from the given date!")
 
    result_df = df.iloc[start_index:start_index + 10]
 
    return result_df

def next_three_values(data_points):
    prices = data_points['price'].tolist()
    n_a = sorted(prices)[-2]
    n = prices[-1]
    n_b = n + (n_a - n) / 2
    n_c = n_b + (n_a - n_b) / 4
    return [n_a, n_b, n_c]

def save_to_csv(file_path, data_points, predicted_prices):
    stock_id = data_points['code'].iloc[0]
 
    output_df = pd.DataFrame(columns=['Stock-ID', 'Timestamp', 'Stock Price'])
 
    data_rows = []
    for _, row in data_points.iterrows():
        data_rows.append({'Stock-ID': stock_id, 'Timestamp': row['date'].strftime('%d-%m-%Y'), 'Stock Price': row['price']})
    last_timestamp = pd.to_datetime(data_points['date'].iloc[-1])
    for i, predicted_price in enumerate(predicted_prices):
        new_timestamp = (last_timestamp + pd.DateOffset(days=i+1)).strftime('%d-%m-%Y')
        data_rows.append({'Stock-ID': stock_id, 'Timestamp': new_timestamp, 'Stock Price': predicted_price})
    
    output_df = pd.concat([output_df, pd.DataFrame(data_rows)], ignore_index=True)
 
    output_file_path = os.path.splitext(file_path)[0] + '_output.csv'
    output_df.to_csv(output_file_path, index=False)
   
    return output_file_path

directory = 'C:\\Users\\theod\\OneDrive\\Desktop\\LSEG Proiect\\NASDAQ'
start_date = '2023-01-01'  
files_to_process = 1

filenames = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

if len(filenames) < files_to_process:
    raise ValueError("Not enough files in the directory to process the specified number of files!")

for i in range(files_to_process):
    file_path = os.path.join(directory, filenames[i])
    print(f"Processing file: {file_path}")
    try:
        data_points = get_points_from_date(file_path, start_date)
        print("Please check the 10 consecutive data points based on the provided start date:")
        print(data_points)
 
        predicted_prices = next_three_values(data_points)
        print("Please check three predicted values for stock prices:")
        print(predicted_prices)
 
        output_file_path = save_to_csv(file_path, data_points, predicted_prices)
        print(f"Results saved to {output_file_path}")
    except Exception as e:
        print(f"An error occurred while processing {file_path}: {e}")