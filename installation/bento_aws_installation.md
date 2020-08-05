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
* Registered Domain. This document assumes that the Custodian has a registered domain, for example **custodian.io**
* Terraform
* AWS CLI

## Installations

### Create Hosted Zone for your Domain
*  Open Amazon Route 53 [console](https://console.aws.amazon.com/route53/home)
*  Click **Hosted Zones** in the navigation pane
*  Click **Create Hosted Zone**
*  In **Domain Name**, enter domain name, example **custodian.io**
*  Select Public Hosted Zone for the **Type**
*   Click **Create**

### Request Free Public Wildcard Certificates for you domain
* Open the ACM [console](https://console.aws.amazon.com/acm/home). 
* Click **Get Started** if this is your first time visiting this resource page. You will have two options on the Get Started page. You want to get started with **Provision Certificates** 
* On the **Request a certificate** page, choose **Request a public certificate** and **Request a certificate** to continue.
* In the **Add domain names** page, type your domain name. example **custodian.io**.
* Choose **Next**.
* On the **Select validation method** page, choose **DNS validation**.
* On the **Add tags** page, you can optionally tag your certificate.
* If the **Review** page contains correct information about your request, choose **Confirm and request**.
* A confirmation page will show that your request is being processed and that certificate domains are being validated
* In the validation page, expand the downward arrow next to the domain name and the wildcard domain. **Choose Create record in Route 53** to automatically validate your request

### Generate ssh key
This step assumes you have a linux shell terminal or Mac OS terminal.

* Open terminal.
*  Enter **ssh-keygen -t rsa** at the prompt as shown below

```
bento@custodian:~$ ssh-keygen -t rsa
```

* Enter the path for to save the file. Example

```
bento@custodian:~$ Generating public/private rsa key pair.
bento@custodian:~$ Enter file in which to save the key (/home/bento/.ssh/id_rsa): /home/bento/custodian_rsa
```
Note if you don't have existing private key, you may simply enter to
accept the default.
* Hit Enter key for the question **Enter passphrase (empty for no
    passphrase)**
    
```
bento@custodian:~$ Enter passphrase (empty for no passphrase):
```

* Hit Enter key again for the confirmation **Enter same passphrase
    again**:
    
```
bento@custodian:~$ Enter same passphrase again:
```

* Your ssh key will be generated at the location specified. Note you
    will have two files, one is your private key and the other is the public
    key with **.pub** extension
    
```
bento@custodian:~$
Your identification has been saved in /home/bento/custodian_rsa.
Your public key has been saved in /home/bento/custodian_rsa.pub.
```

* Copy the content of the public key using your favorite text editor.

    
### Upload ssh key to AWS

* Open the Amazon EC2 [console](https://console.aws.amazon.com/ec2/)
* In the navigation pane, choose **Key Pairs**.
* Choose **Import key pair** under action menu
* For **Name**, enter a descriptive name for the key pair.
*  Either choose **Browse** to navigate to and select your public key or paste the contents of your public key into the **Public key contents** field.
*  Choose **Import key pair**.
*  Verify that the key pair you imported appears in the list of key pairs.

### Create SSH Public Key Parameter in SSM

* Open Amazon System Manager [console](https://console.aws.amazon.com/systems-manager/home)
* Click **Parameter Store** in the navigation pane.
*  Click **Create parameter**.
*  Enter name for the ssh public key parameter in the **Name** box. Paste the content of the ssh public key created earlier in the **Value** box. Note this is just a parameter, you may name it anything you want but we will use it later.

### Setup AWS CLI

* Follow the instruction on official Amazon Web site to install AWS CLI and set up credential on your local machine using platform instruction applicable to you.
* AWS CLI [installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
* [Configure](https://docs.aws.amazon.com/sdk-for-java/v1/developer-guide/setup-credentials.html) AWS Credential 


### Setup Terraform

* Follow the instruction on the official [Terraform](https://learn.hashicorp.com/terraform/getting-started/install.html) site to install terraform on your local workstation using platform instruction applicable to you.

### Deploy Bento Framework

* Note the steps below assumed you have **git** already installed
* Clone  [Bento Framework](https://github.com/CBIIT/bento-custodian) to a temporary
    directory **/tmp**
    
```
bento@custodian:~$ cd /tmp
bento@custodian:/tmp$ git clone https://github.com/CBIIT/bento-custodian
```

* Change directory to terraform **cd bento-custodian/terraform**

```
bento@custodian:/tmp$ cd bento-custodian/terraform
```
*  Using your favorite text editor open and edit **vars.tfvars** file. This is a variable file that will be used as input to the terraform. At minimum, you will need to provide appropriate value for the following;
	*  profile - this is your AWS profile configured in Setup AWS CLI
	*	domain_name - your domain name
	*	ssh_key_name - this is the name of the ssh public key imported to AWS
	*	ssm_ssh_public_key_name - this the name of the parameter you created in SSM


* Export [AWS_PROFILE](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html) environment variable in your local machine's terminal. Note you may skip this step if you have only **default** profile configured from setting up AWS CLI steps above. This is only required if you have more than one AWS Credential profiles configured. The example command below export custodian profile configured under ~/.aws/credentials

```
bento@custodian:~$ export AWS_PROFILE=custodian
```

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
Apply complete! Resources: 72 added, 0 changed, 0 destroyed

Outputs:

admin_user = bento
bastion_host_ip = 54.83.165.61
custodian_api_endpoint = api.mycloudwork.com
custodian_url = custodian.mycloudwork.com
```

