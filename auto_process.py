# -*- coding: utf-8 -*-

import numpy as np

designated_time_s = input('Enter first month, in form of MM/YYYY:')
designated_time_e = input('Enter comprison month, in form of MM/YYYY:')
file_name = input('Data file name:')

def read_geometry(filename, ppb, date):
    with open(filename) as f:
        for row in f.readlines()[1:]:
            ppb.append((row.split(',')[3]))
            date.append((row.split(',')[2]))




NO2_ppb = []
record_data = []
monthly_s = []
monthly_e = []

read_geometry(filename = file_name, ppb = NO2_ppb, date = record_data)
NO2_date = list(zip(NO2_ppb, record_data))

def monthly_average_finder(target_zipped_list):
    for n in range(len(record_data)):
        if target_zipped_list[n][1][3:10] == designated_time_s:
            monthly_s.append(target_zipped_list[n][0])
            if monthly_s.count('') >15:
                print('Data invalid first month')
                break
    for n in range(len(record_data)):
        if target_zipped_list[n][1][3:10] == designated_time_e:
            monthly_e.append(target_zipped_list[n][0])
            if monthly_e.count('') >15:
                print('Data invalid comprison month')
                break
            
monthly_average_finder(target_zipped_list = NO2_date)

monthly_s = [x for x in monthly_s if x != '']
monthly_e = [x for x in monthly_e if x != '']

monthly_s = list(map(float, monthly_s))
monthly_array_s = np.array(monthly_s)
print('Average NO2 (ppb) of ' + str(designated_time_s) + ' is ' + str(np.mean(monthly_array_s)))

monthly_e = list(map(float, monthly_e))
monthly_array_e = np.array(monthly_e)
print('Average NO2 (ppb) of ' + str(designated_time_e) + ' is ' + str(np.mean(monthly_array_e)))

percent = ((np.mean(monthly_array_s) - np.mean(monthly_array_e))/ np.mean(monthly_array_s))*100
print('The change is ' + str(percent * -1) + ' %')