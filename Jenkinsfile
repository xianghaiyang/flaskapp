pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-flask"
        CONTAINER_NAME = "my-flask-container"
        PORT = "8000"  // 改成你后端实际暴露的端口
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                    docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} .
                    docker tag ${IMAGE_NAME}:${BUILD_NUMBER} ${IMAGE_NAME}:latest
                """
            }
        }

        stage('Deploy') {
            steps {
                sh """
                    # 停掉并删除旧容器（如果存在）
                    if docker ps -a --format '{{.Names}}' | grep -q '^${CONTAINER_NAME}\$'; then
                        docker stop ${CONTAINER_NAME}
                        docker rm ${CONTAINER_NAME}
                    fi
                    # 启动新容器
                    docker run -d \
                        --name ${CONTAINER_NAME} \
                        --restart always \
                        -p ${PORT}:${PORT} \
                        ${IMAGE_NAME}:latest
                """
            }
        }
    }

    post {
        success {
            echo "部署成功：${IMAGE_NAME}:${BUILD_NUMBER}"
        }
        failure {
            echo "流水线失败，请检查日志"
        }
    }
}