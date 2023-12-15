# Use an official Node.js runtime as a parent image
FROM node:14

# Set environment variables
ENV NODE_ENV development

# Set work directory
WORKDIR /usr/src/app

# Install Node.js dependencies
COPY ../4skl/package.json ../4skl/package-lock.json* ./
RUN npm ci

# Copy project
COPY ../4skl/ .

# Expose the Vue.js development server port
EXPOSE 3000

# Run the Vue.js development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]