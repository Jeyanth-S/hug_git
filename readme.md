# Machine Learning Model Training Repository

A Python project for training a Random Forest classifier on the Iris dataset with performance profiling and automated CI/CD.

## Overview

This repository contains an automated machine learning pipeline that:
- Trains a Random Forest classifier using scikit-learn
- Profiles the training process to measure performance metrics
- Automatically runs on code pushes via GitHub Actions
- Uploads trained model artifacts for download

## Project Structure

```
.
├── train.py                          # Main training script
├── requirments.txt                   # Python dependencies
├── README.md                         # This file
├── .gitignore                        # Git ignore rules
├── .github/
│   └── workflows/
│       └── train.yaml               # GitHub Actions workflow
└── trained-model/
    └── profile.txt                  # Performance profiling results
```

## Requirements

- Python 3.10+
- scikit-learn

### Installation

Install dependencies:

```bash
pip install -r requirments.txt
```

## Usage

### Local Training

Run the training script locally:

```bash
mkdir -p model
python train.py
```

This will:
1. Load the Iris dataset from scikit-learn
2. Train a Random Forest classifier with default parameters
3. Save the trained model to `model/my_model.pkl`
4. Generate performance profiling data in `model/profile.txt`

### Using the Trained Model

```python
import pickle

with open('model/my_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Make predictions
predictions = model.predict(X_new)
```

## Automated Training

The repository includes a GitHub Actions workflow ([`.github/workflows/train.yaml`](.github/workflows/train.yaml)) that automatically:
- Triggers on every push to the main branch
- Sets up Python 3.10 environment
- Installs dependencies
- Runs the training script with profiling
- Uploads the trained model and profiling results as artifacts

You can download the trained artifacts from the GitHub Actions workflow run page.

## Performance Metrics

The training completes in **~0.16 seconds** on the Iris dataset (150 samples, 4 features, 3 classes).

### Profiling Summary

Key performance insights from [trained-model/profile.txt](trained-model/profile.txt):
- **Total function calls**: 213,471
- **Training time**: 0.160 seconds
- **Most time spent in**: `RandomForestClassifier.fit()` (0.156s cumulative)
- **Tree building overhead**: 100 decision trees built in parallel

## Model Details

- **Algorithm**: Random Forest Classifier
- **Dataset**: Iris (150 samples, 4 features, 3 classes)
- **Number of trees**: 100 (default)
- **Output format**: Pickled Python object (`.pkl`)

## Files

- [train.py](train.py) - Training script with cProfile integration
- [requirments.txt](requirments.txt) - Project dependencies
- [.github/workflows/train.yaml](.github/workflows/train.yaml) - CI/CD pipeline configuration
- [.gitignore](.gitignore) - Git ignore configuration

## Notes

- The `trained-model/` and `model/` directories are excluded from version control (see [.gitignore](.gitignore))
- Model artifacts are saved to the local `model/` directory
- Training includes comprehensive performance profiling via Python's `cProfile`
- GitHub Actions automatically uploads artifacts for each workflow run

## License

This project is open source and available under the MIT License.