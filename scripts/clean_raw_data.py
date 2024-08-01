import numpy as np
import pandas as pd

train = pd.read_csv("data/medal_smaller_train.csv")
validation = pd.read_csv("data/medal_smaller_validation.csv")
test = pd.read_csv("data/medal_smaller_test.csv")
print("Train dataset length:", len(train))
print("Validation dataset length:", len(validation))
print("Test dataset length:", len(test))

max_length = 200
max_location = max_length - 3 # minus [CLS] and [SEP] tokens added and index offset

def process_location(location):
    return list(map(int, eval(location)))[0]

def process_label(label):
    return eval(label)[0]

# Reading and processing training data
train_df = pd.read_csv('data/medal_smaller_train.csv')
#train_df['location'] = train_df['location'].map(process_location)
#train_df['label'] = train_df['label'].map(process_label)
#train_df['abbreviation'] = train_df.apply(lambda row: row['text'].split()[row['location']], axis=1)
train_df = train_df[train_df['location'] <= max_location]

# Reading and processing validation data
val_df = pd.read_csv('data/medal_smaller_validation.csv')
# val_df['location'] = val_df['location'].map(process_location)
# val_df['label'] = val_df['label'].map(process_label)
# val_df['abbreviation'] = val_df.apply(lambda row: row['text'].split()[row['location']], axis=1)
val_df = val_df[val_df['location'] <= max_location]

# Reading and processing test data
test_df = pd.read_csv('data/medal_smaller_test.csv')
# test_df['location'] = test_df['location'].map(process_location)
# test_df['label'] = test_df['label'].map(process_label)
# test_df['abbreviation'] = test_df.apply(lambda row: row['text'].split()[row['location']], axis=1)
test_df = test_df[test_df['location'] <= max_location]

train_df.to_parquet("data/medal_smaller_train_df.parquet")
val_df.to_parquet("data/medal_smaller_val_df.parquet")
test_df.to_parquet("data/medal_smaller_test_df.parquet")

print("Data cleaned and DFs saved in data folder.")
