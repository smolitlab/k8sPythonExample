docker build -t smolit-hello .

docker run -d --name example-app -p 8080:80 smolit-hello:latest

docker tag smolit-hello:latest smolit/smolit-hello:1.1
docker push smolit/smolit-hello:1.1