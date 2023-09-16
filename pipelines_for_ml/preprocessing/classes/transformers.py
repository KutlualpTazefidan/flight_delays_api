from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder

class ColumnNameFixer(BaseEstimator, TransformerMixin):
    """
    A transformer to fix column names by replacing spaces and hyphens.

    This transformer converts column names to lowercase and replaces spaces and hyphens with underscores.

    Attributes:
        None

    Methods:
        fit(self, X, y=None):
            Fit the transformer to the data (not used).
        transform(self, X):
            Transform the input DataFrame by fixing column names.

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
        Transform the input DataFrame by fixing column names.

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            pd.DataFrame: The transformed DataFrame with fixed column names.
        """
        X.columns = X.columns.str.replace(' ', '_').str.lower().str.replace('-', '_')
        return X

class DropColumns(BaseEstimator, TransformerMixin):
    """
    A transformer to drop specified columns from the dataset.

    This transformer drops a list of specified columns from the input DataFrame.

    Attributes:
        columns_to_drop (list): A list of column names to be dropped.

    Methods:
        fit(self, X, y=None):
            Fit the transformer to the data (not used).
        transform(self, X):
            Transform the input DataFrame by dropping specified columns.

    """
    def __init__(self, columns_to_drop):
        """
        Initialize the transformer with the columns to be dropped.

        Args:
            columns_to_drop (list): A list of column names to be dropped.

        Returns:
            None
        """
        self.columns_to_drop = columns_to_drop

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
        Transform the input DataFrame by dropping specified columns.

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            pd.DataFrame: The transformed DataFrame with specified columns dropped.
        """
        X.drop(self.columns_to_drop, axis=1, inplace=True)
        return X

class LabelEncoderTransformer(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        """
        Initialize the transformer with the columns to be label encoded.

        Args:
            columns (list): A list of column names to be label encoded.

        Returns:
            None
        """
        self.columns = columns
        self.label_encoders = {}

    def fit(self, X, y=None):
        """
        Fit the transformer to the data by creating and fitting label encoders.

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            self: The transformer object.
        """
        for col in self.columns:
            label_encoder = LabelEncoder()
            label_encoder.fit(X[col])
            self.label_encoders[col] = label_encoder
        return self

    def transform(self, X):
        """
        Transform the input DataFrame by applying label encoding to specified columns.

        Args:
            X (pd.DataFrame): The input data.

        Returns:
            pd.DataFrame: The transformed DataFrame with label encoding applied to specified columns.
        """
        X_encoded = X.copy()
        for col, label_encoder in self.label_encoders.items():
            X_encoded[col] = label_encoder.transform(X_encoded[col])
        return X_encoded