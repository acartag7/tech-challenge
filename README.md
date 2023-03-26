# Tech Challenge: Decision Log

This document is a record of the technical decisions made for the Tech Challenge.

## Table of Contents

- [Encoder Application](#encoder-application)
- [Docker Image](#docker-image)
- [Testing](#testing)
- [Linting](#linting)
- [Build](#build)
- [CI](#ci)
- [CD](#cd)
- [Deployment](#deployment)

## Encoder Application

The encoder application is a simple Python script that takes a string as input and returns the encoded string as output. The encoding is done by adding 5 to the ASCII value of each character. The application exposes a REST API with the following routes:

- `GET /{n}` returns a JSON payload with the result of the application transformation.
- `GET /status` returns the JSON payload: `{"status":"ok"}`.
- `GET /help` returns a help message.
- `GET /!` returns a 400 error as the input is not a alphanumeric string.

Regarding the framework, I decided to use Flask as it is a lightweight framework that is easy to use and deploy. I wanted to keep the application as simple as possible.
Flask provides several useful features for building web applications, such as routing, request handling, and templating.
Flask also provides a built-in development server that makes it easy to test and debug your application during development.

Overall, Flask is a good choice for building simple web applications and APIs in Python, thanks to its simplicity, flexibility, and ease of use.

## Docker Image

The Docker image is built using the Dockerfile in the `docker` folder.
This Dockerfile uses the `python:3.11.2-slim-bullseye` base image to build a lightweight Docker image for the Tech Challenge Character Encoder app. It sets up the app to run on port 80, uses a non-root user for security, and includes a health check for the /status endpoint. The use of a health check ensures that the container is healthy before it is added to a load balancer or other service discovery mechanism."

## Testing

The application is tested using the `pytest` framework. The tests are located in the `tests` folder. The tests cover the following scenarios:

- Test that the application returns a 400 error when the input is not a alphanumeric string.
- Test that the application returns a 200 status code when the input is a alphanumeric string.
- Test that the application returns the correct encoded string when the input is a numeric string.
- Test that the application returns the correct encoded string when the input is a alphanumeric string.
- Test that the application returns a 200 status code when the /status endpoint is called.
- Test that the application returns a 200 status code when the /help endpoint is called.

The tests are run using the `pytest` framework. The tests are run in a GitHub action workflow that is triggered whenever a pull request is made to the `main` branch. The workflow runs the tests and outputs the results.

## Linting

We are running linters for the python code, markdown code and yaml code. The linters are run in a github workflow that is triggered whenever a pull request is made to the `main` branch. The workflow runs the linters and outputs the results.

## Build

The application is built using the `docker build` command. The build is run in a GitHub action workflow that is triggered whenever a pull request is made to the `main` branch. The workflow builds the Docker image and pushes it an AWS ECR repository.

## CI

This GitHub Actions workflow that performs linting and testing on a Python project. It includes four jobs: python-lint, yaml-lint, markdown-lint, and test.
The workflow is triggered on pull requests to the main branch or from a workflow call.

Here's an overview of the workflow:

- The job is triggered on a pull request on the main branch, or when it is called as a sub-workflow. It consists of four separate jobs, each with its own set of steps:

- python-lint: This job installs the necessary dependencies, such as pip, pylint, and pytest. It then runs pylint on all Python files in the repository to ensure that they conform to coding standards.

- yaml-lint: This job installs yamllint and uses it to check the syntax of all YAML files in the repository against a specified configuration file.

- markdown-lint: This job installs markdownlint-cli and uses it to check the syntax of all Markdown files in the repository against a specified configuration file.

- test: This job installs the necessary dependencies, such as pip, pylint, and pytest. It then runs pytest to execute all Python unit tests in the repository.

Overall, this workflow is designed to ensure that the Python code in the repository is well-formatted and free of errors and that all unit tests pass. It is a good practice to run such automated tests as part of a continuous integration (CI) process to ensure that the codebase remains healthy and maintainable over time.

## CD

This GitHub Actions workflow builds a Docker image, pushes it to an Amazon Elastic Container Registry (ECR), scans it for vulnerabilities using Trivy, and deploys it to an Amazon Elastic Kubernetes Service (EKS) cluster.

Here's an overview of the workflow:

- The workflow runs when a push is made to the main branch.
- The first job, build-and-push-image, checks out the code, configures AWS credentials, logs in to the ECR, builds and tags the Docker image, and pushes the image to the ECR.
- The second job, vulnerability-scan, configures AWS credentials, logs in to the ECR, and uses the Trivy vulnerability scanner to scan the Docker image for critical vulnerabilities.
- The third job, deploy, configures AWS credentials, checks out the code, logs in to the ECR, updates the kubeconfig for the EKS cluster, uses Kustomize to set the Docker image tag in the Kubernetes deployment manifest, applies the manifest, waits for the deployment to finish rolling out, and gets the hostname for the Kubernetes service.

### Here are the steps performed by each job

#### build-and-push-image job

- Check out the code using the actions/checkout action.
- Configure AWS credentials using the aws-actions/configure-aws-credentials action and the secrets stored in the repository.
- Log in to the ECR using the aws-actions/amazon-ecr-login action.
- Build the Docker image using the docker build command and tag it with the SHA of the commit that triggered the workflow and with the latest tag.
- Push the Docker image to the ECR using the docker push command.

#### vulnerability-scan job

- Configure AWS credentials using the aws-actions/configure-aws-credentials action and the secrets stored in the repository.
- Log in to the ECR using the aws-actions/amazon-ecr-login action.
- Use the aquasecurity/trivy-action action to run a vulnerability scan on the Docker image in the ECR.
- Set environment variables for the ECR registry, repository, and image tag, as well as for the AWS access key ID, secret access key, and default region.
- Set options for the trivy command, including the image reference, output format, exit code, and vulnerability types and severities to scan for.

#### deploy job

- Configure AWS credentials using the aws-actions/configure-aws-credentials action and the secrets stored in the repository.
- Check out the code using the actions/checkout action.
- Log in to the ECR using the aws-actions/amazon-ecr-login action.
- Update the kubeconfig for the EKS cluster using the aws eks update-kubeconfig command and the name of the EKS cluster stored in the secrets of the repository.
- Set environment variables for the ECR registry, repository, and image tag.
- Use the kustomize command to set the Docker image tag in the Kubernetes deployment manifest and apply the manifest using the kubectl apply command.
- Wait for the deployment to finish rolling out using the kubectl rollout status command.
- Get the hostname for the Kubernetes service using the kubectl get svc command and output it in JSON format.

## Deployment

Due to time constraints, I was not able to create the helm chart for the deployment. I have created the deployment yaml files for the deployment. The deployment yaml files are located in the `kustomize` folder.

The deployment consists of the following components:

- A Kubernetes deployment that runs the Tech Challenge Character Encoder app.
- A Kubernetes service that exposes the deployment to the internet.
- A Kubernetes ingress that routes traffic to the service.

The deployment is deployed using the `kubectl apply -k kustomize` command. The deployment is deployed in a GitHub action workflow that is triggered whenever a pull request is made to the `main` branch. The workflow deploys the application to an AWS EKS cluster.

The kubernetes deployment, is configured to use the Docker image that was built and pushed to the AWS ECR repository in the CI workflow. The replica amount can be easily set differently per environment by changing the `replicas` value in the `kustomize/overlays` files.

I've also included liveliness and readiness probes in the deployment. The liveness probe checks if the application is running. The readiness probe checks if the application is ready to accept requests. The liveness and readiness probes are configured to use the `/status` endpoint of the application. The liveness probe is configured to retry 3 times with a 5 second delay between retries. The readiness probe is configured to retry 3 times with a 5 second delay between retries.

The kubernetes service is configured to expose the deployment on port 80. The service is configured to use the `LoadBalancer` type. This means that the service will be exposed to the internet using an AWS Elastic Load Balancer (ELB). The ELB will be configured to use the `internet-facing` scheme. This means that the ELB will be publicly accessible. The ELB will be configured to use the `network` load balancer type. This means that the ELB will be configured to use the TCP protocol.

There was an ingress controller on the cluster but it didn't seem to work, so I just used the service to expose the deployment to the internet.
To test it without a domain name, I would have used:

```sh
curl -i -H "Host: mydomain.com" http://xxxxxxxxxxxxx.us-east-1.elb.amazonaws.com/hostname
```
