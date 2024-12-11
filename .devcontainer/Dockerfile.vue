# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set environment variables
ENV NODE_ENV=development

# Set work directory
WORKDIR /usr/src/blog.4skl.com/4skl

# Install Node.js dependencies
COPY ../4skl/package*.json ./
RUN npm ci

# Expose the Vue.js development server port and HMR port
EXPOSE 3000 24678

# Run the Vue.js development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]