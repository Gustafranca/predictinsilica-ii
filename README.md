# PredictInSilica-II: End-to-End MLOps for Mining

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![Flask](https://img.shields.io/badge/Flask-API-lightgrey?logo=flask)
![DVC](https://img.shields.io/badge/DVC-Data_Version_Control-purple?logo=dvc)

**PredictInSilica-II** represents the evolution of a data science initiative from a static analysis project into a full-cycle MLOps system.

Originally developed to secure my internship, this project focuses on predicting silica concentration in a mining flotation process. I am now expanding it into a deployable system that handles the entire lifecycle—from Exploratory Data Analysis (EDA) to Model Deployment and Monitoring.

---

## 🏗️ Project Evolution

### Phase 2: MLOps & Model Deployment (Current Focus)
**Goal:** Transition from notebooks to a production environment.
I am currently developing a full system that operationalizes the model. This phase focuses on the "In-Silica" deployment, ensuring the model can serve predictions via API and be monitored for drift.

** The MLOps Pipeline:**
`Data Preparation` → `Model Training` → `Model Evaluation` → `Deployment (API)` → `Monitoring`

**Tech Stack for Phase 2:**
* **Containerization:** Docker
* **API Framework:** Flask
* **Modeling:** Scikit-learn, Pandas, Numpy, Pickle

### Phase 1: The Foundation (EDA & DVC)
**Goal:** Clean code, reproducibility, and rigorous analysis.
This phase played a key role in my onboarding. I was challenged to refactor the initial analysis using modern software engineering practices.

**Key Achievements:**
* **Reproducibility:** implemented **DVC (Data Version Control)** to manage data versioning and pipeline stages, integrated with an S3 bucket for remote storage.
* **Deep Analysis:** Conducted extensive EDA to understand the correlations in the flotation plant variables.

---

## ⛏️ The Context: Mining Industry 4.0

It is often difficult to find high-quality real-world datasets from industrial processes. This project utilizes the **"Quality Prediction in a Mining Process"** dataset, available on [Kaggle](https://www.kaggle.com/).

**The Challenge:**
The dataset focuses on the **Froth Flotation** process, a critical stage in mineral processing. The goal is to predict the percentage of Silica (impurity) in the iron ore concentrate. Accurate prediction allows engineers to adjust process variables in real-time, improving ore quality and reducing waste.

---

## 📂 Project Structure

```bash
predictinsilica-ii/
├── .dvc/                   # DVC configuration files
├── .github/                # CI/CD workflows (if applicable)
├── data/                   # Data registry (tracked by DVC)
├── notebooks/              # Jupyter notebooks for EDA and experiments
├── scripts/                # Modular scripts for processing and training
├── api/                    # Flask application for model serving
├── docker/                 # Dockerfile and compose setups
├── results/                # Model artifacts and evaluation metrics
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies
