""" zid_project1.py

"""
import json
import os

import toolkit_config as cfg

# ----------------------------------------------------------------------------
# Location of files and folders
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' strings with the appropriate
#   expressions.
# IMPORTANT:
#   - Use the appropriate method from the `os` module to combine paths
#   - Do **NOT** include full paths like "C:\\User...". You **MUST* combine
#     paths using methods from the `os` module
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
ROOTDIR = os.path.join(cfg.PRJDIR, "project1")
DATDIR = os.path.join(ROOTDIR, "data")
TICPATH = os.path.join(ROOTDIR, "TICKERS.txt")
# ----------------------------------------------------------------------------
# Variables describing the contents of ".dat" files
# Instructions:
#   - Replace the '<COMPLETE THIS PART>' string with the appropriate
#     expression.
#   - See the assessment description for more information
# ----------------------------------------------------------------------------
# NOTE: `COLUMNS` must be a list, where each element is a column name in the
# order they appear in the ".dat" files
COLUMNS = ['Volume', 'Date', 'Adj Close', 'Close', 'Open', 'High']

# NOTE: COLWIDTHS must be a dictionary with {<col> : <width>}, where
# - Each key (<col>) is a column name in the `COLUMNS` list
# - Each value (<width>) is an **integer** with the width of the column, as
#   defined in your README.txt file
#
COLWIDTHS = {'Volume': 14, 'Date': 11, 'Adj Close': 19, 'Close': 10, 'Open': 6, 'High': 20}


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def get_tics(pth):
    """ Reads a file containing tickers and their corresponding exchanges.
    Each non-empty line of the file is guaranteed to have the following format:

    "XXXX"="YYYY"

    where:
        - XXXX represents an exchange.
        - YYYY represents a ticker.

    This function should return a dictionary, where each key is a properly formatted
    ticker, and each value the properly formatted exchange corresponding to the ticker.

    Parameters
    ----------
    pth : str
        Full path to the location of the TICKERS.txt file.

    Returns
    -------
    dict
        A dictionary with format {<tic> : <exchange>} where
            - Each key (<tic>) is a ticker found in the file specified by pth (as a string).
            - Each value (<exchange>) is a string containing the exchange for this ticker.

    Notes
    -----
    The keys and values of the dictionary returned must conform with the following rules:
        - All characters are in lower case
        - Only contain alphabetical characters, i.e. does not contain characters such as ", = etc.
        - No spaces
        - No empty tickers or exchanges

    """
    tickers = {}
    with open(pth, 'r') as file:
        for line in file:
            if line.strip():  # Check if line is not empty
                parts = line.strip().split("=")
                if len(parts) == 2:
                    ticker = parts[1].strip().lower().strip('"')
                    exchange = parts[0].strip().lower().strip('"')
                    if ticker and exchange:  # Check if ticker and exchange are not empty
                        tickers[ticker] = exchange
    return tickers


# Example usage:
if __name__ == "__main__":
    pth = r"C:\Users\HP\pythonProject\toolkit\project1\TICKERS.txt"
    tics = get_tics(pth)
    print(tics)


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------


def read_dat(tic):
    """ Returns a list with the lines of the ".dat" file containing the stock
    price information for the ticker `tic`.


    Parameters
    ----------
    tic : str
        Ticker symbol, in lower case.

    Returns
    -------
    list
        A list with the lines of the ".dat" file for this `tic`. Each element
        is a line in the file, without newline characters (e.g. '\n')


    Hints (optional)
    ----------------
    - Create a variable with the location of the relevant file using the `os`
      module, the `DATDIR` constant, and f-strings.

    """
    # IMPORTANT: The answer to this question should NOT include full paths
    # like "C:\\Users...". There should be no forward or backslashes.
    # Construct the file path
    dat_file_path = os.path.join(DATDIR, f"{tic}_prc.dat")

    # Read the contents of the file and return as a list of lines
    with open(dat_file_path, 'r') as file:
        lines = file.readlines()

    # Remove newline characters from each line
    lines = [line.strip() for line in lines]

    return lines


# Example usage (outside the function)
if __name__ == "__main__":
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    tic = tics[0]
    lines = read_dat(tic)
    # Print the first line in the file
    print(f'The first line in the dat file for {tic} is:')
    print(lines[0])
# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def line_to_dict(line):
    """Returns the information contained in a line of a ".dat" file as a
    dictionary, where each key is a column name and each value is a string
    with the value for that column.

    This line will be split according to the field width in `COLWIDTHS`
    of each column in `COLUMNS`.

    Parameters
    ----------
    line : str
        A line from ".dat" file, without any newline characters

    Returns
    -------
    dict
        A dictionary with format {<col> : <value>} where
        - Each key (<col>) is a column in `COLUMNS` (as a string)
        - Each value (<value>) is a string containing the correct value for
          this column.

    Hints (optional)
    ----------------
    - Your solution should include the constants `COLUMNS` and `COLWIDTHS`
    - For each line in the file, extract the correct value for each column
      sequentially.

    """
    # Initialize an empty dictionary to store column values
    result = {}

    # Define the starting index for each column
    start = 0
    for i in COLUMNS:
        # Get the width of the column
        width = COLWIDTHS[i]

        # Extract the value for the current column based on the width
        value = line[start:start + width].strip()

        # Add the column name and value to the dictionary
        result[i] = value

        # Update the start index for the next column
        start += width

    return result


# Example usage (outside the function)
if __name__ == "__main__":
    pth = TICPATH
    tics = sorted(list(get_tics(pth).keys()))
    lines = read_dat(tics[0])
    dic = line_to_dict(lines[0])
    print(dic)


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def verify_tickers(tic_exchange_dic, tickers_lst=None):
    """Verifies if the tickers provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        tic_exchange_dic : dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----
        If tickers_lst is not None, raise an Exception if any of the below rules are violated:
            1. tickers_lst is an empty list.

            2. tickers_lst contains a ticker that does not correspond to a key tic_exchange_dic

               Example:
               If tic_exchange_dic is {'tsm':'nyse', 'aal':'nasdaq'},
               tickers_lst = ['aal', 'Tsm'] would raise an Exception because
               'Tsm' is not a key of tic_exchange_dic.

    """
    # Check if tickers_lst is provided
    if tickers_lst is not None:
        # Rule 1: Check if tickers_lst is an empty list
        if not tickers_lst:
            raise Exception("tickers_lst is an empty list.")

        # Rule 2: Check if any ticker in tickers_lst is not a key in tic_exchange_dic
        for ticker in tickers_lst:
            if ticker not in tic_exchange_dic:
                raise Exception(f"Ticker '{ticker}' is not a valid ticker.")


# Example usage:
if __name__ == "__main__":
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aal', 'Tsm']
    verify_tickers(tic_exchange_dic, tickers_lst)


# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------

def verify_cols(col_lst=None):
    """Verifies if the column names provided are valid according to the rules provided in the Notes.
        If a rule is broken, this function should raise an Exception.

        Parameters
        ----------
        col_lst : list, optional
            A list containing column names (as strings) to be verified

        Returns
        -------
        None
            This function does not return anything

        Notes
        -----_
        If collst is not None, raise an Exception if any of the below rules are violated:
            1. col_lst is an empty list.

            2. col_lst contains a column that is not found in `COLUMNS`.

               Example:
               If COLUMNS = ['Close', 'Date'],
               col_lst = ['close'] would raise an Exception because 'close' is not found in `COLUMNS`

    """
    # Check if col_lst is provided
    if col_lst is not None:
        # Rule 1: Check if col_lst is an empty list
        if not col_lst:
            raise Exception("col_lst is an empty list.")

        # Rule 2: Check if any column in col_lst is not found in COLUMNS
        for column in col_lst:
            if column not in COLUMNS:
                raise Exception(f"Column '{column}' is not a valid column.")


# Example usage:
if __name__ == "__main__":
    col_lst = ['Volume', 'close', 'Open']
    verify_cols(col_lst)


# ----------------------------------------------------------------------------
#   Please complete the body of this function, so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_data_dict(tic_exchange_dic, tickers_lst=None, col_lst=None):
    """Returns a dictionary containing the data for the tickers specified in tickers_lst.
        An Exception is raised if any of the tickers provided in tickers_lst or any of the
        column names provided in col_lst are invalid.

        Parameters
        ----------
        tic_exchange_dic: dict
            A dictionary returned by the `get_tics` function

        tickers_lst : list, optional
            A list containing tickers (as strings)

        col_lst : list, optional
            A list containing column names (as strings)

        Returns
        -------
        dict
            A dictionary with format {<tic> : <data>} where
            - Each key (<tic>) is a ticker in tickers_lst (as a string)
            - Each value (<data>) is a dictionary with format
                {
                    'exchange': <tic_exchange>,
                    'data': [<dict_0>, <dict_1>, ..., <dict_n>]
                }
              where
                - <tic_exchange> refers to the exchange that <tic> belongs to in lower case.
                - <dict_0> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[0]),
                  but that only contains the columns listed in col_lst
                - <dict_n> refers to the dictionary returned by line_to_dict(read_dat(<tic>)[-1]),
                  but that only contains the columns listed in col_lst

        Notes
        -----
        - Please refer to the assessment description for an example of what the returned dictionary should look like.
        - If tickers_lst is None, the dictionary returned should contain the data for
          all tickers found in tic_exchange_dic.
        - If col_lst is None, <dict_0>, <dict_1>, ... should contain all the columns found in `COLUMNS`

        Hints (optional)
        ----------------
        - To check if tickers_lst contains any invalid tickers, you can call `verify_tickers`
        - To check if col_lst contains any invalid column names, you can call `verify_cols`
        - This function should call the `read_dat` and `line_to_dict` functions

    """
    # Verify tickers_lst and col_lst
    if tickers_lst is not None:
        verify_tickers(tic_exchange_dic, tickers_lst)
    if col_lst is not None:
        verify_cols(col_lst)

    # Initialize the result dictionary
    result = {}

    # Iterate over tickers_lst or all tickers if tickers_lst is None
    for ticker in (tickers_lst or tic_exchange_dic.keys()):
        exchange = tic_exchange_dic[ticker.lower()]  # Get the exchange for the ticker
        data = []

        # Read the data for the ticker and convert each line to a dictionary
        for line in read_dat(ticker.lower()):
            data_dict = line_to_dict(line)

            # If col_lst is provided, filter the dictionary to include only columns in col_lst
            if col_lst:
                data_dict = {col: data_dict[col] for col in col_lst}
            else:
                # If col_lst is None, include all columns from COLUMNS
                data_dict = {col: data_dict[col] for col in COLUMNS}

            data.append(data_dict)

        # Add the ticker data to the result dictionary
        result[ticker.lower()] = {'exchange': exchange, 'data': data}

    return result


# Example usage:
if __name__ == "__main__":
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)

    for tic in tickers_lst:
        data_dict[tic]['data'] = data_dict[tic]['data'][:3]

    print(data_dict)

# ----------------------------------------------------------------------------
#   Please complete the body of this function so it matches its docstring
#   description. See the assessment description file for more information.
# ----------------------------------------------------------------------------
def create_json(data_dict, pth):
    """Saves the data found in the data_dict dictionary into a
        JSON file whose name is specified by pth.

        Parameters
        ----------
        data_dict: dict
            A dictionary returned by the `create_data_dict` function

        pth : str
            The complete path to the output JSON file. This is where the file with
            the data will be saved.


        Returns
        -------
        None
            This function does not return anything

    """
    with open(pth, 'w') as json_file:
        json.dump(data_dict, json_file)


# ----------------------------------------------------------------------------
#    Please put your answers for the last question here:
# ----------------------------------------------------------------------------
    """
    1. There are various advantages to configuring the file and folder locations as mentioned in Step 1 using 
    expressions for the constants ROOTDIR, DATDIR, and TICPATH:
    
        a). The code becomes platform-independent by constructing file paths using the appropriate methods from the os 
        module. This indicates that the code won't need to be modified in order to function properly on Windows, Linux, 
        and macOS. 
        
        b). More flexibility is added to the code. Since the file paths are relative to these base locations, they will
        remain valid even if the project folder or package location changes.
        
        c). Using constants such as TICPATH, DATDIR, and ROOTDIR to express file paths improves readability and 
        maintainability of the code. In the event that the file locations need to be modified in the future, it makes 
        it simple to understand where the files are located.
        
    2.  Evaluate both hypotheses:
    
        a). Investors’ evaluations of those firms:
            According to hypothesis a, the negative sentiment expressed in the article reflects investors' assessment 
            of the company's performance based on available information, including the company's fundamentals. As a 
            result, investors are likely to respond to negative sentiment by selling stocks, leading to a short-term 
            decline in stock returns. In the long run, equity returns may not recover or may continue to decline if 
            corporate fundamentals deteriorate or if negative sentiment can be justified.
            
        b). Valuable information beyond firm fundamentals:
            According to hypothesis b, the negative sentiment in the article may contain valuable information beyond 
            the fundamentals of the company. The negative sentiment in the article may indicate an underlying issue or 
            event that the market has not yet fully recognized. As a result, stock returns are likely to continue to 
            decline over the long term as more information comes in and investors adjust their expectations.
            
        In summary, therefore, the second hypothesis (valuable information beyond the fundamentals of the company) 
        seems more likely to be correct. If negative sentiment simply reflected investors' assessment based on company 
        fundamentals, expect some reversal in equity returns over the long term. But over the long term, the absence 
        of a reversal suggests that negative sentiment may indeed contain valuable information beyond traditional 
        company fundamentals.

    3.  evaluate the short-run predictability for the trading volume with reason
    
        a). Directly affect investor sentiment:
            The negative sentiment expressed in the article could cause investors to panic and become more cautious 
            or concerned about the company's prospects, leading to a change in trading volume.
            In addition, short-term traders and speculators, who may actively trade based on the impact of negative 
            news on the company's stock price and trading volume.
        b). Growth in volatility
            Negative sentiment can create volatility and uncertainty in the market, and high levels of uncertainty, 
            and the unpredictability of market reactions to negative sentiment, may also encourage more trading 
            activity as investors try to adjust their positions based on new information.
        c). Herd behavior
            Negative sentiment can affect market sentiment and trigger herd behavior among investors. May prompt 
            investors to go with the flow and adjust their trading activity accordingly, resulting in short-term 
            predictability of trading volumes as investors collectively react to the news.
        
    """

def _test_create_json(json_pth):
    """ Test function for the `create_json_ function.
    This function will save the dictionary returned by `create_data_dict` to the path specified.

    """
    pth = TICPATH
    tic_exchange_dic = get_tics(pth)
    tickers_lst = ['aapl', 'baba']
    col_lst = ['Date', 'Close']
    data_dict = create_data_dict(tic_exchange_dic, tickers_lst, col_lst)
    create_json(data_dict, json_pth)
    print(f'Data saved to {json_pth}')

if __name__ == "__main__":
    _test_create_json(os.path.join(DATDIR, 'data.json'))  # Save the file to data/data.json






