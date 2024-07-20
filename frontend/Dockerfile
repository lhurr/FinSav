# Use an official Node runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and install dependencies
COPY package.json /app/
RUN npm install

COPY . /app/
# COPY ./src /app/src

EXPOSE 3001
CMD ["npm", "run", "dev"]