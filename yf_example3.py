"""
Module: yf_example3
Purpose: Download stock price data for Qantas for a given year and save the information in a CSV file.
"""

import os
import yf_example2
import toolkit_config as cfg


def qan_prc_to_csv(year):
    """
    Download Qantas stock prices for a given year into a CSV file.

    Parameters:
        year (int): The year for which to download the data.

    Purpose:
        Download Qantas stock prices for a given year into a CSV file.
        The name of this file will be qan_prc_YYYY.csv, where the YYYY stands for the year in 'year'.
        This file will be saved under the data folder. The location of this folder is determined by the toolkit_config module.
    """
    start_date = f"{year}-01-01"
    end_date = f"{year}-12-31"
    file_name = f"qan_prc_{year}.csv"
    file_path = os.path.join(cfg.DATADIR, file_name)
    yf_example2.yf_prc_to_csv('QAN.AX', file_path, start_date, end_date)


if __name__ == "__main__":
    # Test case to download data for year 2020
    qan_prc_to_csv(2020)
