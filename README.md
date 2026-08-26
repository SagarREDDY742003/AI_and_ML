# 1. First explain the project

**Answer:**

> My project is **Cake Delight**, a cloud-native cake ordering application built using a **microservices architecture**.
>
> I have divided the application into six microservices:
>
> 1. User Service – registration and login
> 2. Catalog Service – cake information
> 3. Order Service – basket and orders
> 4. Notification Service – order notifications through RabbitMQ and Brevo
> 5. Rating Service – ratings and reviews
> 6. API Gateway – single entry point for the client
>
> I am using **MongoDB** for persistence, **RabbitMQ** for asynchronous communication, **Docker** for containerization, and **Kubernetes/Minikube** for deployment and orchestration.

---

# 2. Architecture of your project

Your architecture is essentially:

```text
                         Client / Postman
                                |
                                v
                       API Gateway :3030
                                |
          +---------------------+---------------------+
          |          |          |          |           |
          v          v          v          v           v
       User       Catalog     Order      Rating
       :3000       :3001      :3002      :3004
                              |
                              v
                         RabbitMQ :5672
                              |
                              v
                    Notification Service
                           :3003
                              |
                              v
                       Brevo Email API

       User/Catalog/Order/Rating
                |
                v
             MongoDB
              :27017
```

---

# 3. How many services have you used?

### Answer:

> I have **six application microservices**:
>
> * API Gateway
> * User Service
> * Catalog Service
> * Order Service
> * Notification Service
> * Rating Service
>
> In addition, I use two infrastructure components:
>
> * MongoDB
> * RabbitMQ
>
> So there are **8 runtime components** in the application environment.

In Docker Compose, you actually define **8 containers/services**.

---

# 4. What technologies are you using?

### Answer:

> I am using:
>
> * **Node.js** for backend services
> * **Express.js** for REST APIs
> * **MongoDB** as the database
> * **Mongoose** for MongoDB interaction
> * **JWT** for authentication
> * **bcryptjs** for password hashing
> * **RabbitMQ** for asynchronous messaging
> * **Docker** for containerization
> * **Docker Compose** for local multi-container execution
> * **Kubernetes with Minikube** for orchestration
> * **Brevo HTTPS API** for email notifications
> * **API Gateway** using `http-proxy-middleware`
> * **Git** for source-code version control.

---

# 5. Why did you use microservices instead of monolith?

### Answer:

> I used microservices because the application has different business responsibilities such as users, catalog, orders, ratings and notifications.
>
> In a monolithic application, all these functionalities would be inside one application. In my project, each functionality is independently deployed as a service.
>
> This gives me:
>
> * Independent deployment
> * Independent scaling
> * Better separation of responsibilities
> * Easier maintenance
> * Failure isolation
> * Different services can communicate independently
>
> For example, if the Notification Service has a problem, the Catalog Service does not need to be stopped.

### If interviewer asks: "Why not monolith?"

Say:

> A monolith would be simpler for a small application, but my objective was to demonstrate a **cloud-native microservices architecture**, including API Gateway, Docker, Kubernetes, RabbitMQ and independent services.

---

# 6. What is the API Gateway and why did you use it?

### Answer:

> API Gateway is the **single entry point** for client requests.
>
> Instead of the client directly communicating with every microservice, the client communicates with the API Gateway on port **3030**.
>
> The Gateway forwards the request to the appropriate service.

For example:

```text
GET /api/cakes
       |
       v
API Gateway :3030
       |
       v
Catalog Service :3001
```

Your code is in:

```text
api-gateway/src/app.js
```

For example:

```text
/api/users   → User Service
/api/cakes   → Catalog Service
/api/baskets → Order Service
/api/orders  → Order Service
/api/ratings → Rating Service
```

---

# 7. What does `5003:5003` mean?

### Answer:

> The first number is the **host port** and the second number is the **container port**.
>
> So `5003:5003` means:
>
> ```text
> Host machine → 5003
> Container    → 5003
> ```
>
> When I access `localhost:5003`, Docker forwards that request to port `5003` inside the container.

---

# 8. Difference between host and container

### Answer:

> The **host** is my actual operating system, for example my Windows machine.
>
> A **container** is an isolated runtime environment created by Docker inside the Docker environment.
>
> The container has its own filesystem, processes, network namespace and application environment.

---

# 9. Are host and container the same?

### Answer:

> No. They are different environments.
>
> The host is the physical or virtual machine running Docker.
>
> The container is an isolated environment running the application.
>
> Docker provides networking so the host can communicate with the container through published ports.

---

# 10. What is your endpoint port?

There are two situations.

### Docker Compose

The main external endpoint is:

```text
http://localhost:3030
```

So the API Gateway endpoint port is:

```text
3030
```

### Kubernetes / Minikube

Your Kubernetes API Gateway has:

```yaml
port: 3030
targetPort: 3030
nodePort: 30300
```

Therefore:

```text
Client
  |
  v
Minikube NodePort :30300
  |
  v
Kubernetes Service :3030
  |
  v
API Gateway container :3030
```

So when using your Kubernetes deployment, the **external endpoint port is 30300**.

Your README specifically uses:

```text
minikube service api-gateway -n cakedelight --url
```

---

# 11. Where are all the port configurations written?

### Answer:

There are two main places.

### Docker Compose

File:

```text
docker-compose.yml
```

Example:

```yaml
api-gateway:
  ports:
    - "3030:3030"
```

### Kubernetes

Files inside:

```text
k8s/
```

For example:

```text
k8s/api-gateway.yaml
k8s/user-service.yaml
k8s/catalog-service.yaml
k8s/order-service.yaml
k8s/notification-service.yaml
k8s/rating-service.yaml
k8s/mongodb.yaml
k8s/rabbitmq.yaml
```

The actual Node.js application port is also defined through:

```text
.env
```

or Kubernetes environment variables.

---

# 12. Why do you need both `EXPOSE` and `ports`?

Your Dockerfile has:

```dockerfile
EXPOSE 3030
```

while Docker Compose has:

```yaml
ports:
  - "3030:3030"
```

### Answer:

> `EXPOSE` documents the port that the application listens on inside the container.
>
> `ports` actually publishes/maps the container port to the host.
>
> `EXPOSE` by itself does not make the service accessible from the host.

---

# 13. Which service is used for placing the order?

### Answer:

> The **Order Service** is responsible for placing the order.

The endpoint is:

```text
POST /api/orders/checkout
```

---

# 14. Explain the order flow

### Answer:

> First, the user logs in and receives a JWT.
>
> The user adds cakes to the basket.
>
> When the user performs checkout, the Order Service:
>
> 1. Gets the user ID from the JWT.
> 2. Finds the user's basket in MongoDB.
> 3. Checks that the basket is not empty.
> 4. Validates the shipping address.
> 5. Creates an Order document.
> 6. Clears the basket.
> 7. Publishes an order event to RabbitMQ.
> 8. Notification Service consumes that event.
> 9. Notification Service sends an email through Brevo.

---

# 15. Where are you adding an item to the basket?

Your endpoint is:

```text
PUT /api/baskets/:basketId
```

The route is in:

```text
order-service/src/routes/basketRoutes.js
```

It calls:

```text
addItemToBasket()
```

from:

```text
order-service/src/controllers/basketController.js
```

which calls:

```text
basketService.addItemToBasket()
```

inside:

```text
order-service/src/services/basketService.js
```

---

# 16. Where are the items actually stored?

### Answer:

> Basket items are stored in MongoDB through the Order Service.

The model is:

```text
order-service/src/models/basket.js
```

The basket contains:

```text
customerId
customerName
customerEmail
items
totalAmount
```

Each item contains:

```text
cakeId
cakeName
price
quantity
subTotal
```

The MongoDB database is:

```text
orderdb
```

when using your Docker Compose configuration.

---


# 17. When you open Catalog, where do cake images, prices and details come from?

### Answer:

> They come from the **Catalog Service**, which retrieves cake documents from MongoDB.

The flow is:

```text
GET /api/cakes
       ↓
API Gateway
       ↓
Catalog Service
       ↓
MongoDB catalogdb
       ↓
Cake documents
       ↓
API response
```

The MongoDB model is:

```text
catalog-service/src/models/cake.js
```

The fields include:

```text
name
description
category
price
available
imageUrl
```

So the image itself is represented by the stored:

```text
imageUrl
```

The project does not store image files inside MongoDB.

---

# 18. Are you using MongoDB?

### Answer:

> Yes. I am using MongoDB with Mongoose.
>
> I use MongoDB for multiple service-specific databases.

Your configuration includes:

```text
usersdb
catalogdb
orderdb
ratingsdb
```

This follows the idea that each service owns its own data.

---

# 19. Why multiple MongoDB databases?

### Answer:

> Because each microservice should own its own data.
>
> User Service uses `usersdb`.
>
> Catalog Service uses `catalogdb`.
>
> Order Service uses `orderdb`.
>
> Rating Service uses its rating database.
>
> This prevents all services from becoming tightly coupled to one common database schema.

---

# 20. How are you creating the database?

### Answer:

> I don't manually create the MongoDB databases using a separate SQL-style `CREATE DATABASE` command.
>
> Mongoose connects using a MongoDB URI such as:
>
> ```text
> mongodb://mongodb:27017/catalogdb
> ```
>
> MongoDB creates the database/collections when data is actually written.

For example:

```text
mongodb://mongodb:27017/catalogdb
                         ↑
                    database name
```

When a cake is inserted, MongoDB creates the required database/collection structure.

---

# 21. Where is MongoDB running?

```text
k8s/mongodb.yaml
```

MongoDB runs as a Kubernetes Pod controlled by a Deployment.

It also uses:

```text
mongodb-pvc
```

for persistent storage.

---

# 22. Is the MongoDB data on your local machine or inside Docker?

### Answer:

> When I run MongoDB through Docker Compose, the MongoDB server is running inside the MongoDB container.
>
> The actual database data is stored in the Docker named volume:
>
> ```text
> mongodb_data
> ```
>
> which is mounted to:
>
> ```text
> /data/db
> ```
>
> On the host machine, I can access MongoDB through:
>
> ```text
> localhost:27017
> ```
>
> because Docker maps:
>
> ```text
> 27017:27017
> ```
>
> So seeing the database in MongoDB Compass on my local machine does **not mean MongoDB itself is running directly on Windows**. My local MongoDB client is connecting to the MongoDB container through the published port.

---

# 23. How can local MongoDB Compass see the container's data?

Suppose Docker has:

```yaml
ports:
  - "27017:27017"
```

Then:

```text
MongoDB Compass
      |
      | localhost:27017
      v
Windows Host Port 27017
      |
      | Docker port mapping
      v
MongoDB Container Port 27017
      |
      v
/data/db
      |
      v
Docker Volume mongodb_data
```

Therefore Compass can display the same data stored by the container.

---

# 24. Where have you written the message broker code?

### Answer:
The message broker is **RabbitMQ**.
The publisher code is here:
```text
order-service/src/services/rabbitMQService.js
```
The consumer code is here:
```text
notification-service/src/services/rabbitMQService.js
```
RabbitMQ itself is configured in:
```text
docker-compose.yml
```
and:
```text
k8s/rabbitmq.yaml
```
---

# 25. Where is RabbitMQ publishing the message?

The Order Service publishes the message to:

```text
orderQueue
```

The code is:

```text
order-service/src/services/rabbitMQService.js
```

It uses:

```javascript
channel.sendToQueue(
    queue,
    messageBuffer,
    {
        persistent: true
    }
);
```

where:

```text
queue = "orderQueue"
```

---

# 26. Where is RabbitMQ consuming the message?

The Notification Service consumes it.

File:

```text
notification-service/src/services/rabbitMQService.js
```

It uses:

```javascript
channel.consume(queue, ...)
```

The same queue is:

```text
orderQueue
```

So:

```text
Order Service
     |
     | publish
     v
RabbitMQ
 orderQueue
     |
     | consume
     v
Notification Service
```

---

# 27. Why are you using RabbitMQ and Why is RabbitMQ called a message broker?

### Answer:
> RabbitMQ acts as an intermediary between producers and consumers.
>
> I use RabbitMQ for asynchronous communication between the Order Service and Notification Service.
>
> The Order Service should not have to directly wait for the email notification to complete.
>
> Instead, it publishes an order event to RabbitMQ.
>
> Notification Service consumes the event independently and sends the email.

This provides **loose coupling** between Order and Notification services.

---

# 28. Why not directly call Notification Service?

### Answer:

> Direct HTTP communication would tightly couple the Order Service to the Notification Service.
>
> With RabbitMQ, Order Service only publishes an event. Notification Service independently consumes it.
>
> If the Notification Service is temporarily unavailable, RabbitMQ can hold the message until the consumer processes it, depending on the queue configuration.

---

# 29. What events are you publishing?

Your code supports:

```text
ORDER_PLACED
ORDER_PROCESSING
ORDER_SHIPPED
ORDER_DELIVERED
ORDER_CANCELLED
```

The notification service receives:

```text
type
order
message
```

---

# 30. Where does the email notification happen?

### Answer:

The Notification Service receives the RabbitMQ event.

Then:

```text
notification-service/src/services/notificationService.js
```

calls:

```text
emailService.js
```

Your current code sends the email using the **Brevo HTTPS transactional email API**.

It calls:

```text
https://api.brevo.com/v3/smtp/email
```

---

# 31. What is your message flow?

A very good answer is:

```text
Customer
   |
   | Checkout
   v
API Gateway
   |
   v
Order Service
   |
   | Save order
   v
MongoDB
   |
   | Publish event
   v
RabbitMQ
   |
   | Consume event
   v
Notification Service
   |
   v
Brevo
   |
   v
Customer Email
```

---

# 32. Why did you use Kubernetes?

### Answer:

> I used Kubernetes to orchestrate my Docker containers.
>
> Kubernetes manages:
>
> * Deployments
> * Pods
> * Services
> * Networking
> * Service discovery
> * Restarting failed containers
> * Scaling
> * Configuration
> * Persistent storage
>
> Instead of manually starting every container, Kubernetes manages the complete application.

---

# 33. Why Minikube?

### Answer:

> Minikube provides a local Kubernetes cluster for development and demonstration.
>
> Instead of requiring a cloud Kubernetes cluster such as AWS EKS or Azure AKS, I can run Kubernetes locally using Minikube.

Your README specifically uses:

```text
Minikube + Docker driver
```

---

# 34. What is a container?

### Answer:

> A container is a lightweight, isolated environment used to package and run an application along with its dependencies.
>
> In my project, each microservice is packaged into its own Docker image and runs inside its own container.

For example:

```text
cakedelight-user-service
        ↓
User Service Container
```

---

# 35. What is the role of containers in your project?

### Answer:

> Containers provide a consistent runtime environment for each microservice.
>
> For example, instead of installing Node.js and dependencies separately for every service on my host machine, I create Docker images containing the required Node.js runtime, application code and dependencies.
>
> This makes the application portable and easier to deploy.

---

# 36. Difference between Docker and Kubernetes

### Answer:

> **Docker** is primarily used to build and run containers.
>
> **Kubernetes** is used to orchestrate and manage containers.
>
> Docker answers:
>
> **"How do I package and run this application?"**
>
> Kubernetes answers:
>
> **"How do I manage many application containers reliably?"**

Example:

```text
Docker
  ↓
Build Image
  ↓
Run Container

Kubernetes
  ↓
Manage Pods
  ↓
Manage Services
  ↓
Restart
  ↓
Scale
  ↓
Networking
```

---

# 37. Difference between VM and container

### Answer:

| Virtual Machine            | Container                          |
| -------------------------- | ---------------------------------- |
| Contains complete guest OS | Shares host OS kernel              |
| Heavier                    | Lightweight                        |
| Slower startup             | Fast startup                       |
| More resource usage        | Less resource usage                |
| Strong OS-level isolation  | Process-level isolation            |
| VM image is larger         | Container image is usually smaller |

---

# 38. What is a Docker image?

### Answer:

> A Docker image is a packaged, read-only template used to create containers.
>
> In my project, each microservice has a Dockerfile that defines how its image is built.

For example:

```text
user-service/Dockerfile
```

creates:

```text
cakedelight-user-service:latest
```

---

# 39. How many Docker images have you created?

Your project has **6 custom application Dockerfiles**:

```text
user-service/Dockerfile
catalog-service/Dockerfile
order-service/Dockerfile
notification-service/Dockerfile
rating-service/Dockerfile
api-gateway/Dockerfile
```

So you have:

> **6 custom Docker images.**

In addition, the deployment uses two external/base images:

```text
mongo:8
rabbitmq:3-management
```

Therefore the application environment uses **8 image types in total**.

---

# 40. How many containers have you created?

With Docker Compose, your file defines:

```text
1. mongodb
2. rabbitmq
3. user-service
4. catalog-service
5. order-service
6. notification-service
7. rating-service
8. api-gateway
```

Therefore:

> Docker Compose creates **8 application containers**.

For Kubernetes, you have eight application workloads/Pods as well.

---

# 41. What command shows all running containers?

### Answer:

```bash
docker ps
```

For all containers, including stopped containers:

```bash
docker ps -a
```

---

# 42. What command shows Docker images?

```bash
docker images
```

or:

```bash
docker image ls
```

---

# 43. How do you see Kubernetes Pods?

```bash
kubectl get pods -n cakedelight
```

Services:

```bash
kubectl get svc -n cakedelight
```

Deployments:

```bash
kubectl get deployments -n cakedelight
```
Logs:

```bash
kubectl logs <pod-name> -n cakedelight
```

---

# 44. Are Docker images rebuilt automatically when you edit code?

### Answer:

> No.
>
> If I edit my source code, the existing Docker image does not automatically change.
>
> The image contains the code that existed at the time the image was built.
>
> Therefore I need to rebuild the image.

For Docker Compose:

```bash
docker compose up --build
```

or:

```bash
docker build -t cakedelight-user-service:latest ./user-service
```

---

# 45. What about Kubernetes after editing code?

Your Kubernetes manifests use:

```yaml
imagePullPolicy: IfNotPresent
```

and:

```text
cakedelight-user-service:latest
```

Since you're using Minikube's Docker environment, you would typically:

```bash
eval $(minikube docker-env)

docker build -t cakedelight-user-service:latest ./user-service
```

Then restart the Deployment:

```bash
kubectl rollout restart deployment/user-service -n cakedelight
```

---

# 46. What is `.gitignore`?

### Answer:

> `.gitignore` tells Git which files or directories should not be tracked or committed.

Examples include:

```text
node_modules/
.env
logs/
temporary files
```

This is especially important for my project because `.env` files may contain credentials and secrets.

---


# 47. What is `.dockerignore`?

### Answer:

> `.dockerignore` tells Docker which files should not be copied into the Docker build context.

Your project has entries such as:

```text
node_modules
.env
.git
.gitignore
README.md
```

This reduces image size and avoids copying unnecessary or sensitive files.

---

# 48. What is the difference between `.gitignore` and `.dockerignore`?

### Answer:

> `.gitignore` is for Git.
>
> `.dockerignore` is for Docker.

```text
.gitignore
    ↓
Controls what Git tracks

.dockerignore
    ↓
Controls what Docker sends into build context
```

---

# 49. Where is the data stored?

### Answer:

Catalog Service uses:

```text
MongoDB
    |
    └── catalogdb
```

```text
Order Service
      ↓
MongoDB
      ↓
orderdb
      ↓
Basket collection
```

```text
Order Service
      ↓
MongoDB
      ↓
orderdb
      ↓
Order collection
```

```text
User Service
     ↓
MongoDB
     ↓
usersdb
```

---

# 50. How does authentication work?

### Answer:

> When a user logs in, User Service verifies the credentials and generates a JWT.
>
> The client sends that JWT in the Authorization header:
>
> ```text
> Authorization: Bearer <token>
> ```
>
> Protected services verify the JWT using the same secret key.
>
> The decoded JWT contains:
>
> ```text
> userId
> username
> email
> ```
>
> The Order Service uses the `userId` to identify the user's basket.

Flow:

```text
Login
 ↓
User Service
 ↓
JWT
 ↓
Client
 ↓
Authorization: Bearer JWT
 ↓
Order Service
 ↓
JWT verification
 ↓
req.user
```

---

# 51. Where is JWT verification written?

For Order Service:

```text
order-service/src/middleware/authMiddleware.js
```

It extracts:

```text
Authorization: Bearer <token>
```

and verifies it using:

```javascript
jwt.verify(token, process.env.SECRET_KEY)
```

---

# 52. Why is API Gateway useful with Kubernetes?

### Answer:

> The Gateway hides the internal service addresses from the client.
>
> Internally Kubernetes uses service names such as:
>
> ```text
> user-service:3000
> catalog-service:3001
> order-service:3002
> rating-service:3004
> ```
>
> The client only needs the API Gateway endpoint.

---

# 53. Are your internal Kubernetes services exposed to the outside?

### Answer:

> No. Most of my internal services use Kubernetes `ClusterIP`.
>
> For example:
>
> ```text
> user-service → ClusterIP
> catalog-service → ClusterIP
> order-service → ClusterIP
> rating-service → ClusterIP
> notification-service → ClusterIP
> ```
>
> Only the API Gateway is exposed externally using a `NodePort`.

Your API Gateway:

```yaml
type: NodePort
nodePort: 30300
```

---

# 54. Why use ClusterIP?

### Answer:

> ClusterIP is used for internal Kubernetes communication.
>
> It allows services inside the cluster to communicate without exposing every microservice to the outside world.

For example:

```text
API Gateway
     |
     v
catalog-service:3001
```

The client doesn't directly need access to `catalog-service`.

---

# 56. What is the difference between `port`, `targetPort`, and `nodePort`?

```yaml
ports:
  - port: 3030
    targetPort: 3030
    nodePort: 30300
```

```text
nodePort
   ↓
External access

port
   ↓
Kubernetes Service port

targetPort
   ↓
Container/application port
```

So:

```text
Client
 ↓
30300
 ↓
Kubernetes Service :3030
 ↓
Pod :3030
```

---

# 57. What is RabbitMQ's port?

```text
5672  → AMQP Application messaging
15672 → RabbitMQ management UI
```

---


# 58. What happens if Notification Service is down?

### Answer:

> The Order Service can publish the event to RabbitMQ without directly depending on Notification Service.
>
> RabbitMQ can retain the message in the queue depending on queue/message durability, and the Notification Service can consume it when it becomes available.

Your message is sent as:

```javascript
persistent: true
```

and the queue is asserted as:

```javascript
durable: true
```

So the design supports message persistence.

---

# 59. Why do you clear the basket after checkout?

### Answer:

> After successfully creating the Order, I clear the basket because the items have been converted into an actual order.
>
> The Order contains its own copy of the items, prices, quantities and total amount.
>
> Therefore the basket can be reused for the next order.

---

# 60. Why do you copy basket items into the Order?

### Answer:

> Because an order should preserve the purchase information at the time of checkout.
>
> If the cake price changes later in the Catalog Service, the previous order should still contain the original price.
>
> Therefore the Order Service stores its own snapshot of the basket items.

---

# 61. How does adding a cake work internally?

Example:

```text
PUT /api/baskets/123
```

with:

```json
{
  "cakeId": "abc",
  "cakeName": "Black Forest",
  "price": 699,
  "quantity": 2
}
```

Order Service:

```text
Find Basket
    ↓
Check whether cake already exists
    ↓
If exists → increase quantity
    ↓
Otherwise → push new item
    ↓
Calculate subtotal
    ↓
Calculate totalAmount
    ↓
Save Basket
    ↓
Return updated Basket
```

---

# 62. What happens when you update quantity?

Endpoint:

```text
PUT /api/baskets/:basketId/items/:cakeId
```

The service:

```text
Find basket
 ↓
Find cake
 ↓
Validate quantity
 ↓
Update quantity
 ↓
Calculate subtotal
 ↓
Recalculate basket total
 ↓
Save MongoDB
```

---

# 63. What happens when you remove an item?

Endpoint:

```text
DELETE /api/baskets/:basketId/items/:cakeId
```

The Order Service removes that item from the basket and recalculates:

```text
totalAmount
```

Then it saves the basket in MongoDB.

---


# 64. How do you run the project?

For Docker Compose:

```bash
docker compose up --build
```

For Kubernetes:

```bash
minikube start
```

Then:

```bash
eval $(minikube docker-env)
```

Build the six images:

```bash
docker build -t cakedelight-user-service:latest ./user-service
docker build -t cakedelight-catalog-service:latest ./catalog-service
docker build -t cakedelight-order-service:latest ./order-service
docker build -t cakedelight-rating-service:latest ./rating-service
docker build -t cakedelight-notification-service:latest ./notification-service
docker build -t cakedelight-api-gateway:latest ./api-gateway
```

Then:

```bash
kubectl apply -f k8s/
```

Check:

```bash
kubectl get pods -n cakedelight
```

Then get the external URL:

```bash
minikube service api-gateway -n cakedelight --url
```

---

# 1. What is the role of each service in the project?

Your project has **six microservices**.

| Service                  | Role                                                                 | Port |
| ------------------------ | -------------------------------------------------------------------- | ---: |
| **API Gateway**          | Single entry point; routes client requests to microservices          | 3030 |
| **User Service**         | User registration, login and authentication                          | 3000 |
| **Catalog Service**      | Manages cake information such as name, price, category and image URL | 3001 |
| **Order Service**        | Manages baskets, checkout and orders                                 | 3002 |
| **Notification Service** | Consumes order events and sends email notifications                  | 3003 |
| **Rating Service**       | Manages cake ratings/reviews                                         | 3004 |

Infrastructure components:

| Component    | Role                                                                |
| ------------ | ------------------------------------------------------------------- |
| **MongoDB**  | Stores application data                                             |
| **RabbitMQ** | Asynchronous message broker between Order and Notification services |

---

# 2. What is the difference between the root-level Dockerfile and `docker-compose.yml`?

> **A Dockerfile defines how Docker built image for an individual service , whereas `docker-compose.yml` defines how multiple containers and infrastructure components are configured and run together.**

---

# 3. Why do we have separate Dockerfiles for each microservice?

> **I use separate Dockerfiles because each microservice is independently deployable. Each Dockerfile creates a separate image containing the code and dependencies required by that particular service.**

---

# 4. What resources are defined in the Kubernetes YAML file?

Deployment and Service.

---

# 5. How many actual container replicas are running?

Your Deployments use:

```yaml
replicas: 1
```

for the application services.

Therefore, if everything is healthy, you have:

```text
API Gateway        → 1 Pod
User Service       → 1 Pod
Catalog Service    → 1 Pod
Order Service      → 1 Pod
Notification       → 1 Pod
Rating Service     → 1 Pod
```

So your six application services have:

> **6 application replicas.**

Plus your MongoDB and RabbitMQ workloads, assuming each is running one Pod, gives approximately:

> **8 running application/infrastructure Pods.**

---

# 6. What is a replica in Kubernetes?

> **A replica is a copy of a Pod maintained by a Kubernetes controller such as a Deployment. Replicas provide availability and allow an application to be scaled horizontally.**

---

# 7. Who manages the replicas?

> **The Deployment manages the desired replica count. Internally, Kubernetes uses a ReplicaSet to maintain the required number of Pods.**

---

# 8. Why did you use Kubernetes in this project?

### Answer:

> **I used Kubernetes because my application consists of multiple containerized microservices. Kubernetes provides orchestration for these containers. It manages Pods, deployments, networking, service discovery, scaling and recovery when a Pod fails.**

For your project:

```text
Docker
   ↓
Creates/runs containers

Kubernetes
   ↓
Manages those containers at application level
```

---

# 9. What is the difference between Pod, Deployment and Service?

> **Pod = runs the application**
> **Deployment = manages the Pods**
> **Service = provides network access to the Pods**

---

# 11. What is the difference between Docker image and Docker container?

A Docker image is a **read-only template/package** used to create containers.

A container is a **running instance of that image**.

---

# 12. Give any two Docker commands.

### Display running containers

```cmd
docker ps
```

### Display Docker images

```cmd
docker images
```

Other useful commands:

```cmd
docker build -t myimage .
```

Builds an image.

```cmd
docker run myimage
```

Creates and starts a container.

```cmd
docker logs <container-name>
```

Displays container logs.

```cmd
docker stop <container-name>
```

Stops a container.

---

# 13. What are the advantages of using Kubernetes in this project?

You can give several points.

### 1. Container orchestration

Kubernetes manages all your microservice Pods.

### 2. Self-healing

If a Pod crashes, Kubernetes can create a replacement.

### 3. Scaling

You can change:

```yaml
replicas: 1
```

to:

```yaml
replicas: 3
```

and Kubernetes creates three Pods.

### 4. Service discovery

Your API Gateway can communicate using:

```text
http://user-service:3000
```

rather than hardcoded Pod IP addresses.

### 5. Load distribution

If you have multiple replicas, a Kubernetes Service can distribute requests across them.

### 6. Resource management

Your YAML specifies:

```yaml
requests:
  cpu: "100m"
  memory: "128Mi"

limits:
  cpu: "500m"
  memory: "512Mi"
```

Kubernetes can use these values for scheduling and resource control.

### 7. Persistent storage

Your MongoDB deployment uses persistent storage so database data isn't dependent solely on the lifetime of a Pod.

---

# 14. What is a Microservice?

### Simple answer

> A microservice is a small, independently deployable application that is responsible for one specific business functionality.

Each service has its own:

* Code
* API endpoints
* Dockerfile
* Docker image
* Configuration
* Responsibility

---

# 15. How can you see Docker container health?

There are several commands, depending on what they mean by "health."

## See running containers

```cmd
docker ps
```

This shows:

```text
CONTAINER ID
IMAGE
STATUS
PORTS
NAMES
```

For example:

```text
STATUS
Up 5 minutes
```

means the container is running.

---

## See detailed container status

```cmd
docker inspect <container-name>
```

For example:

```cmd
docker inspect api-gateway
```

### For Docker Compose

You can also use:

```cmd
docker compose ps
```

---

## Kubernetes health

Since your project is also deployed using Kubernetes, use:

```cmd
kubectl get pods -n cakedelight
```

You'll see:

```text
NAME                         READY   STATUS
api-gateway-xxxxx            1/1     Running
user-service-xxxxx           1/1     Running
catalog-service-xxxxx        1/1     Running
```

Here:

```text
1/1
```
means one container is ready out of one container in that Pod.

---

# 16. How exactly does REST API work?

REST API is a way for applications/services to communicate using HTTP.

Your project uses REST APIs between the client/API Gateway and your microservices.

The basic flow is:

```text
Client
   |
   | HTTP Request
   ↓
API Gateway
   |
   | HTTP Request
   ↓
Microservice
   |
   ↓
MongoDB
   |
   ↓
HTTP Response
   |
   ↓
Client
```

---

# 17. What are HTTP methods?

You should know these:

| Method   | Purpose       | Example in your project |
| -------- | ------------- | ----------------------- |
| `GET`    | Retrieve data | Get cakes               |
| `POST`   | Create data   | Create order/login      |
| `PUT`    | Update data   | Update basket           |
| `DELETE` | Delete data   | Remove basket item      |

---

# 18. What is an API?

API means:

> **Application Programming Interface**

It provides a defined way for one application to communicate with another.

For example:

```text
API Gateway
     |
     | GET /api/cakes
     ↓
Catalog Service
```

The API defines things like:

```text
HTTP Method
URL
Request
Response
Status Code
```

---

# 19. What is REST?

REST stands for:

> **Representational State Transfer**

REST is an architectural style for designing APIs around resources.

In your project:

```text
/cakes
/users
/baskets
/orders
/ratings
```

are resources.

---

# 20. Why RabbitMQ instead of direct REST communication?

> **I used RabbitMQ because notification is an asynchronous operation. The Order Service publishes an event and doesn't need to directly call the Notification Service. The Notification Service independently consumes the event and processes the notification.**

---

# 22. Why did you use Node.js instead of Spring Boot?

### Viva answer

> **I chose Node.js because this project is based on lightweight microservices and REST APIs. Node.js with Express is lightweight, has good support for asynchronous and I/O-intensive operations, and allows me to build REST APIs quickly using JavaScript. It also integrates easily with MongoDB, RabbitMQ and Docker.**

### If they ask "Is Spring Boot better?"

Don't say Node.js is better.

Say:

> **Neither is universally better. Spring Boot is very strong for enterprise Java applications, while Node.js is lightweight and well suited for I/O-heavy REST and microservice applications. I selected Node.js based on the requirements and simplicity of this project.**

---

# 23. What is Node.js?

> **Node.js is a JavaScript runtime that allows JavaScript to run outside the browser, particularly on the server side. It uses an event-driven, non-blocking I/O model, which makes it suitable for APIs and I/O-intensive applications.**

---

# 24. What is Express.js?

> **Express.js is a lightweight web framework built on top of Node.js. I use it to create REST APIs, define routes, use middleware, handle HTTP requests and responses, and start my microservice servers.**

---

# 25. Node.js vs Express.js

> **Node.js is the runtime environment, while Express.js is a web framework running on Node.js that simplifies API and HTTP server development.**

---

# 26. What is MongoDB?

> **MongoDB is a NoSQL, document-oriented database. Instead of storing data primarily in rows and columns like a relational database, it stores documents in BSON format inside collections.**

---

# 27. What is Mongoose?

> **Mongoose is an ODM — Object Data Modeling library — for MongoDB and Node.js. It provides schemas, models, validation and convenient methods for interacting with MongoDB.**

---

# 28. Why use Mongoose if we can directly work with MongoDB?

> **MongoDB is the actual database, while Mongoose is a library that provides an easier and structured way for my Node.js application to interact with MongoDB. I use Mongoose for schemas, models, validation and database operations.**

---

# 29. What are middleware and Why do we use middleware?

> **Middleware is a function that executes during the request-response cycle before the final route handler or response is completed.**

Middleware can be used for:

* Request parsing
* Authentication
* Logging
* CORS
* Error handling
* Validation
* Authorization

---

# 30. What is CORS?

CORS stands for:

> **Cross-Origin Resource Sharing**

> **CORS is a browser security mechanism that controls cross-origin HTTP requests. I use the Express CORS middleware so that the frontend can communicate with my backend APIs when they are running on different origins.**

---

# 31. What is Docker Compose?

> **Docker Compose is a tool for defining and running multiple related containers using a YAML configuration file, usually `docker-compose.yml`.**

Your project can define:

```text
API Gateway
User Service
Catalog Service
Order Service
Notification Service
Rating Service
MongoDB
RabbitMQ
```

in one Compose configuration.

Instead of starting everything separately:

```cmd
docker run ...
docker run ...
docker run ...
```

you can use:

```cmd
docker compose up
```

or:

```cmd
docker compose up --build
```

---

# 32. Why did you use microservices?

> **I used microservices to divide the application according to business responsibilities. This allows individual services to be developed, deployed, maintained and scaled independently. It also reduces the impact of changes or failures in one service on the entire application.**

---

# 33. Explain one REST API from your project step-by-step

Suppose the user opens the catalog.

### Step 1

Frontend sends:

```http
GET /api/cakes
```

### Step 2

Request reaches:

```text
API Gateway
```

### Step 3

Gateway forwards it to:

```text
catalog-service:3001
```

### Step 4

Catalog Service receives the request.

### Step 5

Catalog Service uses Mongoose:

```text
Catalog Service
      ↓
Mongoose
      ↓
MongoDB
```

### Step 6

MongoDB returns cake documents.

### Step 7

Catalog Service returns JSON.

### Step 8

Gateway returns the response to the client.

Complete flow:

```text
Client
 ↓
GET /api/cakes
 ↓
API Gateway
 ↓
Catalog Service
 ↓
Mongoose
 ↓
MongoDB
 ↓
Catalog Service
 ↓
API Gateway
 ↓
Client
```

---

# 34. Explain your Order + RabbitMQ flow

> **When an order is placed, Order Service stores the order and publishes an order event to RabbitMQ. Notification Service consumes the event asynchronously and sends the notification.**

---

# 35. Why MongoDB instead of MySQL?

If they ask this after MongoDB:

> **MongoDB's document-oriented model fits the flexible JSON-like data used by my Node.js microservices. It also integrates naturally with Node.js through Mongoose.**

You can add:

> **However, MySQL would also be a valid choice, especially where strong relational constraints and complex joins are important.**

---

# 36. Why Express instead of using Node.js directly?

> **Node.js provides the runtime, while Express simplifies the development of HTTP servers and REST APIs through routing and middleware.**

---

# 37. What are the stages of a Promise?

A Promise has **three states**:

### 1. Pending

The operation has started but hasn't completed.

### 2. Fulfilled

The asynchronous operation completed successfully.

### 3. Rejected

The operation failed.

### Viva answer

> **A Promise starts in the pending state and eventually becomes either fulfilled or rejected. We handle successful results using `then`, errors using `catch`, and cleanup using `finally`.**

---

# 38. How do you handle asynchronous operations in Node.js?

> **I handle asynchronous operations mainly using Promises and async/await. Database operations, REST API calls and other I/O operations are asynchronous, so Node.js doesn't need to block the entire application while waiting for them.**

---

# 39. Difference between Promise and async/await

This is a very common follow-up.

### Promise

A Promise represents the eventual result of an asynchronous operation.

```javascript
Cake.find()
  .then(cakes => {
      console.log(cakes);
  })
  .catch(error => {
      console.error(error);
  });
```

### async/await

`async/await` is syntax built on top of Promises that makes asynchronous code easier to read.

```javascript
async function getCakes() {
    try {
        const cakes = await Cake.find();
        return cakes;
    } catch (error) {
        console.error(error);
    }
}
```

---

# 40. What is `async`?

When you put:

```javascript
async function getCakes() {
}
```

the function always returns a Promise.

For example:

```javascript
async function test() {
    return "Hello";
}
```

is effectively returning a fulfilled Promise containing `"Hello"`.

---

# 41. What is `await`?

`await` waits for a Promise to settle **inside an async function**.

Example:

```javascript
const cakes = await Cake.find();
```

It means:

> Wait for the database operation's Promise to resolve before assigning the result to `cakes`.

Important:

> `await` does not mean Node.js blocks the entire server.

The asynchronous operation is handled by Node.js's event-driven architecture.

---

# 42. What are Node.js core modules?

| Module    | Purpose                          |
| --------- | -------------------------------- |
| `fs`      | File system operations           |
| `path`    | File/directory path handling     |
| `http`    | HTTP server/client functionality |
| `https`   | HTTPS functionality              |
| `os`      | Operating-system information     |
| `events`  | Event handling                   |
| `url`     | URL handling                     |
| `util`    | Utility functions                |
| `stream`  | Streaming data                   |
| `process` | Process/environment information  |

---

# 43. Does Docker handle orchestration?

> **Docker provides containerization, while Kubernetes provides container orchestration. Docker Compose can coordinate multiple containers for local development, but Kubernetes handles orchestration features such as replicas, self-healing, service discovery and scaling.**

---

# 44. Docker `create` vs Docker `build`

### `docker build`

Creates a Docker image from a Dockerfile.

```cmd
docker build -t cakedelight-api-gateway .
```

### `docker create`

Creates a **container from an existing image**, but does **not start it**.

```cmd
docker create --name mycontainer cakedelight-api-gateway:latest
```

To start it:

```cmd
docker start mycontainer
```

### Difference

| `docker build`                   | `docker create`                  |
| -------------------------------- | -------------------------------- |
| Creates an image                 | Creates a container              |
| Uses Dockerfile                  | Uses an existing image           |
| Image is not running             | Container is created but stopped |
| Example: `docker build -t app .` | Example: `docker create app`     |

---

# 46. What are the different types of middleware?

### 1. Application-level middleware

Applied to the entire Express application.

```javascript
app.use(express.json());
```

### 2. Route-level middleware

Applied to a specific route.

```javascript
app.get("/orders", authMiddleware, getOrders);
```

### 3. Built-in middleware

Provided by Express itself.

Examples:

```javascript
express.json()
express.urlencoded()
express.static()
```

---

### 4. Third-party middleware

Installed using npm.

Examples from common Express applications:

```javascript
cors()
```

and other packages such as logging middleware.

---

### 5. Error-handling middleware

Has four parameters:

```javascript
(err, req, res, next)
```

Example:

```javascript
app.use((err, req, res, next) => {
    res.status(500).json({
        message: err.message
    });
});
```

---

# 47. Give any two built-in Express middleware

> **Two built-in Express middleware functions are `express.json()` for parsing JSON request bodies and `express.static()` for serving static files.**

---

# 48. What is an `.env` file?

An `.env` file contains **environment-specific configuration values** as key-value pairs.

Example:

```text
PORT=3030
MONGO_URI=mongodb://...
RABBITMQ_URL=amqp://...
```

Your application accesses them using:

```javascript
process.env.PORT
```

---

# 49. Why do you use `.env` in your project?

The main reason is to keep **configuration separate from application code**.

For example, instead of hardcoding:

```javascript
const port = 3030;
```

you can use:

```javascript
const port = process.env.PORT;
```

---

# 50. How is `.env` used with Node.js?

Usually a package such as `dotenv` loads the variables.

For example:

```javascript
require("dotenv").config();
```

Then:

```javascript
const port = process.env.PORT;
```

---

# 51. Why should `.env` be in `.gitignore`?

Because it may contain sensitive configuration such as:

```text
DATABASE_URL=...
JWT_SECRET=...
API_KEY=...
PASSWORD=...
```

---

# 52. What is orchestration?

> **Container orchestration means automatically managing multiple containers, including deployment, networking, scaling, health/recovery and updates.**

---

# 53. if 100 microservices are there is there any requirement for 100 dockerfiles or any alternative?

No. **100 microservices do not necessarily require 100 Dockerfiles**, although having one Dockerfile per independently deployed service is a very common and clean approach.

### In your project
 you have six Dockerfiles:

```text
api-gateway/Dockerfile
user-service/Dockerfile
catalog-service/Dockerfile
order-service/Dockerfile
notification-service/Dockerfile
rating-service/Dockerfile
```

This makes sense because each service produces its own independently deployable image.

> **"For 100 microservices, I don't necessarily need 100 unique Dockerfiles. I need independently deployable container images. If the services use the same technology and build structure, I can standardize or share the Docker build process, use templates, Buildpacks, or CI/CD automation. In my Cake Delight project, I use separate Dockerfiles because each microservice is independently built and deployed, which keeps the architecture clear and maintainable."**

# 54. Don't change the code. Make the catalog empty and show me that no cakes are displayed.

> kubectl get pods -n cakedelight

> docker exec -it mongodb-container-name mongosh

> use your-database-name

> show collections

> db.cakes.find()

> db.cakes.deleteMany({})
