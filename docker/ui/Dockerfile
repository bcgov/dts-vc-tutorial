# build stage
FROM node:fermium as build-stage
WORKDIR /app
COPY ui/package*.json ./
RUN npm install
COPY ui/ .
RUN npm run build

# runtime stage
FROM vc-tutorial-site as runtime-stage
USER root
RUN mkdir -p /var/www/static/ui
COPY --from=build-stage /app/dist /var/www/static/ui
