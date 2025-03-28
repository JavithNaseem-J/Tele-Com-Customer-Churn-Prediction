# Tele Com Customer Churn Prediction
Below is a detailed, step-by-step guide to set up your project, including cloning the repository, creating a local environment, and configuring AWS CI/CD deployment with GitHub Actions. This response is tailored to your query and ensures a complete, self-contained explanation.


## **Local Setup Steps**

### **1. Clone the Repository**
- **Description**: Clone the GitHub repository to your local machine to access the project files.
- **Command**:
  ```bash
  git clone https://github.com/entbappy/Tele-Com-Customer-Churn-Prediction.git
  ```
- **Notes**:
  - Ensure Git is installed on your system. If not, download it from [git-scm.com](https://git-scm.com/).
  - After cloning, navigate into the project directory:
    ```bash
    cd Tele-Com-Customer-Churn-Prediction-
    ```

### **2. Create a Conda Environment**
- **Description**: Set up a virtual environment using Conda to manage dependencies.
- **Commands**:
  ```bash
  conda create -n mlproj python=3.10 -y
  conda activate mlproj
  ```


### **3. Install Requirements**
- **Description**: Install the project’s dependencies listed in `requirements.txt`.
- **Command**:
  ```bash
  pip install -r requirements.txt
  ```

### **4. Run the Application**
- **Description**: Launch the web application locally to test it.
- **Command**:
  ```bash
  python app.py
  ```

---

## **AWS CI/CD Deployment with GitHub Actions**

### **1. Log in to AWS Console**
  - Go to [aws.amazon.com](https://aws.amazon.com/) and sign in.
  - If you don’t have an account, create one and set up billing.


### **2. Create an IAM User for Deployment**
  - Navigate to IAM > Users > Add user in the AWS Console.
  - Set a username (e.g., `deployment-user`).
  - Select **Programmatic access** as the access type.
  - Attach the following policies:
    - `AmazonEC2ContainerRegistryFullAccess`: Grants full access to ECR.
    - `AmazonEC2FullAccess`: Grants full access to EC2.
  - Review and create the user.
  - Save the **Access Key ID** and **Secret Access Key** securely.

### **3. Create an ECR Repository**
  - Go to ECR > Repositories > Create repository in the AWS Console.
  - Select **Private** and name it (e.g., `mlproj`).
  - Note the repository URI (e.g., `970547337635.dkr.ecr.ap-south-1.amazonaws.com/mlproj`).


### **4. Create an EC2 Instance**
  - Go to EC2 > Instances > Launch Instance in the AWS Console.
  - Choose an Ubuntu AMI (e.g., Ubuntu Server 20.04).
  - Select an instance type (e.g., `t2.micro` for free tier eligibility).
  - Configure a security group:
    - Allow inbound traffic on port 22 (SSH).
    - Allow the port your app uses (e.g., 5000).
  - Launch the instance and download the key pair (e.g., `my-key.pem`).
- **Notes**:
  - Store the key pair securely; it’s required to SSH into the instance.

### **5. Install Docker on EC2**
  ```bash
  sudo apt-get update -y
  sudo apt-get upgrade -y
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo usermod -aG docker ubuntu
  newgrp docker
  ```
- **Notes**:
  - SSH into your EC2 instance first (e.g., `ssh -i my-key.pem ubuntu@<ec2-public-ip>`).
  - These commands update the system and install Docker, adding the `ubuntu` user to the Docker group.

### **6. Configure EC2 as a Self-Hosted Runner**
  - Go to your GitHub repository > Settings > Actions > Runners > New self-hosted runner.
  - Select the OS (Linux) and architecture (X64).
  - Follow the provided instructions to:
    - Download the runner software.
    - Configure it with a token.
    - Start the runner on your EC2 instance.
- **Notes**:
  - Run the commands one by one on your EC2 instance via SSH.
  - This enables GitHub Actions to execute workflows on your EC2 machine.

### **7. Set Up GitHub Secrets**
  - Go to your GitHub repository > Settings > Secrets > New repository secret.
  - Add the following secrets:
    - `AWS_ACCESS_KEY_ID`: Your IAM user’s access key.
    - `AWS_SECRET_ACCESS_KEY`: Your IAM user’s secret key.
    - `AWS_REGION`: The region of your ECR (e.g., `ap-south-1` or `us-east-1` as per your query).
    - `AWS_ECR_LOGIN_URI`: The ECR login URI (e.g., `970547337635.dkr.ecr.ap-south-1.amazonaws.com`).
    - `ECR_REPOSITORY_NAME`: The name of your ECR repository (e.g., `mlproj` or `simple-app` as per your query).
