import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

np.random.seed(42)
T = 1000
W = 10
H = 5
metric = np.random.normal(0,1,T)
incidents = np.zeros(T)
for i in range(50, T, 200):
    metric[i:i+10] += 5
    incidents[i:i+10] = 1

X = []
y = []
for t in range(W, T-H):
    window = metric[t-W:t]
    features = [window.mean(), window.max(), window.min(), window[-1]]
    X.append(features)
    y.append(int(incidents[t:t+H].max()>0))

X = np.array(X)
y = np.array(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, shuffle=False, test_size=0.2)

model = RandomForestClassifier(n_estimators=50, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
alerts = model.predict_proba(X_test)[:,1] > 0.5
print("Number of alerts:", alerts.sum())
