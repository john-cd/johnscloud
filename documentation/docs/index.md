# John's Cloud

You will find in this repo collected CloudFormation templates, Bash and Python scripts that I use regularly in my own AWS cloud setups.


## Useful Links / Template Sources

[startup-kit-templates](https://github.com/awslabs/startup-kit-templates)

[AWS CloudFormation Sample Templates](https://github.com/awslabs/aws-cloudformation-templates)

[Cloudonaut](https://cloudonaut.io/templates-for-aws-cloudformation/)

[Free Templates for AWS CloudFormation (Cloudonaut)](https://github.com/widdix/aws-cf-templates)

[Deploying Microservices with Amazon ECS, AWS CloudFormation, and an Application Load Balancer](https://github.com/awslabs/ecs-refarch-cloudformation)


## CloudFormation Templates

### VPC folder

The VPC template is the foundation for everything else. It creates a VPC that includes
the following network resources:
- Two public subnets.
- Two private subnets.
- A NAT Gateway to allow instances in private subnets to communicate with AWS services.
- Two route tables, one for public subnets and the other for private subnets.
- Security groups for an app, load balancer, database, and bastion host.
    
The bastion host is used to provide SSH access to instances with private IP addresses in
the application's security group. 
