## End to end ML project

### Created an environment 
```
conda create -p venv python==3.10
```
### Install all necessary libraries
```
pip install -r requirements.txt
```

AWS beanstalk deployement :
- Add a folder named .ebextensions and create a file named python.config and add these lines of code :
    option_settings:
    "aws:elasticbeanstalk:container:python":
      WSGIPath: application:application   
- Then open elastic bean stalk and create a python environment in new application
- Now go to pipelines and select a code pipeline and add the git repo there 

Azure web-app deloyement :
- Create a resource group and select web app 
- Give the source as github and connect to github 
- Create the application and give all othe rnecessary settings

