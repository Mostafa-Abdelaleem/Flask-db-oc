# Deploy a flask app to OpenShift and connect to db2 using an OpenShift secret

Applications nowadays are built in many different source codes and in many components hence comes the concept of microservices 
where you build your application in different small pieces (containers) and use some orchestration tool that can orchestrate 
your processes simply and ensure that all tasks happen in the proper order.

Connecting databases to your application or website can be a real pain specially with changing environments as you would want a seemless switch between different databases and work environment like development, test and deploying. you want it an easy yet secure way to do that, with openshift secret you can create a connection to your database in seconds while ensuring the privacy of your credentials.

RedHat's Openshift has emerged as a leading hybrid cloud, enterprise Kubernetes application platform that can help with containerizing, deploying, and monitoring your application. It delivers a cloud-like experience as a self-managing
platform with automatic software updates and lifecycle management across hybrid cloud environments.

In today's tutorial, we will see how easy it is to deploy an app and connect it securely to a database elsewhere using Openshift
secrets to ensure credentials are encrypted yet accessible to our application, Openshift will automatically detect our framework
containerize, deploy, and manage our application in a span of minutes.

# Prerequisites
In order to follow the tutorial you should have.

- Active IBM cloud account, please create one if you don't have one on [IBM Cloud](https://cloud.ibm.com/registration)
- A Provisioned OpenShift 4.2 cluster, you can provision yours [here](https://cloud.ibm.com/kubernetes/landing?platformType=openshift)
- OpenShift CLI, download [HERE](https://cloud.ibm.com/docs/openshift?topic=openshift-openshift-cli)

# Estimated Time
This tutorial should take about 45 min to complete.

# Steps

***1- create a db2 database on IBM cloud***

- Go to Catalog -> choose services from the left pane -> tick the database checkbox -> choose db2

- Create a lite plan instance of db2 database, change the location and name if you wish then press create

![create db2](snaps/db2_2.png)



***2- create credentials for your db2 database***


- press service credentials then new credentials

- expand your created credentials and make note of the database URI

![db2 credentials2](snaps/db2_5.png)



- [optional] open the console to track changes in the database


***3- create an OpenShift Project***

- from terminal log in to your OC cluster and create a new project
```
oc new-project flask-db-project
```

- Or from OC web-console switch to developer mode for a Developer oriented  view and create a project
![](snaps/OC1.png)

***4- create an OpenShift Secret***

- from terminal create a secret to store and encrypt our database credentials to access it later using  environment variables

**make sure the the secret name and key are `dbcred` as the application access the env variables by the key name**
```
oc create secret generic dbcred --from-literal=dbcred="your db2 ssldsn value"
```
ex. oc create secret generic dbcred --from-literal=dbcred="DATABASE=*;HOSTNAME=*;PORT=50001;PROTOCOL=TCPIP;UID=*;PWD=*;"

-Or from OC webconsole go to search under advanced and filter services for secrets then create a key value secret
![](snaps/OC3.png)

***5- deploy the flask app and connect it to the db database***

- create a new app by going to add then choose from catalog 

![](snaps/OC6.png)

- press languages, choose python and choose a python app then press create application 

![](snaps/OC7.png)

- Add the Github Repo URL https://github.com/mostafa3m/Flask-db-oc.git in its field and show advanced option then add `/flask-app` in Context Dir field and choose a name for your app then press on Deployment Configuration

![](snaps/OC8.png)


- IN Deployment Configuration choose Add from config map or secret and add the values of our secret.
- add `dbcred` to name and choose `dbcred` resource and `dbcred` key.
- Remove the empty Environment Variable and click create.

![](snaps/OC10.png)



***6- monitor the build and deployment process***

- you can monitor the build process and the deployment process till it's done.
- Also notice the app route (URL)

![](snaps/OC11.png)


***7- Verify the app works and connects to db2 database***

(optional)Remember to open the db2 console to watch changes if you want. please note that db2 lite plan gives you one  schema where you can create table and it has the same name as your user in the service credentials so watch changes there

Wait for the app to be completely deployed then try it by pressing on the Application URL in the routes section.

**the app has four URLs**

- 1- main URL: (the APP exposed route)    
  It shows that the App is online and also creates a table named values in the db2 database
  

- 2- insert name URL: (the APP exposed route)/insertname  
  This URL inserts a name in the table we created on the db2 database
  
  ![](snaps/OC13.png)

  
- 3- table content URl:(the APP exposed route)/db2  
   This URL shows the data in the values table
   


- 4- Delete table URl:(the APP exposed route)/deletetable  
   This URL deletes the values table from db2 database
   
   ![](snaps/OC15.png)

# Summary

In this tutorial we saw how easy it is to deploy an application and connect it to a db2 database on IBM Cloud in a matter of minutes. Openshift identified, containerized, built and deployed our application for us.
This shows how you can build applications with different source codes and connect it to other services securely without the fear of any sensitive data exposed (the db2 credentials in our case) thanks to OpenShift Secrets.       


Learn more about REDHAT Openshift [HERE](https://learn.openshift.com/).you can also try OpenShift [HERE](https://www.openshift.com/try)
