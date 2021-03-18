from keras.models import Sequential
from keras.layers import Dense
from DictionaryStore import DictionaryStory

dict = DictionaryStory()
X, y = dict.get_label_and_data()

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

# compile the keras model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=150, batch_size=10)
accuracy = model.evaluate(X, y)
print('Accuracy: %.2f' % (accuracy*100))