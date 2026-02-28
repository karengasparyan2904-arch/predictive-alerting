# Predictive Alerting for Cloud Metrics

This project is a simple prototype of a predictive alerting system for cloud metrics. The goal is to predict whether an incident will occur within the next few time steps based on historical metrics. The project uses a sliding-window approach and a basic machine learning model.

## Problem

Cloud services generate many metrics, and incidents can happen suddenly. The task is to predict incidents a few steps ahead using previous metric values. This helps raise alerts before problems occur.

## Dataset

For this prototype, a **synthetic dataset** is used. The metric values are generated randomly, and incidents are simulated as spikes in the metric. Each window of previous values is labeled as incident (`1`) or no incident (`0`) for the next time steps.

## Solution Approach

- Use a **sliding window** of previous `W` steps to predict the next `H` steps.
- Extract simple features from the window: mean, max, min, and last value.
- Train a **Random Forest classifier** on these features.
- Predict probability of an incident and raise an alert if it exceeds a threshold (e.g., 0.5).

## Training and Evaluation

- Train/test split is done **chronologically** to respect time series order.
- Evaluation metrics:
  - **Recall:** how many incidents were correctly predicted before they happen.
  - **False positives:** number of alerts raised without real incidents.
  - **Lead time:** how early the alert is raised before the incident.
- The code prints a classification report and the total number of alerts.
