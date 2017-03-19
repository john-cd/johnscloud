# John's Cloud

You will find in this repo collected CloudFormation templates, Bash and Python scripts and Docker images that I use regularly in my own AWS cloud setups.

## ``utils`` folder

Simple scripts to convert JSON CloudFormation templates or config files into YAML format


## ``src\infrastructure`` folder

CloudFormation Templates 


## Work in Progress

### VPC CloudFormation Template

The VPC template is the foundation for everything else. It creates a VPC that includes
the following network resources:

- Two public subnets.
- Two private subnets.
- A NAT Gateway to allow instances in private subnets to communicate with AWS services.
- Two route tables, one for public subnets and the other for private subnets.
- Security groups for an app, load balancer, database, and bastion host.
    
The bastion host is used to provide SSH access to instances with private IP addresses in
the application's security group. 
