# Student_performance_calculator  end to end mlproject(CI & CD pipelines )
![4abd0000-f6e7-11ea-9205-8ea0ef6d8474](https://github.com/subhaganesh/mlproject/assets/96689756/ecefc154-0eed-43af-8504-3e64a93afdc1)

This project focuses on data cleaning, exploratory data analysis (EDA), model training, and deployment of a Student Performance Calculator. The following steps were performed:

1.Data Cleaning: The dataset was carefully processed to remove any inconsistencies, missing values, or anomalies that could affect the analysis and model performance.

2.Exploratory Data Analysis (EDA): Extensive EDA techniques were applied to gain insights from the dataset. Visualizations and statistical methods were utilized to explore relationships, identify patterns, and understand the variables' impact on student performance.

3.Model Training: Various models were trained using the dataset, and evaluation metrics were used to identify the best-performing model. Hyperparameter tuning techniques were applied to optimize the model's performance further.

4.Flask App Development: A Flask web application was developed to provide a user-friendly interface for predicting student performance. The Flask app can be run locally on the localhost for testing purposes.

5.Docker Integration: A Dockerfile was created to facilitate the deployment process. The Dockerfile enables easy containerization of the Flask app, ensuring consistent and reliable execution across different environments.

6.Docker Image Creation: The Dockerfile was used to build a Docker image. This image encapsulates the Flask app and its dependencies, making it portable and easy to distribute.

7.Docker Hub Repository: The Docker image was uploaded to a Docker Hub repository. This repository serves as a central location where anyone can access and pull the code, enabling others to use the Student Performance Calculator for their own purposes.

By following these steps, the project achieves a streamlined workflow that encompasses data cleaning, EDA, model training, Flask app development, Docker integration, and image deployment to Docker Hub. The resulting application provides a convenient tool for predicting student performance based on the trained model.

## Libraries used
pandas: 1.3.0

numpy: 1.21.0

seaborn: 0.11.1

matplotlib: 3.4.2

scikit-learn: 0.24.2

catboost: 0.26.1

xgboost: 1.4.2

dill: 0.3.4

flask: 2.0.1

## Deployment
The deployment was done in the docker hub by using github actions and dockerfile a workflow is created so that if any change in the code happens the it automatically build and push that change to the docker image.

## docker push subhaganesh/stud_perfo_app:tagname 
By use the above command you can download the app as a docker image 

## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://subhaganesh.github.io/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/subhaganesh-s-170875236/)



