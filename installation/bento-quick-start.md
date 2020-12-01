---
layout: default
sort: 1
title: Bento Quick Start
---

# Quick Start Tutorial

## Introduction
Bento follows the principle of “Configure Locally. Deploy Globally”. An end-user installs a local version of his/her application and configures it to its desired state. The updated application is then pushed to a cloud platform. 
<br>The purpose of this tutorial is to walk the end-user through process of installing a data sharing platform on AWS. 

## Fork the Bento Repositories
The Bento code-base is divided into three main components: (a) the front end (b) the back end and (c) the database. The code-base for all three are stored on GitHub. Here are the repos to fork:

1.  Front End Repo: [https://github.com/CBIIT/bento-frontend.git](https://github.com/CBIIT/bento-frontend.git)

2.  Back End Repo: [https://github.com/CBIIT/bento-backend.git](https://github.com/CBIIT/bento-backend.git)

3.  Data Model: [https://github.com/CBIIT/BENTO-TAILORx-model](https://github.com/CBIIT/BENTO-TAILORx-model)

Fork each of these to create your own remote repos. Instructions on forking a GitHub repo are [here](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github/fork-a-repo).

For this tutorial we shall assume that you have named your repos:
<br>`https://github.com/CBIIT/bento-demo-frontend.git`
<br>`https://github.com/CBIIT/bento-demo-backend.git`
<br>`https://github.com/CBIIT/bento-demo-model.git` 


## Set up the Bento Local Environment on your machine.
The ‘Bento Local’ environment is designed to run within Docker, on a user's local machine, and can be set up within all types of operating systems- Windows, Mac and Unix flavors. This allows users to create and deploy their local copy of Bento, with minimal changes to their local environment.

### Prerequisites
To install the 'Bento Local' environment you will need to:

1. Install Git: Bento uses GitHub to commit, store and share its code base. Instructions to install Git, on your local machine, are found [here](https://github.com/git-guides/install-git). 

2. Install Docker: All code in Bento is containerized. You will need to install the following Docker components on your local machine: (a) Docker Desktop (b) Docker Engine and (c) Docker Compose.
    * Instructions to install Docker Desktop are [here](https://www.docker.com/products/docker-desktop).
    * Instructions to install Docker Engine are [here](https://docs.docker.com/engine/install/).
    * Instructions to install Docker Compose are [here](https://docs.docker.com/compose/install/).
    
3. (If you want to upload your own data) Ensure that your data is (a) it is Bento data model compliant and (b) you have a Neo4J dump of you data set.

The code-base to create the local environment is available at:  `https://github.com/CBIIT/bento-local`.
For this tutorial we shall consider `$src` to be the folder in which you will store all your local code for Bento.

1.  Clone the bento-local code-base in your local machine by running the following commands in `$src`. The first command initializes a git repository in `$src`; the second, clones the bento-local repo on your machine.

    ```
    git init
    
    git clone https://github.com/CBIIT/bento-local
    ```

    This creates a `bento-local` folder under `$src`.

2. Inspect the bento-local folder, by running the following commands. 

    ```
    cd bento-local/

    ls -al
    ```
The list of files in your  `bento-local` folder should look like this:

```
drwxr-xr-x  10 <your user name>  <your group name>    320 Oct 24 08:23 .
drwxr-xr-x   7 <your user name>  <your group name>    224 Oct 24 08:23 ..
-rw-r--r--   1 <your user name>  <your group name>   2037 Oct 24 08:23 .env
drwxr-xr-x  12 <your user name>  <your group name>    384 Oct 24 08:23 .git
-rw-r--r--   1 <your user name>  <your group name>  12904 Oct 24 08:23 README.md
drwxr-xr-x   4 <your user name>  <your group name>    128 Oct 24 08:23 dataloader
-rw-r--r--   1 <your user name>  <your group name>    454 Oct 24 08:23 dataloader.yml
-rw-r--r--   1 <your user name>  <your group name>   1306 Oct 24 08:23 docker-compose.yml
drwxr-xr-x   6 <your user name>  <your group name>    192 Oct 24 08:23 dockerfiles
drwxr-xr-x   6 <your user name>  <your group name>    192 Oct 24 08:23 initialization
```

3. Open the `.env` file using a text editor of your choice. 
    * Set the following variables: `FRONTEND_REPO`, `BACKEND_REPO`, `MODEL_REPO` to the URLS of your forked repos for the front end, back end and data model respectively. 
    * Set the variable BUILD_MODE to `dev`. Note: see [here](https://cbiit.github.io/bento-docs/installation/installing-bento-on-your-local-machine.html#overview) for a discussion on the three modes for Bento local environment.
    * Save and exit the `.env` file.


Here is what your `.env` file should like after you are done with your updates:

```
########################################
#                                      #
#      INITIALIZATION PROPERTIES       #
#                                      #
########################################

USE_DEMO_DATA=yes
# Set to "yes" to seed the project with the provided demo data set

BACKEND_REPO=https://github.com/CBIIT/bento-demo-backend.git
BACKEND_BRANCH=master

FRONTEND_REPO=https://github.com/CBIIT/bento-demo-frontend.git
FRONTEND_BRANCH=master

MODEL_REPO=https://github.com/CBIIT/bento-demo-model.git
MODEL_BRANCH=master
# Set these variables to the desired branches to use when initializing the project with Bento source code

########################################
#                                      #
#          RUNTIME PROPERTIES          #
#                                      #
########################################

BUILD_MODE=dev
# Defines the build type used when building the project. Available options are:  demo, build, dev

```

4. The `initialization` folder in `bento-local` stores the intialization scripts for the Bento local enviroment. Move to the appropriate `initialization` sub-folder: 
	*  `initialization/mac_linux` for Mac and Linux users
	*  `initialization/windows` for Windows users. 

This sub-folder stores the initialization script(s) for the relevant operating system. For Mac and Linux users, make the script executable and the run it:
```
    chmod a+x init.sh
    ./init.sh
```

This script clones the code from your three repos: front-end, back-end, data model in the `bento-local`folder and also creates a `data` folder in `bento-local`.
The initialization script will query you `use demo data [default=yes]:`. Type `yes` to include demo data in the `data` folder.

Note to advanced users: if you have your own Bento data model compliant data set as a Neo4J dump file, then you can store the dump file in the `bento-local/data` folder and rename it `bento-data.dump`. Bento will then display your data on the UI.

5. In the `bento-local` folder start the three docker containers with the following command:

    ```
    docker-compose up -d
    ```

Downloading all the image layers and creating the Docker containers takes about 5 minutes. 

6. To test, open a browser and go to URL: `http://localhost:8085/`. You should see the landing page for Bento: 

![Home](resources/bento-cloud/bentoindexpage.png)


## Set up Bento on AWS.
At this point in the tutorial you will have successfully set up the Bento local environment. In this section, we will walk you through the process of installing Bento on AWS.

### Prerequisites
To install the Bento in AWS you will need to:

1. Create an account on Amazon Web Services. You will need an administrator’s role on AWS, and the ability to create cloud resources. See [here](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/) for instructions on creating an AWS account.

2. Download and run the `custodian-workstation` docker image. This image is loaded with the software packages: Terraform, Ansible and AWS CLI, that you will need to deploy your platform on AWS. 
 
```console 
docker run -d --name custodian cbiitssrepo/custodian-workstation
docker exec -ti custodian bash
[root@5062d391c705 /]# 

```

3. Configure AWS CLI credentials within the `custodian-workstation` container by running `aws configure`. See below and [here](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html) for instructions on configuring AWS CLI.
```console  
[root@5062d391c705 /]# aws configure
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: 
Default output format [None]:
```



1. **Within the `custodian-workstation` container**, clone the Bento Custodian repo. The folder will be downloaded into the root folder in your container.

```
git clone https://github.com/CBIIT/bento-custodian
```

2. The `data` sub-folder under `bento-local`, created in the previous section, stores all the data that you have loaded onto your local version of Bento. Load files in the `data` folder to a S3 bucket. [This](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html) guide gives you the instructions on creating an S3 bucket and loading local files. 
    * Note 1: AWS will require your S3 bucket name to be globally unique. 
    * Note 2: For advanced users, you may load your own Bento-model compliant data set to the S3 bucket. 


3. Open the `vars.tfvars` file with an editor of your choice. The path of this file is: `/bento-custodian/terraform/aws/vars.tfvars`. 
<br> See `/bento-custodian/terraform/aws/variables.tf` for a description of the variables in `vars.tfvars`.

4. Update the following variables in `vars.tfvars`:
    * `profile`: The name of your profile as it is set in the `.aws/credential` file.
    * `region`: This is the AWS region you wish to provision your resources.
    * `backend_repo`: Your Back End Repo URL (in this case, `https://github.com/CBIIT/bento-demo-backend.git`)
    * `frontend_repo`: Your Front End Repo URL (in this case, `https://github.com/CBIIT/bento-demo-frontend.git`)
    * `data_repo`: Your Front End Repo URL (in this case, `https://github.com/CBIIT/bento-demo-model.git`)
    * `s3_bucket`: Name of the globally unique S3 bucket loaded with Bento data.
    * `s3_folder`: Name of the folder in the S3 bucket loaded with Bento data.
    <br>See below for an example `vars.tfvars` file:

```
#define any tags appropriate to your environment
tags = {
  ManagedBy = "terraform"
}
...

#enter the region in which your aws resources will be provisioned
region = <Region in which your AWS resources will be provisioned>

#specify your aws credential profile. Note this is not IAM role but rather profile configured during AWS CLI installation
profile = <Your AWS profile name>

...

#specify the url of the bento backend repository
backend_repo = <Back End Repo URL>

#specify the url of the bento frontend repository
frontend_repo = <Front End Repo URL>

#specify the url of the bento data repository

data_repo = <Data Model Repo URL>

#specify dataset to be used
s3_bucket = <S3 Bucket Name>
s3_folder = <S3 Folder Name>
...
```

5. Once the `vars.tfvars` file has been updated, run the command `terraform init`, in the folder `/bento-custodian/terraform/aws/`. 

6. Once the previous command has run successfully, run the command `terraform plan -var-file=vars.tfvars` to preview the list of resources that will be created to stand up your Bento application. 

7. If you are satisfied with the resources being created, then run the following command, in the same folder, to provision your resources:

```
terraform apply -var-file=vars.tfvars -auto-approve
```
Once deployment is complete, you will see a message similar to the following:

```
Apply complete! Resources: 68 added, 0 changed, 0 destroyed.

Outputs:

admin_user = evay
bastion_host_ip = 12.13.14.15
custodian_api_endpoint = http://evay-alb-2073444928.us-east-1.elb.amazonaws.com/api/graphql/
custodian_url = http://evay-alb-2073444928.us-east-1.elb.amazonaws.com
```
It takes about 10 minutes for complete deployment.

8. You can monitor the deployment process on AWS State Manager.
    * Open [SSM](https://us-west-1.console.aws.amazon.com/systems-manager/home)
    * Click [State Manager](https://us-west-1.console.aws.amazon.com/systems-manager/state-manager) in the left pane of the navigation
* You will see the current status of the deployment. If everything goes well the **status** should change from **Pending** to **Success** as shown below.

**Deployment Pending**
![Pending](resources/bento-cloud/bentopending.png)

**Deployment Successful**
![Success](resources/bento-cloud/bentosuccess.png)

9. Once deployment has been successfully completed navigate to the `custodian_url` (see step 7.) to view the application installed on AWS. The application should look and behave like your local copy of Bento.

![Home](resources/bento-cloud/bentoindexpage.png)






