#!/bin/bash

# Create the S3 Gateway, replacing the blanks with the VPC and Routing Table Ids: aws ec2 create-vpc-endpoint --vpc-id _______ --service-name com.amazonaws.region.s3 \ --route-table-ids _______

aws ec2 create-vpc-endpoint --vpc-id vpc-05f119bdeb0799d1b --service-name com.amazonaws.us-east-1.s3 --route-table-ids rtb-0247af10c27028544