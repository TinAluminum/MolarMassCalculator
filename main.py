import pandas as pd
import re
import tkinter

data = pd.read_excel('Molar mass list.xlsx', sheet_name='Sheet1')

def get_molar_mass(element):
    index = data.loc[data["Symbol"] == element].index[0]
    return data.iloc[index, 2]

def seperate(elements):
    list = []
    for element in elements:
        name = ''.join(re.findall(r'[a-zA-Z]', element))
        amount = re.findall(r'\d+', element)
        if len(amount) == 0:
            amount = 1
        else:
            amount = int(amount[0])
        list.append((name, amount))
    return list

def calculate_molar_mass(elements):
    molar_mass = 0
    for element in elements:
        name = element[0]; amount = element[1]
        m_mass = get_molar_mass(name)
        molar_mass += amount*m_mass
        print(name, m_mass, amount)
    return molar_mass

def main():
    user_input = input("input element: ")
    elements = re.findall('[A-Z][^A-Z]*', user_input)
    elements = seperate(elements)
    molar_mass = calculate_molar_mass(elements)
    print("Molar mass: ", molar_mass)

main()






