# 0. Import the following libraries:
#    pandas, numpy
#    matplotlib.pyplot as plt
#    sklearn libraries for KNN, accuracy_score, train_test_split, and cross_val_score

###################################
# PART 1: MACHINE LEARNING BASICS #
###################################

# 1. Load Dataset 
filename = None
df = None

# 2. Create matrix X containing the features
#    Create target vector y containing the classes
X = None
y = None

# 3. Split the dataset
#    Set the test_size = 0.33
#    Set seed (random_state) = 42 for reproducibility
X_train, X_test, y_train, y_test = None, None, None, None

# 4. Instantiate Learning Model for KNN. 
#    Set K = 3 (i.e. n_neighbors)

# 5. Fit KNN model to training set

# 6. Predict labels of the test set using the KNN model

# 7. Evaluate accuracy
accuracy = 0
print("KNN accuracy: " + str(accuracy))

##################################################
# PART 2: Parameter Tuning with Cross Validation #
##################################################

# 1. Import (at the start of the script) the sklearn library for cross validation: cross_val_score

# 2. Create a list neighbors (a list of k's) which will be a list of odd numbers from 1 to 50:
# 	 e.g. neighbors = [1, 3, 5, 7, 9, 11, ..., 49]
neighbors = []

cv_scores = []
# 3. For each k in neighbors,
#       3.1 Instantiate a learning model for KNN and set parameter n_neighbors = k
#       3.2 Perform cross validation using the cross_val_score function (set number of folds cv=10, scoring='accuracy')
#       3.3 Set avg_score to the average of the scores returned by cross_val_score and append avg_score to cv_scores list

mse = []
# 4. Get the misclassification errors and store them in list 'mse'
#    For each score in cv_scores:
#       4.1 Set the misclassification error to (1- score) and append the misclassification error to the list mse

optimal_k = None
# 5. Get the optimal k
#    5.1. Set index_min = index of the minimum value in mse 
#    5.2. Set optimal_k as the value of neighbors at index_min

print("Optimal value for k is: ", optimal_k)
print("Misclassification score: ", min(mse))
print("Accuracy: ", 1 - min(mse))

# Plotting misclassification errors vs neighbors (k's)
# Uncomment this part to display graph
"""
plt.plot(neighbors, mse)
plt.xlabel('Number of Neighbors K')
plt.ylabel('Misclassification Error')
plt.show()
"""