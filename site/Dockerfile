FROM node:18.18.0-alpine
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm install --no-audit --legacy-peer-deps
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
