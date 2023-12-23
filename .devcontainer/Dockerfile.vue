# Use an official Node.js runtime as a parent image
FROM node:14-alpine

# Set environment variables
ENV NODE_ENV development

# Set work directory
WORKDIR /usr/src/4skl.com/4skl

# Install Node.js dependencies
COPY ../4skl/package*.json ./
RUN npm ci

# Copy project
# Don't copy project https://stackoverflow.com/questions/74680419/dockerized-sveltkit-app-hot-reload-not-working
# COPY ../4skl/ .
# Copy project files
COPY ../4skl/src ./src
COPY ../4skl/public ./public
COPY ../4skl/vite.config.ts ./vite.config.ts
COPY ../4skl/tsconfig.json ./tsconfig.json
COPY ../4skl/tsconfig.app.json ./tsconfig.app.json
COPY ../4skl/tsconfig.node.json ./tsconfig.node.json
COPY ../4skl/.env.development ./.env.development
COPY ../4skl/env.d.ts ./env.d.ts
COPY ../4skl/index.html ./index.html

# Expose the Vue.js development server port and HMR port
EXPOSE 3000

# Use polling as it's run in wsl2
ENV USE_POLLING=true

# Run the Vue.js development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]