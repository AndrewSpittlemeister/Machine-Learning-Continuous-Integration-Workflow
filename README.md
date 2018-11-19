# Model Development and Deployment Example Repository

This was originally created to test out [Gitlab's built-in CI](https://about.gitlab.com/product/continuous-integration/) on developing and deploying models found [here](https://gitlab.com/AndrewSpittlemeister/ML-Dev-Example). 

## Repository Directory Structure

### ```datasets```

Directory containing all datasets used for training, validation, and testing. If another option is available for hosting a dataset and linking into this data directly from training or evaluation scripts, that would be even better.

### ```src```

Directorying containing all source files for developing, training, and evaluating the machine learning models. This directory has 3 core sub-directories:

- ```./src/train/```: a directory for all files used to train a model on existing datasets
- ```./src/evaluate/```: a directory for all files used to evaluate a model on existing datasets
- ```./src/models/```: a directory for models saved during the training or evaluation processes

Additionally, it may be a good idea to use this directory to store evaluation results for all the models in the ```./models/``` directory. Typically, with the use of version control, the ```./models/``` file should only contain a single and latest model (or as many models as the application needs) rather than store previously trained models.

### ```test```

Directory containing unit-testing and accuracy testing files. Unit-testing may consist of checking for model compilation, model I/O shapes, etc. Accuracy testing could be used to determine if the latest model passes some basic criteria before it can be considered ready for distribution.

## Generic Workflow

1. A change in model structure, training structure, datasets, etc. occurs
2. Model training and evaluation are performed offline to update the models with this newest information
3. A continuous integration process may be used to perform unit and accuracy testing against it; yielding a passing or failing grade
4. The distribution model is updated and produce as a CI artifact or uploaded to some host

