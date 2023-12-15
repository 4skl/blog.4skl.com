# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set environment variables
ENV NODE_ENV development

# Set work directory
WORKDIR /workspaces/4skl

# Install system dependencies
RUN apk add --no-cache make gcc g++ python3

# Install Node.js dependencies
COPY 4skl/package.json 4skl/package-lock.json* ./
RUN npm ci

# Copy project
COPY 4skl/ .

# Expose the Vue.js development server port
EXPOSE 8080

# Run the Vue.js development server
CMD ["npm", "run", "serve"]