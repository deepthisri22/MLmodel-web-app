# MLmodel-web-app

This is a simple project to demonstrate how Machine Learning Models can be deployed on production using Flask API.

This demo uses a simple Iris dataset and performs classification using Random Forest.
The trained model is then deployed on the server like AWS or Heroku. 

<h2> Prerequisites

Install Pandas, Scikit Learn, Flask.

```
pip install pandas scikit-learn flask
```

<h2> Contents
  

1. Dataset
2. Machine Learning Model
3. Web Application using Flask
4. Cloud Deployment


<h2> Dataset

The Iris dataset consists of 3 classes of 50 instances each, where each class refers to a type of iris plant i.e., Iris Setosa, Iris Versicolour, Iris Virginica. It has following 4 features:
* Sepal Length(cm)
* Sepal Width(cm)
* Petal Length(cm)
* Petal Width(cm)

Dataset can be downloaded from [here](http://archive.ics.uci.edu/ml/datasets/iris).


<h2> Machine Learning Model

Random Forest from scikit-learn package is used as the ML model for classification. It is an ensemble learning method for classification which trains multiple individual decision trees during training.

The file iris.pynb contains the training of Random Forest on iris dataset. The trained model is saved as pickle file (model.pkl) and it is used during inference.


<h2> Web application using Flask

Flask is a web framework written in python for developing web applications. The file *app.py* contains Flask APIs that receives iris features through GUI, computes the predicted class using the trained model and returns it. The templates folder contains the HTML templates to allow the user to enter iris features and displays the predicted class.

<h2> Cloud Deployment

The ML model is deployed on Heroku Cloud which is a PaaS. *Procfile* is a configuration file which tells Heroku which file to execute first. The command 
```
web: gunicorn app:app
```
tells to execute the Flask application named *app*  present in the *app.py* file.

The deployed web page can be found [here](https://iris-classification-app.herokuapp.com/).


<h3> Web app Home page

![Home page](https://github.com/deepthisri22/MLmodel-web-app/blob/master/web_images/home_page.png)

<h3> Web app Predict page

![Home page](https://github.com/deepthisri22/MLmodel-web-app/blob/master/web_images/predict_page.png)



