# US Visa Approval Prediction --- MLOps Production-Ready ML Project

A fully scalable, modular, and production-ready Machine Learning
pipeline designed using **MLOps best practices**.\
This project covers everything from data ingestion to deployment,
following industry standards for reproducibility, automation, and
maintainability.

------------------------------------------------------------------------

## 🚀 Features

-   Modular project architecture\
-   Config-driven pipeline\
-   Automated data ingestion & validation\
-   Data transformation pipeline\
-   Model training with hyperparameter tuning\
-   Custom components & pipelines\
-   Logging, exception handling & utilities\
-   CI/CD ready structure\
-   Easy installation & setup using Conda

------------------------------------------------------------------------

## 📁 Project Structure

    us_visa/
    │
    ├── components/
    │   ├── data_ingestion.py
    │   ├── data_validation.py
    │   ├── data_transformation.py
    │   ├── model_trainer.py
    │   └── __init__.py
    │
    ├── entity/
    ├── constants/
    ├── pipeline/
    ├── main.py
    └── __init__.py

    artifacts/  (Auto-generated after pipeline runs)

------------------------------------------------------------------------

## 🛠️ Tech Stack

-   **Python 3.8**
-   **Conda** for environment management
-   **Scikit-learn**, **pandas**, **numpy**
-   **MLflow** (optional integration)
-   **MLOps modular architecture**

------------------------------------------------------------------------

## 🔧 Installation & Setup

### 1️⃣ Create Conda Environment

``` bash
conda create -n visa python=3.8 -y
```

### 2️⃣ Activate Environment

``` bash
conda activate visa
```

### 3️⃣ Install Dependencies

``` bash
pip install -r requirements.txt
```

------------------------------------------------------------------------

## ▶️ How to Run the Project

### Run the entire ML pipeline:

``` bash
python main.py
```

This executes:

1.  **Data Ingestion**\
2.  **Data Validation**\
3.  **Data Transformation**\
4.  **Model Training**

Outputs are stored in the **artifacts/** folder.

------------------------------------------------------------------------

## 📌 Workflow Description

### **1. Constants**

Contains static values like paths, filenames, and column names.

### **2. Entity**

Defines input/output schemas for different pipeline stages.

### **3. Components**

Core building blocks of the ML pipeline:\
- `data_ingestion.py`\
- `data_validation.py`\
- `data_transformation.py`\
- `model_trainer.py`

### **4. Pipeline**

Scripts that connect components in an end-to-end flow.

### **5. Main File**

Entry point that triggers the complete process.

------------------------------------------------------------------------

## 🧪 Testing

You can add `pytest` or unit test modules later for validating
components and pipelines.

------------------------------------------------------------------------

## 📝 Git Commands

``` bash
git add .
git commit -m "Updated"
git push origin main
```

------------------------------------------------------------------------

## 🙌 Author

**Dinesh Jamdade**\
MLOps Engineer \| Data Scientist
