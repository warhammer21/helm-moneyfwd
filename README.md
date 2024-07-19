## Infra needed to run this setup

1. you need to make sure **warhammer21/helmchart** tag is replaced with wherever you want your docker image to be pushed and pulled from
replace from all these places with your tag, these places are the value files used for helm and dev-prod is CI/CD pipeline workflow: <br/>

      values.yaml <br />
      values-dev.yaml <br />
      values-prod.yaml <br />
      dev_prod.yaml <br />

store your hub username/pass by **DOCKER_HUB_USERNAME**,**DOCKER_HUB_ACCESS_TOKEN** as GitHub secret  <br />

2. set up a GKE cluster <br />

      create name spaces using the follwing <br />
      **kubectl create namespace dev** <br />
      **kubectl create namespace prod** <br />
      store GKE credentials **GKE_SA_KEY** as a GitHub secret. <br/>
      store **GKE_CLUSTER_NAME,GKE_CLUSTER_ZONE,GKE_PROJECT_ID**  as GitHub secret

3. Trigger a simple commit to Main and the workflow should trigger to deploy helm chart on GKE <br />
   
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

Final result <br />
<img width="2420" alt="Screenshot 2024-07-19 at 2 55 37 PM" src="https://github.com/user-attachments/assets/298d6f04-6f20-46b5-b76f-b6c6f3a74556">

## Why This Workflow Makes Sense for an ML Team<br />

Build Job<br />
Ensures that Docker images are consistently built and pushed to Docker Hub. This process is essential for maintaining reproducibility and alignment among team members working on various ML models and services.<br />

Deploy to Dev Job<br />
Allows for testing and validation in a dedicated development environment. This step is crucial for catching issues early, verifying functionality, and running initial tests on the ML models before they reach production.<br />

Deploy to Prod Job<br />
Handles the deployment to production only after the changes have been validated in the development stage. This cautious approach minimizes the risk of introducing errors into the live environment and ensures that the application is robust and stable.<br />

Testing<br />
Incorporates linting and validation checks on Helm charts to ensure that deployments are correctly configured and free from common issues. This step is vital for maintaining deployment quality and avoiding configuration errors.<br />

By structuring the workflow in this way, the ML team benefits from streamlined CI/CD processes, improved code quality, and reduced risk of errors in production deployments. This approach supports efficient collaboration, enhances model reliability, and ensures that updates are safely and effectively managed.


## Ideal Setup<br />
Given more time, the ideal setup would involve:<br />

PR Stage<br />
On every pull request (PR), trigger a temporary build in a dedicated development environment.<br />
This allows developers to test their changes in isolation before merging.<br />

Development Verification<br />
Once the developer is confident in their changes, they can request a senior team member to review and merge the PR.<br />
Merging to the main branch triggers a build and deploy to a staging environment.<br />

Staging Deployment<br />
This deployment includes comprehensive testing to ensure the stability and functionality of the application.<br />
The staging environment simulates production but is used for final verification.<br />

Production Deployment<br />
After successful staging, a senior team member manually initiates the production deployment.<br />
This manual step ensures that all changes are thoroughly reviewed and validated before going live.<br />







