# Fruit Freshness Classification

This project classifies fruits as fresh or rotten using computer vision. It can tell if an apple, banana, or strawberry is fresh or rotten by looking at a picture of it.

## What It Does

The project uses a deep learning model to look at images of fruits and decide if they are fresh or rotten. It works with three types of fruits:
- Apples
- Bananas
- Strawberries

For each fruit, it can tell if it is fresh or rotten. This gives six different categories in total.

## How It Works

The code uses PyTorch to build and train a model. The model learns from many pictures of fresh and rotten fruits. After training, it can look at new pictures and predict if the fruit is fresh or rotten.
This model was trained locally on a RTX3090, but can be done with other accelerators such as Apple Silicon. In the notebooks and scripts, there is use of both CUDA and MPS accelerators as this was used on both types of hardware.

The project includes code to:
- Organize the training data
- Split data into training and testing sets
- Train the model
- Test the model on new images

## About This Project

This project was created while learning from the Zero to Mastery "Learn PyTorch for Deep Learning" course. It shows how to build a simple image classification model using PyTorch.

