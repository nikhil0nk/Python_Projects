from pytrends.request import TrendReq
import pandas as pd
from openpyxl import load_workbook
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from datetime import datetime
import re

pytrends = TrendReq(hl='en-US', tz=360)

keyword = []
date_time = ''
def get_trend(keyword, date_time):
  pytrends.build_payload(keyword, cat = '0', timeframe = date_time, geo = 'US', gprop = '')
  data_interest = pytrends.interest_over_time()
  data_interest.drop(data_interest.columns[len(data_interest.columns)-1], axis=1, inplace=True)

  # Excel dump
   
  try:
    book = load_workbook("googletrend_data.xlsx")
    writer = pd.ExcelWriter("googletrend_data.xlsx", engine = 'openpyxl')
    writer.book = book
    data_interest.to_excel(writer, sheet_name=keyword[0])
    writer.save()
  except:
    writer = pd.ExcelWriter("googletrend_data.xlsx",engine='xlsxwriter')
    data_interest.to_excel(writer, sheet_name=keyword[0])
    writer.save()
  
  
  # Graphical representation
  plt.xlabel("Date")
  plt.ylabel(keyword[0])
  plt.title("Interest Over Time")
  plt.plot(data_interest, color='blue', label='original')
  plt.plot(data_interest.rolling(window=4).mean(), color='red', label='mean')
  plt.xticks(rotation=90)
  plt.savefig(keyword[0]+"_trend.png")
  plt.close()

  # Log Scale Graph
  data_interest_log = np.log(data_interest)
  plt.xlabel("Date")
  plt.ylabel(keyword[0])
  #plt.yscale("log")
  plt.title("Log Graph: Interest Over Time")
  plt.plot(data_interest_log, color='black', label='log')
  plt.plot(data_interest_log.rolling(window=4).mean(), color='green', label='log mean')
  plt.xticks(rotation=90)
  plt.savefig(keyword[0]+"_log_trend.png")
  plt.close()
  

  dt_mean = re.findall("\d+\.\d+", str(data_interest.mean()))
  dt_mean = float(dt_mean[0])
  dt_last = re.findall(r'\d+', str(data_interest.iloc[-1]))
  dt_last = float(dt_last[0])

  if dt_last >= dt_mean:
    print(keyword[0], "is in \u001b[32muptrend\u001b[37m")
  else:
    print(keyword[0], "is in \u001b[31mdowntrend\u001b[37m")
  
  return data_interest

kw_list = [
  # "Countertop Microwave Ovens", "Stand Mixers", "TVs", "Portable Air Conditioners", "Inkjet Printers",
  # "Air Fryers", "Projectors", "Cordless Drills", "Stand-Up Paddleboards", "Treadmills",
  "Smartwatches"
  ] #List of Categories
for kw in kw_list:
  keyword.append(kw)
  get_trend(keyword, '2018-09-22 2021-09-21')
  keyword.pop()

