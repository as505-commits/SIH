import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder 
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,precision_score,recall_score,f1_score
import joblib

df=pd.read_excel("CAPF_Stress_Dataset_FINAL.xlsx")
print(df.head())

print("before drop:", df.shape)


y=df["Stress_Level"]
x=df.drop(columns=["ID","Stress_Level"])

print("after drop:", x.shape)
print(x.head())

#ecoding categorical columns
cat_col=[
    "Work_Pressure_Level",
    "Work_Life_Balance",
    "Family_Support_Level",
    "Job_Satisfaction",
    "Training_Opportunities"
]
encoders={}
for col in cat_col:
    le = LabelEncoder()
    x[col] = le.fit_transform(x[col])
    encoders[col] = le

print("\nEncoded x:")
print(x[cat_col].head())

#splitting into test and training

x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.2,random_state=42,stratify=y)
print("\ntraining data shape:", x_train.shape)
print("Testing data shape:", x_test.shape)

#making random forest model
model=RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
 )
model.fit(x_train,y_train)
print("\nRandom Forest model trained successfully!")

#prediction
y_pred=model.predict(x_test)
print("\nPredictions:")
print(y_pred[:20])

#accuracy,precision,recall,f1 score
accuracy=accuracy_score(y_test,y_pred)
precision=precision_score(y_test,y_pred,average="weighted")
recall=recall_score(y_test,y_pred,average="weighted")
f1=f1_score(y_test,y_pred,average="weighted")

print("\nEVALUATION")
print("accuracy:", accuracy)
print("precision:", precision)
print("recall:", recall)
print("f1 score:", f1)

saved_model = {
    "model": model,
    "encoders": encoders,
    "features": x.columns.tolist()
}
joblib.dump(saved_model, "model.pkl")
print("\nModel saved successfully as stress_model.pkl")

#plotting graphs
plt.figure(figsize=(6, 4))

df["Stress_Level"].value_counts().plot(kind="bar")

plt.title("Stress Level Distribution")
plt.xlabel("Stress Level")
plt.ylabel("Number of Personnel")
plt.xticks(rotation=0)

plt.tight_layout()
plt.show()

#confusion matrix
y_pred=model.predict(x_test)
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6, 5))

plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.xticks(
    range(len(model.classes_)),
    model.classes_
)

plt.yticks(
    range(len(model.classes_)),
    model.classes_
)

for i in range(len(model.classes_)):
    for j in range(len(model.classes_)):
        plt.text(j, i, cm[i, j],
                 ha="center",
                 va="center")

plt.colorbar()

plt.tight_layout()
plt.show()


