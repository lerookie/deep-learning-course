# Deep Learning Developer Course

## Project 1: Addition Basic Classification
### Description
* Dense neural network for adding two integers (between 1-100).
* For pre-processing, each pair of integer is converted into a 14 bit binary number.

## Project 2: CNN
### Description
* Convolutional neural network for classifying images in the [QuickDraw dataset](https://github.com/googlecreativelab/quickdraw-dataset)
* Training was done with 200 classes, 10000 examples per class.
* Model managed to achieve 53% accuracy on the validation data after 10 epochs.
    * Possible room for improvement would be to train the model over more epochs (e.g. 50 epochs).

## Project 3: RNN
### Description
* Generative model trained on the novel "A Game of Thrones".
* Temperature was added to reduce the likelihood of the model generating the same phrase over and over.

## Project 4: Personal Project - Classifier for food images
### Description
* Convolutional neural network for classifying images of food
* Dataset consists of 132 classes, approximately 250 examples per class.
* Model managed to achieve 73.9% accuracy on the validation data after 20 epochs.
    * Unfortunately, it seems like the model is overfitting on the training data.
    * Possible room for improvement would be to add more drop out in the top layer and to train it over more epochs
    * Model seems to be able to classify baked beans with high degree of accuracy

## Project 5: Personal Project - Recommender for similar restaurants
### Description
* Made use of [Doc2Vec](https://radimrehurek.com/gensim/models/doc2vec.html) on [Yelp's dataset](https://www.yelp.com/dataset/challenge).
* Data was processed as such:
    * Filter to only include businesses that had the category "Restaurants" or "Food".
    * Filter to exclude business with less than 5 reviews.
* Each restaurant is then converted to an embedding based on its reviews.
* Model can be queried for restaurants similar to a given restaurant.
* Plotting the restaurant embeddings, using t-SNE, seems to indicate that similar types of restaurants are "closer" to each other in the vector space (i.e. pizzerias are grouped close together at the top of the plot).
