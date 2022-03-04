# Ignore SKlearn warning
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn


import argparse
import pandas as pd
from model import BaselineModel

parser = argparse.ArgumentParser()
parser.add_argument('--input_csv', default='input.csv')
args = parser.parse_args()

# Load input.csv
with open(args.input_csv) as input_csv:
    df = pd.read_csv(input_csv)

# Run predictions
y_predictions = BaselineModel(model_file_path='src/model.pickle').predict(df)
y_predictions = [round(pred, 2) for pred in y_predictions]

# Save predictions to file
df_predictions = pd.DataFrame({'prediction': y_predictions})
df_predictions.to_csv('predictions.csv', index=False)

print(f'Made {len(y_predictions)} predictions \n')
print('Download the predictions [here](predictions.csv)')
