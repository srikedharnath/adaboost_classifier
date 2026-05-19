
import pandas as pd
import streamlit as st

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import AdaBoostClassifier


st.title("Mushroom Classification using AdaBoost")


df = pd.read_csv("mushrooms.csv")


label_encoders = {}

for col in df.columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le


X = df.drop('class', axis=1)
y = df['class']


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)


cap_shape = st.selectbox(
    "Cap Shape",
    ['x', 'b', 's', 'f', 'k', 'c']
)

cap_surface = st.selectbox(
    "Cap Surface",
    ['s', 'y', 'f', 'g']
)

cap_color = st.selectbox(
    "Cap Color",
    ['n', 'y', 'w', 'g', 'e', 'p', 'b', 'u', 'c', 'r']
)

bruises = st.selectbox(
    "Bruises",
    ['t', 'f']
)

odor = st.selectbox(
    "Odor",
    ['p', 'a', 'l', 'n', 'f', 'c', 'y', 's', 'm']
)


input_data = pd.DataFrame({
    'cap-shape': [cap_shape],
    'cap-surface': [cap_surface],
    'cap-color': [cap_color],
    'bruises': [bruises],
    'odor': [odor]
})


for col in input_data.columns:
    input_data[col] = label_encoders[col].transform(input_data[col])


for col in X.columns:
    if col not in input_data.columns:
        input_data[col] = 0


input_data = input_data[X.columns]


if st.button("Predict"):

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Poisonous Mushroom 🍄")
    else:
        st.success("Edible Mushroom ✅")