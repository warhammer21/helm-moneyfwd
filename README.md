## Infra needed to run this setup
<br/>
<br/>
1. you need to make sure **warhammer21/helmchart** tag is replaced with wherever you want your docker image to be pushed and pulled from <br />
repplace from all these places with your tag, these places are the value files used for helm and dev-prod is CI/CD pipeline workflow: <br/>
values.yaml <br />
values-dev.yaml <br />
values-prod.yaml <br />
dev_prod.yaml <br />
store your hub username/pass by **DOCKER_HUB_USERNAME**,**DOCKER_HUB_ACCESS_TOKEN** as GitHub secret  <br />
<br/>
<br/>
3. set up a GKE cluster <br />
create name spaces using the follwing <br />
**kubectl create namespace dev** <br />
**kubectl create namespace prod** <br />
store GKE credentials **GKE_SA_KEY** as a GitHub secret. <br/>
store **GKE_CLUSTER_NAME,GKE_CLUSTER_ZONE,GKE_PROJECT_ID**  as GitHub secret

## Explanation of the workflow and logic 

Build Job<br />
Purpose: Build and push Docker images.<br />
Steps: Checkout code, set up Docker Buildx, login to Docker Hub, build and push Docker image.<br />

Deploy to Dev Job<br />
Purpose: Deploy the application to the development environment.<br />
Steps: Checkout code, authenticate to Google Cloud, get GKE credentials, install Helm, deploy Helm chart to the dev namespace, and run linting tests.<br />

Deploy to Prod Job<br />
Purpose: Deploy the application to the production environment.<br />
Steps: Checkout code, authenticate to Google Cloud, get GKE credentials, install Helm, deploy Helm chart to the prod namespace, and expose the service via a LoadBalancer.<br />

Testing<br />
Simple Test: Run linting tests to validate the Helm charts.<br />








