import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt
import tushare as ts

def init_ts():
  ts.set_token('05601a1e82504ef17e2296a01c80d64530362ce80e41f614245ab6ae')
  pro = ts.pro_api()
  return pro

def get_total_stock_info(pro):
  pass

def main():
    print('Hello World!')


if __name__ == "__main__":
  main()  
