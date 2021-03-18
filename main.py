from sklearn.linear_model import LogisticRegression
import os
from sklearn.model_selection import train_test_split
import pickle
import time
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.pipeline import Pipeline

test_percent = 0.2

text = []
label = []

for line in open('data.txt', 'r', encoding="utf-8"):
    words = line.strip().split()
    label.append(words[0])
    text.append(' '.join(words[1:]))

X_train, X_test, y_train, y_test = train_test_split(
    text, label, test_size=test_percent, random_state=42)

MODEL_PATH = "models"

if not os.path.exists(MODEL_PATH):
    os.makedirs(MODEL_PATH)

start_time = time.time()

text_clf = Pipeline([('vect', CountVectorizer(ngram_range=(1, 1),
                                              max_df=0.8,
                                              max_features=None)),
                     ('tfidf', TfidfTransformer()),
                     ('clf', LogisticRegression(solver='lbfgs',
                                                multi_class='auto',
                                                max_iter=10000))
                     ])
text_clf = text_clf.fit(X_train, y_train)

train_time = time.time() - start_time

print('Done training Linear Classifier in', train_time, 'seconds.')

test = text_clf.predict(X_test)

count = 0
for i in range(len(test)):
    if test[i] == y_test[i]:
        count += 1
print(" Tỉ lệ nhận dạng đúng là: ", count / len(test))

# Save model
pickle.dump(text_clf, open(os.path.join(MODEL_PATH, "linear_classifier.pkl"), 'wb'))
