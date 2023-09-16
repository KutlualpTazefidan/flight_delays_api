# Pipelines for ML Purposes

Welcome to the documentation for Pipelines for ML Purposes.

This Python package provides a set of custom data preprocessing transformers and a machine learning pipeline for data preparation and machine learning.

## Installation

You can install this package using pip:

```bash
pip install pipelines_for_ml
```

## Usage

### Preprocessing

To use the data preprocessing pipeline, you'll need to import both the pipeline creation function and the custom transformer classes.

Here's how to do it:

```python
from pipelines_for_ml.preprocessing.classes import *

from pipelines_for_ml.preprocessing.flight_data_preprocessing import create_preprocessing_pipeline
```

#### Create the preprocessing pipeline

```python
preprocessing_pipeline = create_preprocessing_pipeline()
```

#### Now you can use:

```python
 preprocessing_pipeline.fit_transform(Data)
```

### Machine Learning

...

## Contributing

If you would like to contribute to this project or report issues, please visit the GitHub repository:
https://github.com/KutlualpTazefidan/pipelines_for_ml

## License

This project is licensed under the MIT License - see the LICENSE file for details.
