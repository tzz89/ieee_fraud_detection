import pickle
import os


def read_config_file():
    pass


def save_schema(dataframe, path="", file_name="schema.pkl"):
    '''
    This function will save the schema (dictionary) of a the dataframe in pickle format
    dataframe: pandas dataframe
    path: folder to store the schema file
    filename: name of the schema file, will automatically add .pkl if not added

    Example usage

    file_name = "raw_schema"
    save_schema(pandas_dataframe ,path="", file_name=file_name)

    with open(file_name+'.pkl', 'rb') as handles:
        loaded_schema = pickle.load(handles)
    print(loaded_schema)
    >> {'TransactionID': dtype('int64'), 'isFraud': dtype('int64'), 
        'TransactionDT': dtype('int64'), 
        'card1': dtype('int64'), 'V330': dtype('float64')}
    '''
    schema = dataframe.dtypes.to_dict()
    if file_name[-4:] != ".pkl":
        file_name = file_name + ".pkl"
    file_location = os.path.join(path, file_name)
    with open(file_location, "wb") as handles:
        pickle.dump(schema, handles, protocol=pickle.HIGHEST_PROTOCOL)
