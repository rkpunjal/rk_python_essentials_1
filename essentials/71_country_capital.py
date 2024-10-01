import requests
import pandas as pd


def get_country_capital(country):
    url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data[0] and 'capital' in data[0] and data[0]['capital'] and data[0]['capital'][0]:
            capital = data[0]['capital'][0]
            return capital
        else:
            print("didn't find capital info")
            return "Capital not found"
    else:
        return "Capital not found"
# -----------------------------

def get_country_currency(country):
    url = f"https://restcountries.com/v3.1/name/{country}?fullText=true"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data[0] and 'currencies' in data[0]:

            key_name = list(data[0]['currencies'].keys())[0]
            currency_name = data[0]['currencies'][key_name]['name']
            return currency_name
        else:
            print("didn't find currency info")
            return "Currency not found"
    else:
        return "Currency not found"
# -----------------------------

def try_capital():
    while True:
        country_name = input("Enter a country name (or 'x' to quit): ")

        if country_name.lower() == "x":
            print("Exiting the program.")
            break

        capital = get_country_capital(country_name)
        print('--------')
        print(f"The capital of {country_name.capitalize()} is {capital.capitalize()}.")
        print('--------')
# -----------------------------

def create_capitals_data():
    # Load the Excel file
    file_path = 'D:/quiz_brain_workspace/capitals_trial/flag_questions_sorted.xlsx'  # Replace with your file path
    sheet_name = 'Sheet1'
    read_column = 'Country'
    write_column = 'Capital'

    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)


    # # Read the rows of the specified column
    # column_data = df[column_name].tolist()

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        country_name = row[read_column]
        capital_name = get_country_capital(country=country_name)
        print(f"{index+1}, \"{country_name}\", \"{capital_name}\"")
        df.at[index, write_column] = capital_name

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, sheet_name=sheet_name, index=False)

    print(f"Values updated successfully in column '{write_column}'.")
# ----------------------------

def create_currencies_data():
    # Load the Excel file
    file_path = 'D:/quiz_brain_workspace/capitals_trial/flag_questions_sorted.xlsx'  # Replace with your file path
    sheet_name = 'Sheet1'
    read_column = 'Country'
    write_column = 'Currency'

    # Read the Excel file
    df = pd.read_excel(file_path, sheet_name=sheet_name)


    # # Read the rows of the specified column
    # column_data = df[column_name].tolist()

    # Iterate over the rows of the DataFrame
    for index, row in df.iterrows():
        country_name = row[read_column]
        currency_name = get_country_currency(country=country_name)
        print(f"{index+1}, \"{country_name}\", \"{currency_name}\"")
        df.at[index, write_column] = currency_name

    # Save the updated DataFrame back to the Excel file
    df.to_excel(file_path, sheet_name=sheet_name, index=False)

    print(f"Values updated successfully in column '{write_column}'.")
# ----------------------------


if __name__ == "__main__":
    try_capital()
    # create_capitals_data()
    # create_currencies_data()
