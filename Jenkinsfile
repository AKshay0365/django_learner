pipeline{
    agent any
    
    stages{
        stage("GitHub Repo Clone"){
            steps{
                echo "Github Data Cloning"
                git url:"https://github.com/AKshay0365/expense_tracker_project.git", branch:"main"
                
            }
        }
        stage("Image Build"){
            steps{
                echo "Docker image building"
                sh "docker build -t expense ."
            }
        }
        stage("Push Image to DockerHub"){
            steps{
                echo "pushing image to dockerHub"
                withCredentials([usernamePassword(credentialsId: "dockerHub",passwordVariable: "dockerHubpass",usernameVariable: "dockerHubuser")]){
                echo "credentials are taken"
                sh "docker tag expense ${env.dockerHubuser}/expense:latest"
                sh "docker login -u ${env.dockerHubuser} -p ${env.dockerHubpass}"
                sh "docker push ${env.dockerHubuser}/expense:latest"
                }
            }
        }
        stage("Deployment"){
            steps{
                echo "Final deploment on server"
                sh "docker run -d -p 8000:8000 akshay0365/expense:latest"
            }
        }
    }
}
