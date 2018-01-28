# Charcoal
Simple character recommender for story writing. Built at Hack@Brown 2018.

## How it works
- Training data comes from [Nate the Snake](http://natethesnake.com/)
  - Label is each character in the text
  - Features are the previous `num_previous` characters (defined in `utils.py`)
- Logistic regression model trained on data using one-hot encodings for the characters
- Flask server allows user to interact with the trained model

## Future Updates
- Generate story feature
- Webcrawl wikipedia for more training data
