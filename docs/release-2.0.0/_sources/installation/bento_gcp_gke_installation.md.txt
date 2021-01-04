# Deploying Bento on GCP 
This is the user documentation on provisioning bento on AWS.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f4d5afb8403642dbab917cb4aa4ef47d)](https://www.codacy.com/gh/CBIIT/icdc-dataloader?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=CBIIT/icdc-dataloader&amp;utm_campaign=Badge_Grade)


## Introduction
The purpose of this guide is to provide instructions on how to provision and deploy Bento Framework on GCP using google kubernetes engine. This guide assumes that the Custodian has an operating account with Google Cloud Platform.

### Disclaimer
GCP is a Pay As You Go provider, as result the use of this instruction may result in  usage charges. We're in no way responsible for any charges incurred from resources created using this documentation.

All scripts related to this documentation can be found here: [Bento Custodian](https://github.com/CBIIT/bento-cloudrun)

## Pre-requisites
This instructions assumed you have a google account and a project with billing enabled. In addition, you will need terraform and git installed.

* [Google account](https://cloud.google.com)
* [Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html#install-terraform)
* [gcloud](https://cloud.google.com/sdk/install)
* [GCP Project](https://cloud.google.com/appengine/docs/standard/nodejs/building-app/creating-project)

## Architecture
The code in this demo will create the following resources via Terraform:

* A new VPC and new VPC subnets
* A Cloud NAT router for egress access from the VPC subnets
* A GCE Instance serving as a Bastion Host
* A Private GKE Cluster with two nodes running two services - frontend and backend
* Neo4j Database in private subnets


## Installations

* Clone [Bento Custodian](https://github.com/CBIIT/bento-custodian) repository

```
bento@custodian:~$ git clone https://github.com/CBIIT/bento-custodian
```

* Change directory to gke workspace

```
bento@custodian:~$ cd bento-custodian/terraform/gke
```

* Authenticate gcloud client

```
bento@custodian:~$ gcloud auth login
```

* Create google project. The name of the project can be anything you want or you may run **gcloud config set project PROJECT_NAME** to use existing project where **PROJECT_NAME** is the name of your project. 

```
bento@custodian:~$ gcloud projects create PROJECT_NAME
```

* Configure gcloud to use the newly created project or you use existing one.

```
bento@custodian:~$ gcloud config set project PROJECT_NAME
```

* Create service account. Note you can name it anything you want, in this example I am calling it bento-sa

```
bento@custodian:~$ gcloud iam service-accounts create bento-sa
```

* List and copy the email address of the service account

```
bento@custodian:~$ gcloud iam service-accounts list
NAME  EMAIL                                               DISABLED
      bento-sa@bento-cloudrun.iam.gserviceaccount.com  False
```

* Create a credential key for the service account. Note the name of the file can be anything but ensure it ends with **.json**. Google allows other file formats but in this example I will be using json format.

```
bento@custodian:~$ gcloud iam service-accounts keys create gcloud_api_key.json --iam-account=bento-sa@bento-cloudrun.iam.gserviceaccount.com
```

* Get your Billing Account ID

```
bento@custodian:~$ BILLING_ACCOUNT=$(gcloud beta billing accounts list | cut -d " " -f1 | grep -v "ACCOUNT_ID")
```

* Link your project to Billing account

```
bento@custodian:~$ gcloud beta billing projects link bento-cloudrun --billing-account $BILLING_ACCOUNT
```

* Enable google cloud services apis

```
bento@custodian:$ gcloud services enable cloudresourcemanager.googleapis.com
bento@custodian:$ gcloud services enable iam.googleapis.com
bento@custodian:$ gcloud services enable cloudbilling.googleapis.com
bento@custodian:$ gcloud services enable compute.googleapis.com
bento@custodian:$ gcloud services enable run.googleapis.com
bento@custodian:$ gcloud services enable vpcaccess.googleapis.com
```

* Grant IAM roles to the service account

```
bento@custodian:$ gcloud projects add-iam-policy-binding  bento-cloudrun --member serviceAccount:bento-sa@bento-cloudrun.iam.gserviceaccount.com --role roles/owner

```

* Generate SSH Keys. We need to generate ssh key in order to connect to the database instance and the bastion host that we will be creating. 

*  Enter **ssh-keygen -t rsa -f FILENAME** at the prompt as shown below

```
bento@custodian:~$ ssh-keygen -t rsa -f bento-ssh-key
```
* Hit Enter key for the question **Enter passphrase (empty for no
    passphrase)** to skip password. Hit Enter key again for the confirmation **Enter same passphrase
    again**
    
```
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in bento-ssh-key.
Your public key has been saved in bento-ssh-key.pub.
```

* Your ssh key will be generated at the location specified. Note you
will have two files, one is your private key and the other is the public key with **.pub** extension

* Edit Terraform vars.tfvars file. Using your favorite editor, open vars.tfvars file. At minimum you will need to provide value to the following.

    * public_ssh\_key = name of the ssh public key generated earlier
    * private_ssh\_key = name of the ssh private key generated earlier
    * gcp_auth\_file = name of the service account key generated earlier
    * gcp_region = gcp region to use for this deployment
    * gcp_project = name of the gcp project created earlier
    * stack_name = can be anything
    * service_account\_id = name of the service account created earlier
   
* Run **terraform init** 

```
bento@custodian:~$ terraform init
```

*  Run **terraform plan** to see what resources will be created.

```
bento@custodian:~$ terraform plan -var-file=vars.tfvars
```

* Review the output of the above command. It will show all the resources to be created.
* Run **terraform apply** to provision your Bento environment

```
bento@custodian:~$ terraform apply -var-file=vars.tfvars -auto-approve
```

* At this point if there are no errors your custodian will be provisioned. Navigate to the url listed at the end of the terraform output. Note it will take about 10 minutes for the application to completely deployed.

```
Outputs:

backend_url = https://bento-cloudrun-backend-rxpxr4ih3q-uk.a.run.app
bastion_host_private_ip = 172.16.1.2
bastion_host_public_ip = 34.86.56.119
db_private_ip = 192.168.5.2
frontend_url = https://bento-cloudrun-frontend-rxpxr4ih3q-uk.a.run.app
service_id = bento-sa@bento-cloudrun.iam.gserviceaccount.com
```
	 
* Navigate to **frontend_url** in your browser.

* Run **terraform destroy** to destroy the resources provisioned.

```
terraform destroy -var-file=vars.tfvars -auto-approve
```

	
