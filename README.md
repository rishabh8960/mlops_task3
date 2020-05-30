MLOps Task 3
This repository contains code for integration of Machine Learning Model and DevOps.

I have created such a environment which launches Container (Operating System with required tools) for running the Machine Learning model. After running Container it will automatically start training and prediction of model using Jenkins and sends accuracy to developer.

TASK :
Create container image that has Python3 and Keras or tensorflow installed using Dockerfile.

Create a job chain of job1, job2, job3, job4 and job5 using build pipeline plugin in Jenkins.

Job1 : Pull the Github repo automatically when some developers push repo to Github.

Job2 : By looking at the code or program file, Jenkins should automatically start the respective container.

Job3 : Train your model and predict accuracy.

Job4 : If accuracy is less than 90% then tweak the machine learning model architecture and retrain it.

Job5: Notify that the best model is being created.

Create One extra job job6 for monitor. If container where app is running fails due to any reason then this job should automatically start the container again from where the last trained model left
