# 🏦 Bank Customer Churn Prediction

## Project Overview

**Bank Customer Churn Prediction** is a machine learning and deep learning project designed to predict whether a bank customer is likely to leave the bank.

The project analyzes customer information such as credit score, age, geography, account balance, number of products, activity status, and estimated salary. A trained predictive model uses these features to classify customers as likely to **Stay** or **Churn**.

The project also includes an interactive **Streamlit web application** that allows users to enter customer details and receive a prediction.

---

## Objectives

* Analyze bank customer data.
* Perform data cleaning and preprocessing.
* Explore customer behavior using EDA.
* Build a customer churn classification model.
* Evaluate model performance.
* Save the trained model and preprocessing objects.
* Develop an interactive Streamlit application.
* Deploy the project online.
* Provide a portfolio-ready end-to-end Data Science project.

---

## Machine Learning Problem

This project is a **binary classification problem**.

The target variable represents whether a customer has exited the bank.

```text
0 → Customer Stayed
1 → Customer Churned
```

The trained model learns patterns from historical customer records and uses those patterns to predict churn for new customers.

---

## Dataset

The project uses a bank customer dataset stored as:

```text
European_Bank.csv
```

Typical customer attributes include:

| Feature         | Description                   |
| --------------- | ----------------------------- |
| CreditScore     | Customer credit score         |
| Geography       | Customer location             |
| Gender          | Customer gender               |
| Age             | Customer age                  |
| Tenure          | Number of years with the bank |
| Balance         | Customer account balance      |
| NumOfProducts   | Number of bank products       |
| HasCrCard       | Credit card ownership         |
| IsActiveMember  | Customer activity status      |
| EstimatedSalary | Estimated customer salary     |
| Exited          | Customer churn target         |

> The exact columns used by the application should match the columns used during model training.

---

## 🔄 Project Workflow

```text
Dataset
   ↓
Data Cleaning
   ↓
Data Preprocessing
   ↓
Exploratory Data Analysis
   ↓
Feature Engineering
   ↓
Train/Test Split
   ↓
Model Training
   ↓
Model Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
   ↓
GitHub
   ↓
Online Deployment
```

---

## 🔍 Exploratory Data Analysis

The project analyzes customer data to identify patterns related to churn.

EDA can include:

* Churn distribution
* Age vs churn
* Geography vs churn
* Credit score analysis
* Account balance analysis
* Number of products
* Active member status
* Gender distribution
* Correlation analysis

Visualization libraries:

```text
Matplotlib
Seaborn
```

---

## Machine Learning Models

The project can evaluate classification algorithms such as:

* Logistic Regression
* Decision Tree
* Random Forest
* Support Vector Machine
* K-Nearest Neighbors
* Naive Bayes

A deep learning model using **TensorFlow/Keras** can also be used.

The final model should be selected based on actual validation/test performance.

---

## Deep Learning Model

The project includes a Keras model:

```text
models/bank_churn_deep_learning.keras
```

The general prediction process is:

```text
Customer Input
      ↓
Data Preprocessing
      ↓
Feature Scaling
      ↓
Deep Learning Model
      ↓
Prediction Probability
      ↓
Churn / Stay
```

---

## Model Evaluation

The model can be evaluated using:

### Accuracy

Measures the percentage of correct predictions.

### Precision

Measures how many customers predicted as churners actually churned.

### Recall

Measures how many actual churners were successfully identified.

### F1-Score

Provides a balance between precision and recall.

### Confusion Matrix

Shows:

```text
                 Predicted
              Stay     Churn

Actual Stay     TN       FP

Actual Churn   FN       TP
```

Actual performance values should be added from the final model evaluation rather than using estimated numbers.

---

## 🌐 Streamlit Application

The project includes an interactive Streamlit application.

### Main Features

* Home page
* Customer Review
* ML Prediction
* Analytics
* Customer input form
* Churn prediction
* Prediction result
* Data visualizations

### Application Flow

```text
Home
 ↓
Customer Review
 ↓
ML Prediction
 ↓
Analytics
```

---

## Project Structure

```text
Bank Customer Churn/
│
├── app.py
├── train_model.py
├── European_Bank.csv
├── requirements.txt
├── Dockerfile
├── README.md
│
└── models/
    ├── bank_churn_deep_learning.keras
    ├── churn_scaler.pkl
    └── feature_columns.pkl
```

---

## File Description

### `app.py`

Main Streamlit application.

It:

* loads the trained model;
* accepts customer input;
* preprocesses input;
* performs prediction;
* displays the prediction result;
* provides the application interface.

### `train_model.py`

Used to:

* load the dataset;
* preprocess the data;
* train the model;
* evaluate the model;
* save the trained model.

### `European_Bank.csv`

Contains the bank customer dataset used for training and analysis.

### `requirements.txt`

Contains the Python packages required to run the application.

### `Dockerfile`

Contains instructions for creating a Docker container for the application.

### `models/`

Stores the trained model and preprocessing files.

---

## Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Machine Learning

* Scikit-learn

### Deep Learning

* TensorFlow
* Keras

### Visualization

* Matplotlib
* Seaborn

### Web Application

* Streamlit

### Development

* VS Code
* Jupyter Notebook

### Version Control

* Git
* GitHub

### Deployment

* Streamlit Community Cloud
* Docker

---

## Installation

Clone the repository:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Go to the project directory:

```bash
cd Bank-Customer-Churn-Prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
venv\Scripts\activate
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

After running the command, Streamlit will provide a local web address.

Open the displayed address in your browser.

---

## Train the Model

If the model needs to be retrained:

```bash
python train_model.py
```

The trained model and preprocessing files should then be saved in the `models/` directory according to the paths used by the application.

---

## Prediction Example

A user enters customer information through the Streamlit interface.

Example:

```text
Credit Score: 650
Age: 40
Balance: 100000
Number of Products: 2
Active Member: Yes
```

The application processes the information and displays a result such as:

```text
🔴 Customer Likely to Churn
```

or:

```text
🟢 Customer Likely to Stay
```

The prediction is generated by the trained model and should be treated as a model estimate, not a guarantee.

---

## GitHub Deployment

Initialize Git:

```bash
git init
```

Add project files:

```bash
git add .
```

Commit:

```bash
git commit -m "Bank Customer Churn Prediction project"
```

Set the main branch:

```bash
git branch -M main
```

Connect the GitHub repository:

```bash
git remote add origin YOUR_GITHUB_REPOSITORY_URL
```

Push the project:

```bash
git push -u origin main
```

---

## ☁️ Online Deployment

The Streamlit application can be deployed using **Streamlit Community Cloud**.

Deployment settings:

```text
Repository: Your GitHub Repository
Branch: main
Main file: app.py
```

After deployment, Streamlit provides a public application URL.

Example:

```text
https://your-project-name.streamlit.app
```

---

## 🐳 Docker

The project can also be containerized using Docker.

Build the image:

```bash
docker build -t bank-customer-churn .
```

Run the container:

```bash
docker run -p 8501:8501 bank-customer-churn
```

The Streamlit application can then be accessed through the local Docker port.

---

## Important Security Notes

For a production system:

* Do not store passwords or API keys in GitHub.
* Do not commit `.env` files.
* Protect customer data.
* Avoid uploading sensitive personal information.
* Add authentication before exposing a real banking application publicly.
* Use appropriate privacy and security controls.

---

## Limitations

* Model predictions depend on the quality of the training data.
* Historical customer behavior may not perfectly represent future behavior.
* Predictions can be incorrect.
* Class imbalance can affect model performance.
* The system is intended as a data-science/portfolio project and should not be treated as a production banking decision system without further validation.

---

## Future Enhancements

Possible improvements include:

* Explainable AI using SHAP.
* Advanced customer analytics.
* Interactive dashboards.
* Database integration.
* User authentication.
* Automated model retraining.
* Model monitoring.
* Cloud infrastructure.
* Customer segmentation.
* Churn probability visualization.
* Automated retention recommendations.

---

## Project Outcome

This project demonstrates an end-to-end Data Science workflow:

```text
Data Collection
      ↓
Data Cleaning
      ↓
EDA
      ↓
Feature Engineering
      ↓
Machine Learning
      ↓
Deep Learning
      ↓
Model Evaluation
      ↓
Streamlit
      ↓
GitHub
      ↓
Online Deployment
```

It demonstrates practical skills in **Python, SQL/Data Analysis concepts, Machine Learning, Deep Learning, Data Visualization, Streamlit, Git, GitHub, Docker, and deployment**.

---

## 👨 Author

### Simon V

### Aspiring Data Scientist | Data Analyst

Skills demonstrated:

```text
Python
SQL
Machine Learning
Deep Learning
Data Analysis
Data Visualization
Pandas
NumPy
Scikit-learn
TensorFlow
Keras
Streamlit
Git
GitHub
Docker
```

---

## License

This project is intended for educational, portfolio, and demonstration purposes.

---

## Acknowledgement

This project was developed as a practical Data Science project to demonstrate the complete process of building and deploying a customer churn prediction application.
