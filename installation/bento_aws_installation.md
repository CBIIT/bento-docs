---
layout: default
nav_order: 1
title: Bento Framework on AWS
---

# Deploying Bento on AWS
This is the user documentation on provisioning bento on AWS.

[![Codacy Badge](https://app.codacy.com/project/badge/Grade/f4d5afb8403642dbab917cb4aa4ef47d)](https://www.codacy.com/gh/CBIIT/icdc-dataloader?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=CBIIT/icdc-dataloader&amp;utm_campaign=Badge_Grade)


## Introduction
The purpose of this guide is to provide instructions on how to provision and deploy Bento Framework on AWS cloud platform. This guide assumes that the Custodian has an operating account with Amazon Web Services
[Amazon Web Services](https://aws.amazon.com) and all the necessary administrator's IAM role and permissions in order to create cloud resources. 
### Disclaimer
AWS is a Pay As You Go provider, as result the use of this instruction may result in  usage charges. We're in no way responsible for any charges incurred from resources created using this documentation.

All scripts related to this documentation can be found here: [Bento Custodian](https://github.com/CBIIT/bento-custodian)

## Pre-requisites
* git
* Terraform


## Installations

### Clone Bento Framework

* Note the steps below assumed you have **git** already installed
* Clone  [Bento Framework](https://github.com/CBIIT/bento-custodian) to a temporary
    directory **/tmp**
    
```
bento@custodian:~$ cd /tmp
bento@custodian:/tmp$ git clone https://github.com/CBIIT/bento-custodian
```

* Change directory to terraform **cd bento-custodian/terraform/aws**

```
bento@custodian:/tmp$ cd bento-custodian/terraform/aws
```

### Generate ssh key
This step assumes you have a linux shell terminal or Mac OS terminal.

We need to generate ssh key in order to connect to the database instance and the bastion host that we will be creating. 

*  Enter **ssh-keygen -t rsa -f FILENAME** at the prompt as shown below

```
bento@custodian:~$ ssh-keygen -t rsa -f bento-ssh-key
```

* Hit the **Enter** key for the question **Enter passphrase (empty for no
    passphrase)** to skip password. 
* Hit the **Enter**  key again for the confirmation **Enter same passphrase
    again**
    
```
Generating public/private rsa key pair.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in bento-ssh-key.
Your public key has been saved in bento-ssh-key.pub.
```

* Your ssh key will be generated and stored at the current working directory. Note you
will have two files, one is your private key and the other is the public key with **.pub** extension

* Copy the content of the public key using your favorite text editor.

    
### Upload ssh key to AWS

* Open the Amazon EC2 [console](https://console.aws.amazon.com/ec2/)
* In the navigation pane, choose **Key Pairs**.
* Choose **Import key pair** under action menu
* For **Name**, enter a descriptive name for the key pair.
*  Either choose **Browse** to navigate to and select your public key or paste the contents of your public key into the **Public key contents** field.
*  Choose **Import key pair**.
*  Verify that the key pair you imported appears in the list of key pairs.


### Setup Terraform

* Follow the instruction on the official [Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html) site to install terraform on your local workstation using platform instruction applicable to you.


### Populate vars.tfvars file

*  Using your favorite text editor open and edit **vars.tfvars** file. This is a variable file that will be used as input to the terraform. Please refer to **variables.tf** file for full descriptions of each the variables listed in thevars.tfvars file. 
*  At minimum, you will need to provide appropriate value for the following;
	*  access_key  - your aws credential access key
	*  secret_key  - your aws credential secret key
	*	domain_name - your domain name
	*	ssh_key_name - this is the name of the ssh public key imported to AWS
	*	ssh_public_key_filename - this is the filename of the ssh public key. **Note** it must end with **.pub**. Keep the file location default to the current working directory


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

* At this point if there are no errors your custodian will be provisioned. Navigate **custodian_url**  listed at the end of the terraform output. Note it will take about 10 minutes for the application to completely deployed.


```
Apply complete! Resources: 68 added, 0 changed, 0 destroyed.

Outputs:

admin_user = evay
bastion_host_ip = 12.13.14.15
custodian_api_endpoint = http://evay-alb-2073444928.us-east-1.elb.amazonaws.com/api/graphql/
custodian_url = http://evay-alb-2073444928.us-east-1.elb.amazonaws.com
```

* Run **terraform destroy** to destroy the resources provisioned.

```
bento@custodian:~$ terraform destroy -var-file=vars.tfvars -auto-approve
```
