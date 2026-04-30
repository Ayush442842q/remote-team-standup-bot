# Remote Team Standup Bot Backend
## Project Description
The Remote Team Standup Bot Backend is a RESTful API designed to manage teams and their related data. It provides endpoints for creating, reading, and updating teams, and is secured using JWT Bearer token authentication.

## Tech Stack Used
* Programming Language: Node.js
* Framework: Express.js
* Database: PostgreSQL
* Authentication: JSON Web Tokens (JWT)

## Setup Instructions
To set up the Remote Team Standup Bot Backend, follow these steps:
1. **Clone the Repository**: Clone the repository using `git clone https://github.com/your-username/remote-team-standup-bot-backend.git`
2. **Install Dependencies**: Install the dependencies using `npm install` or `yarn install`
3. **Create a Database**: Create a PostgreSQL database and update the `database.js` file with your database credentials
4. **Generate JWT Secret Key**: Generate a secret key for JWT authentication using `openssl rand -base64 32`
5. **Start the Server**: Start the server using `npm start` or `yarn start`

## Environment Variables Needed
The following environment variables are required:
* **JWT_SECRET_KEY**: The secret key for JWT authentication
* **DATABASE_HOST**: The host URL of the PostgreSQL database
* **DATABASE_PORT**: The port number of the PostgreSQL database
* **DATABASE_USERNAME**: The username for the PostgreSQL database
* **DATABASE_PASSWORD**: The password for the PostgreSQL database
* **DATABASE_NAME**: The name of the PostgreSQL database

## API Endpoints Overview
The Remote Team Standup Bot Backend provides the following API endpoints:
* **POST /api/v1/teams**: Create a new team
* **GET /api/v1/teams/{team_id}**: Get a team by ID
* **PUT /api/v1/teams/{team_id}**: Update a team

## How to Run Locally
To run the Remote Team Standup Bot Backend locally, follow these steps:
1. **Start the Server**: Start the server using `npm start` or `yarn start`
2. **Use a Tool like Postman or cURL**: Use a tool like Postman or cURL to send requests to the API endpoints

## How to Run Tests
To run the tests, follow these steps:
1. **Install the Required Packages**: Install the required packages using `npm install` or `yarn install`
2. **Run the Tests**: Run the tests using `npm test` or `yarn test`

## API Documentation
For more information about the API endpoints, please refer to the [API Contract](https://github.com/your-username/remote-team-standup-bot-backend/blob/main/API-CONTRACT.md).

## Contribution Guidelines
To contribute to the Remote Team Standup Bot Backend, please follow these steps:
1. **Fork the Repository**: Fork the repository using `git fork https://github.com/your-username/remote-team-standup-bot-backend.git`
2. **Create a New Branch**: Create a new branch using `git branch feature/your-feature`
3. **Make Your Changes**: Make your changes and commit them using `git commit -m "Your commit message"`
4. **Create a Pull Request**: Create a pull request using `git pull-request`