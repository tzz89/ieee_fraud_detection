import math
import gc
import numpy as np


class DataMemoryReducer():
    '''
    This module attempts to reduce 64 bit datatypes to 32 bit
    '''
    def __init__(self):
        self.float_columns_to_reduce = []
        self.int_columns_to_reduce  = []
        self.__float_min = -3.4028235E+38
        self.__float_max =  3.4028235e+38
        self.__int_min = -2147483648
        self.__int_max = 2147483647
        
            
    def fit(self, pandas_df):
        float_df = pandas_df.select_dtypes(include='float64')
        if len(float_df.columns) == 0:
            print("None of the float columns can be changed")
            
        else: 
            #if all the columns are within range, change all
            if  (np.nanmax(float_df.values) <= self.__float_max) and (np.nanmin(float_df.values) >= self.__float_min):
                self.float_columns_to_reduce = float_df.columns

            else:
                self.float_columns_to_reduce = [] #clear any residuals
                for float_column in float_df.columns:
                    if ((np.nanmax(float_df[float_column].values) <= self.__float_max) and 
                       (np.nanmin(float_df[float_column].values) >= self.__float_min)):
                        self.float_columns_to_reduce.append(float_column)
                     
        del float_df
        gc.collect()
        
        
        int_df = pandas_df.select_dtypes(include='int64')
        if len(int_df.columns) == 0:
            print("None of the int columns can be changed")
        else:    
            #if all the columns are within range, change all
            if  (np.nanmax(int_df.values) <= self.__int_max) and (np.nanmin(int_df.values) >= self.__int_min):
                self.int_columns_to_reduce = int_df.columns
            #check each column one by one
            else:
                self.int_columns_to_reduce = []
                for int_column in int_df.columns:
                    if ((np.nanmax(int_df[int_column].values) <= self.__int_max) and 
                       (np.nanmin(int_df[int_column].values) >= self.__int_min)):
                        self.int_columns_to_reduce.append(int_column)
            
            
        del int_df
        gc.collect()

    def transform(self, pandas_df):
        temp_df = pandas_df.copy()
        temp_df[self.float_columns_to_reduce]= temp_df[self.float_columns_to_reduce].astype('float32')
        gc.collect()
        temp_df[self.int_columns_to_reduce] = temp_df[self.int_columns_to_reduce].astype('int32')
        gc.collect()
        return temp_df
    
    def fit_transform(self, pandas_df):
        self.fit(pandas_df)
        return self.transform(pandas_df)
        