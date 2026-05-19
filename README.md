# adaboost_classifier

# Mushroom Classification using AdaBoost Classifier

## Overview

This project predicts whether a mushroom is:

- Edible
- Poisonous

using the AdaBoost Classifier Machine Learning algorithm.

The application is developed using Python and deployed using Streamlit.

---

# Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

---

# Machine Learning Algorithm

AdaBoost Classifier

---

# Dataset

Dataset Name:

mushrooms.csv

The dataset contains different mushroom characteristics such as:

- Cap Shape
- Cap Color
- Odor
- Gill Size
- Habitat
- Population

and many more features used to classify mushrooms.

---

# Features Used

Some important features include:

- Cap Shape
- Cap Surface
- Cap Color
- Odor
- Gill Size
- Gill Color
- Stalk Shape
- Habitat

---

# Target Variable

- Edible
- Poisonous

---

# Installation

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# Run the Project

```bash
streamlit run app.py
```

---

# Project Structure

```text
project folder
│
├── app.py
├── mushrooms.csv
├── requirements.txt
├── README.md
```

---

# Sample Test Cases

## Poisonous Mushroom

| Feature | Value |
|---------|--------|
| Odor | foul |
| Gill Size | narrow |
| Habitat | woods |

Prediction:

```text
Poisonous
```

---

## Edible Mushroom

| Feature | Value |
|---------|--------|
| Odor | almond |
| Gill Size | broad |
| Habitat | grasses |

Prediction:

```text
Edible
```

---

# Output

The application predicts whether the mushroom is:

- Edible
- Poisonous

based on mushroom characteristics.

---

# Author

Akshay

Machine Learning Mini Project
