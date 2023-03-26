# Technical Challenge

1. Please develop an application in Python or Nodejs which encodes the text passed as input.
    Encoding will add 5 positions. For example:

    - "AbcXyz" -> "FghCde"
    - "012789" -> "567234"
    - "TX Group was found in 2019" ->

    Make the application expose a REST API with the following routes on the port 80:

    - `GET /{n}` returns a JSON payload with the result of the application transformation.
    - `GET /status` returns the JSON payload: `{"status":"ok"}`.

2. A docker image of the App has to be built and pushed to a container registry.
We expect this process to be triggered whenever a pull request to change the content of the Docker folder is made.

    Structure:

    ```sh
    .github/workflows - stores GitHub action code.
    terraform - stores Terraform code.
    terraform/values - stores Helm charts values for the helm chart deployments in the EKS cluster.
    docker - stores the Docker file and scripts.
    kustomize - stores the kustomize files.
    config - stores the configuration files for the linting and testing tools.
    ```

3. The docker image has to be retrieved from the registry and deployed as a Docker container in the EKS cluster (through Helm or Terraform).

    Requirements:

    - 2 replicas, in different AZs.
    - Use the already defined ingress.

    There's no need to test the deployment in AWS, since it might cause some costs. Our goal is to test:

    - Coding skills.
    - Docker skills.
    - CICD skills.
    - Terraform skills.
    - AWS understanding.
