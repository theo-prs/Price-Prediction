# Price-Prediction

# NASDAQ\NYSE\LSE Stock Price Prediction

#Description:

This Python script extracts stock prices from CSV files, calculates the necessary data for predictions, and exports the results to a new CSV file. The script processes files from a specified directory and generates predictions for stock prices based on the existing data.

#Table of Contents
Requirements
Installation
Usage
CSV File Structure

#Requirements:
Python 3.7 or higher

#Installation

1. Clone this repository:
Git clone https://github.com/theo-prs/Price-Prediction.git

2. Navigate to the project directory:
cd project

3. Install the dependencies:
pip install numpy pandas

#Usage
1. Ensure you have the necessary CSV files in the directory specified in the directory variable of the script (C:\\Users\\theod\\OneDrive\\Desktop\\LSEG Proiect\\NASDAQ).
2. Modify the start_date variable in the script to set the desired start date (format YYYY-MM-DD).
3. Run the script:
python Stock_Price_Prediction.py
4. The script will process the files and generate an output CSV file for each processed file. The output will be saved in the same directory with an _output suffix.

#CSV File Structure
Each input CSV file must have the following structure:

No header
Columns: code, date, price
Date format: DD-MM-YYYY
