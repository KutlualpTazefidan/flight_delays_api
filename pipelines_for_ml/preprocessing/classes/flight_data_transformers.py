from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np
from geopy.distance import geodesic

class AddAdditionalFlightDataFeatures(BaseEstimator, TransformerMixin):
    """
    A transformer to add custom features to the dataset.

    This transformer adds custom features such as time-related features, elevation differences,
    flight time, average flight speed, international flight indicator, airline code, and more.

    Attributes:
        None

    Methods:
        fit(self, X, y=None):
            Fit the transformer to the data (not used).
        transform(self, X):
            Transform the input DataFrame by adding custom features.

    """
    def fit(self, X, y=None):
        """
        Fit the transformer to the data (not used).

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            self: The transformer object.
        """
        return self
    
    def transform(self, X):
        """
        Transform the input DataFrame by adding custom features.

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            pd.DataFrame: The transformed DataFrame with custom features.
        """
        
        # Convert columns 'sta', 'std', and 'datop' to datetime format with specified formats#
        # X['sta'] = X.apply(lambda row: pd.to_datetime(row['sta'], format='%Y-%m-%d %H.%M.%S') if '.' in row['sta'] else pd.to_datetime(row['sta'], format='%Y-%m-%d %H:%M:%S'), axis=1)
        X['sta'] = pd.to_datetime(X['sta'], format='%Y-%m-%d %H:%M:%S')
        X['std'] = pd.to_datetime(X['std'], format='%Y-%m-%d %H:%M:%S')
        X['datop'] = pd.to_datetime(X['datop'], format='%Y-%m-%d')
        
        # Extract time components from 'std' and 'sta', and remove colons from time strings
        X['std_time'] = X['std'].dt.time
        X['sta_time'] = X['sta'].dt.time
        # print("std_time",X['std_time'].astype(str).str.replace(':', ''))
        X['std_time'] = X['std_time'].astype(str).str.replace(':', '').astype(float)
        X['sta_time'] = X['sta_time'].astype(str).str.replace(':', '').astype(float)
        
        # Calculate the elevation difference between arrival and departure airports
        X['elevation_dif'] = (X['arr_elevation'] - X['dep_elevation'])
        
        # Calculate flight time in minutes by subtracting 'std' from 'sta' and converting to seconds
        X['flight_time_in_min'] = (X['sta'] - X['std']).dt.total_seconds() / 60
        
        # Calculate additional features
        X['average_flight_speed_km_h'] = (X['flight_distance_in_km'] * 60 / X['flight_time_in_min']).round().astype(float)
        # X['international_flight'] = np.where(X['arr_country'] != X['dep_country'], 1, 0).astype(float)
        X['international_flight'] = np.where(X['arr_country'] != X['dep_country'], 'international', 'domestic')
        X['airline_code'] = X['fltid'].str[:2]
        # Extract year, month, and day components
        X['year'] = X['datop'].dt.year.astype(float)
        X['month'] = X['datop'].dt.month.astype(float)
        X['day'] = X['datop'].dt.day.astype(float)
        X['datop'] = X['datop'].astype(str).str.replace('-', '').astype(float)
        
        # Create the seasons column
        X.loc[(X['month'] < 3) | (X['month'] == 12), 'season'] = 'winter'
        X.loc[(X['month'] >= 3) & (X['month'] < 6), 'season'] = 'spring' 
        X.loc[(X['month'] >= 6) & (X['month'] < 9), 'season'] = 'summer' 
        X.loc[(X['month'] >= 9) & (X['month'] < 12), 'season'] = 'autumn'
        
        return X
    
    def get_state(self):
        # Return a dictionary with any essential attributes
        return {}

    @classmethod
    def from_state(cls, state):
        # Create an instance of the class using the state dictionary
        return cls()
    
    
class CalculateFlightDistance(BaseEstimator, TransformerMixin):
    """
    A transformer to calculate the flight distance in kilometers.

    This transformer calculates the great-circle distance between departure and arrival coordinates
    and adds it as a new column 'flight_distance_in_km' to the DataFrame.

    Attributes:
        None

    Methods:
        fit(self, X, y=None):
            Fit the transformer to the data (not used).
        transform(self, X):
            Transform the input DataFrame by calculating flight distances.

    """
    def fit(self, X, y=None):
        """
        Fit the transformer to the data (not used).

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            self: The transformer object.
        """
        return self
    
    def transform(self, X):
        """
        Transform the input DataFrame by calculating flight distances.

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            pd.DataFrame: The transformed DataFrame with flight distances.
        """
        def calculate_distance(row):
            dep_coords = (row['dep_lat'], row['dep_lon'])
            arr_coords = (row['arr_lat'], row['arr_lon'])
            distance = geodesic(dep_coords, arr_coords).kilometers
            return int(round(distance, 0))
        distance = X.apply(calculate_distance, axis=1)
        X['flight_distance_in_km'] = float(distance)
        return X

    def get_state(self):
        # Return a dictionary with any essential attributes
        return {}

    @classmethod
    def from_state(cls, state):
        # Create an instance of the class using the state dictionary
        return cls()