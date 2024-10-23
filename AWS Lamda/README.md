# AWS Lambda
This is a simple example of how to create a AWS Lambda function usiin IaC (Infrastructure as Code).

## Prerequisites
- AWS CLI
- AWS SAM CLI
- AWS account

## Steps
1. Create a new directory for the project
2. Type `sam init` to create a new project
3. Choose the `AWS Quick Start Templates` option
4. Choose the `1 - Hello World Example` option
5. In `Use the most popular runtime and package type?` type `y` and press `Enter`
6. In `Would you like to enable X-Ray tracing on the function(s) in your application?t ` type `y` and press `Enter`
7. In `Would you like to enable monitoring using CloudWatch Application Insights?` type `y` and press `Enter`
8. In `Would you like to set Structured Logging in JSON format on your Lambda functions? ` type `N` and press `Enter`
9. Ingress the project name and press `Enter`


note:
>[!NOTE]
> Commands you can use next
> =========================
> [*] Create pipeline: cd hello-lambda && sam pipeline init --bootstrap
>[*] Validate SAM template: cd hello-lambda && sam validate
>[*] Test Function in the Cloud: cd hello-lambda && sam sync --stack-name {stack-name} --watch