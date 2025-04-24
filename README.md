#  Instacart Market Basket Analysis Project

This repository contains a comprehensive analysis and modeling pipeline based on the **Instacart Online Grocery Shopping Dataset**. The work is part of a dissertation focusing on transaction data mining, recommendation systems, and customer segmentation.

---

##  Project Structure

The project is divided into the following main objectives, each represented by a dedicated Jupyter notebook:

###  Objective 1: Frequent Purchase Pattern Discovery
- **Notebook**: `Explained_Obj_1_Instacart_Analysis.ipynb`
- Performs exploratory analysis on the Instacart dataset.
- Answers 20 business questions around order behavior, product popularity, and reordering trends.

###  Objective 2: Market Basket Analysis – Apriori vs FP-Growth
- **Notebook**: `Final_Complete_Obj_2_Apriori_vs_FPGrowth.ipynb`
- Compares the Apriori and FP-Growth algorithms on speed, scalability, and rule generation.
- Includes detailed rule-based evaluation.

###  Objective 3: Recommendation Optimization
- **Notebook**: `Final_Complete_Obj_3_Recommendation_Optimization.ipynb`
- Leverages FP-Growth insights to create a rule-based product recommender system.
- Evaluates recommendation effectiveness.

###  Objective 4: Customer Segmentation for Targeted Marketing
- **Notebook**: `Final_Complete_Obj_4_Customer_Segmentation.ipynb`
- Uses clustering (K-Means) and PCA to segment customers.
- Derives actionable marketing insights from behavioral patterns.

###  Data Cleaning Scripts
- **Python Script**: `Script_Cleaning_Enhanced_Documented.py`
- Includes modular cleaning routines for each dataset:
  - `aisles.csv`
  - `departments.csv`
  - `orders.csv`
  - `order_products__prior.csv`
  - `order_products__train.csv`

---

##  Dataset Overview

The dataset comes from Instacart's anonymized historical data, consisting of **3 million orders from 200,000 users** and over **50,000 unique products**.

Key Files:
- `orders.csv` – Sequence of user orders (time, order number, etc.)
- `products.csv` – Product names and IDs
- `aisles.csv` – Aisle categorization
- `departments.csv` – Department categorization
- `order_products__prior.csv` – Prior order details with product IDs
- `order_products__train.csv` – Train order details used for recommendation modeling

---

##  Technologies Used

- **Python** (pandas, scikit-learn, matplotlib, seaborn, mlxtend)
- **Jupyter Notebooks** for exploration and modeling
- **Plotly** and **Matplotlib** for visualizations

---



##  Author

- **Name**: Muhammad Salman Javed
- **Affiliation**: MSc Dissertation, Data Science
- **Contact**: mj2066@hw.ac.uk

---



