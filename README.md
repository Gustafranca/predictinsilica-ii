# PredictInSilica-II

This project consists of an Exploratory Data Analysis (EDA) and the initial development of a regression model using a real-world dataset from a mining plant. It played a key role in helping me secure my first internship.

## Context

It's not always easy to find real-world datasets from industrial processes—especially from mining operations. That's why I'm sharing this dataset with the community. It comes from one of the most critical stages in a mineral processing plant: the flotation process.

The dataset used is **"Quality Prediction in a Mining Process"**, which is publicly available on [Kaggle](https://www.kaggle.com/).

## DVC

As part of the onboarding process for my internship, I was challenged to rebuild the project using modern tools and clean code practices, with a focus on scalable Python development.

One of the most essential tools I used was **DVC (Data Version Control)**. It played a crucial role in building reproducible pipelines and managing data versioning, integrated with an S3 bucket for remote storage.
## Project Structure
```
predictinsilica-ii/
├── data/                   # Datasets used for training and validation
├── notebooks/              # Jupyter notebooks with analysis and models
├── scripts/                # Helper scripts for data processing
├── results/                # Outputs and results from model training
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
```
