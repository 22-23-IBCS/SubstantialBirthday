import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import numpy

# Load the training data
train_data = pd.read_csv('CrocAlliTraining.csv')

# Drop the "animal" column from the training data
X_train = train_data.drop('animal', axis=1)
y_train = train_data['animal']

# Fit the classifier to the training data
clf = KNeighborsClassifier(n_neighbors=3)
data=clf.fit(X_train, y_train)



# Load the new data
new_data = pd.read_csv('CrocAlliTest1.csv')

# Separate the features from the target variable
X_new = new_data[['length', 'mass']]

# Make predictions on the new data
pred_animal = clf.predict(X_new)
pred_animal = numpy.ndarray.tolist(pred_animal)
probs = clf.predict_proba(X_new)
probs = numpy.ndarray.tolist(probs)

pred_animal2 = {}
count = 1

for ani in pred_animal:
    name = "Sample "+str(count)
    pred_animal2[name] = ani
    count=count+1

for i in range(len(probs)):
    p1=round(probs[i][0],3)
    p2=round(probs[i][1],3)
    #print(p1,p2)
    probs.pop(i)
    probs.insert(i,[p1,p2])
  
    


# Print the predicted species and corresponding probabilities
for i, animal in enumerate(pred_animal):
    print(f"Sample {i+1}: {animal}, Probabilities: {probs[i]}")



#print(pred_animal)
print(pred_animal2)
#print(type(pred_animal))
print(probs)
#print(type(probs))
