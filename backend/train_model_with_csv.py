"""
CYBER SHIELD - ML MODEL TRAINING WITH CSV DATASET
Trains a Random Forest model using job_scam_training_dataset.csv
"""

import pickle
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print("=" * 80)
print("CYBER SHIELD - ML MODEL TRAINING WITH CSV DATASET")
print("=" * 80)

# Load CSV dataset
print("\n[1] Loading CSV dataset...")
try:
    df = pd.read_csv('../job_scam_training_dataset.csv')
    print(f"    ✓ Dataset loaded successfully")
    print(f"    ✓ Total records: {len(df)}")
    print(f"    ✓ Columns: {list(df.columns)}")
    
    # Check label distribution
    label_counts = df['label'].value_counts()
    print(f"    ✓ Label distribution:")
    for label, count in label_counts.items():
        print(f"      - {label}: {count}")
    
    # Extract messages and labels
    messages = df['text'].astype(str).tolist()
    labels = df['label'].map({'scam': 1, 'ham': 0}).tolist()
    
    print(f"    ✓ Processed {len(messages)} messages")
    print(f"    ✓ Scam messages: {sum(labels)}")
    print(f"    ✓ Legitimate messages: {len(labels) - sum(labels)}")
    
except Exception as e:
    print(f"    ❌ Error loading CSV: {e}")
    exit(1)

# Split dataset
print("\n[2] Splitting dataset into train/test...")
X_train, X_test, y_train, y_test = train_test_split(
    messages, labels, test_size=0.2, random_state=42, stratify=labels
)
print(f"    ✓ Training set: {len(X_train)} messages")
print(f"    ✓ Testing set: {len(X_test)} messages")

# Vectorize text using TF-IDF
print("\n[3] Vectorizing text using TF-IDF...")
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),
    min_df=1,
    max_df=0.95,
    stop_words='english'
)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)
print(f"    ✓ Features created: {X_train_vec.shape[1]}")
print(f"    ✓ Training matrix shape: {X_train_vec.shape}")

# Train Random Forest
print("\n[4] Training Random Forest Classifier...")
model = RandomForestClassifier(
    n_estimators=200,
    max_depth=20,
    min_samples_split=5,
    min_samples_leaf=2,
    random_state=42,
    n_jobs=-1,
    class_weight='balanced'
)
model.fit(X_train_vec, y_train)
print("    ✓ Model training completed")

# Evaluate
print("\n[5] Evaluating model performance...")
y_pred = model.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"    ✓ Accuracy:  {accuracy:.4f} ({accuracy*100:.2f}%)")
print(f"    ✓ Precision: {precision:.4f} ({precision*100:.2f}%)")
print(f"    ✓ Recall:    {recall:.4f} ({recall*100:.2f}%)")
print(f"    ✓ F1-Score:  {f1:.4f}")

# Show some test predictions
print("\n[6] Sample predictions on test data:")
test_indices = np.random.choice(len(X_test), min(5, len(X_test)), replace=False)
for i, idx in enumerate(test_indices, 1):
    actual_label = "SCAM" if y_test[idx] == 1 else "LEGITIMATE"
    predicted_label = "SCAM" if y_pred[idx] == 1 else "LEGITIMATE"
    confidence = np.max(model.predict_proba(X_test_vec[idx:idx+1])) * 100
    
    print(f"    {i}. {actual_label} → {predicted_label} ({confidence:.1f}% confidence)")
    print(f"       Text: {X_test[idx][:100]}...")

# Feature importance
print("\n[7] Top 15 most important features:")
feature_names = np.array(vectorizer.get_feature_names_out())
feature_importance = model.feature_importances_
indices = np.argsort(feature_importance)[-15:][::-1]
for i, idx in enumerate(indices, 1):
    print(f"    {i:2d}. '{feature_names[idx]}': {feature_importance[idx]:.6f}")

# Save model and vectorizer
print("\n[8] Saving model and vectorizer...")
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("    ✓ Model saved to model.pkl")

with open('vectorizer.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)
print("    ✓ Vectorizer saved to vectorizer.pkl")

print("\n" + "=" * 80)
print("MODEL TRAINING COMPLETED SUCCESSFULLY!")
print("=" * 80)
print(f"\n✓ Accuracy: {accuracy*100:.2f}%")
print(f"✓ Precision: {precision*100:.2f}%")
print(f"✓ Recall: {recall*100:.2f}%")
print(f"✓ F1-Score: {f1:.4f}")
print("\nFiles created:")
print("  • model.pkl")
print("  • vectorizer.pkl")
print("\nReady to start Flask server!")
print("=" * 80)
