[![img](https://img.shields.io/badge/Lifecycle-Experimental-339999)](https://github.com/bcgov/repomountie/blob/master/doc/lifecycle-badges.md)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)

# DTS VC Tutorial

A framework used to showcase and explain Verifiable Credentials.

## Project Structure

The project is made of two components:

- a Django app that works as back-end/API as well as webserver

- a VueJS app for the frontend

The application provides a standard-structure framework for various scenarios, while keeping some of the content homogeneous across instances.

The configuration shared across all of the apps/scenarios is held by [global.yaml](docker/site/config/global.yaml): this acts as base and provides all of the shared content.

Each individual app will have a folder in the [config root](docker/site/config) that will act as context for a specific instance of the demo/tutorial app.
The folder name will correspond to the route that will be exposed to the web browser (e.g.: `/my-great-tutorial`) and it will include at least a `config.yaml` file specifying all of the dynamic content for the application instance. Specifying keys with the same name as the ones provided in the global configuration will override them.

To add a new instance all that is required is to add a new folder for the new route/context with the required configuration files, and the application will pick it up automatically.

A "catch-all" view at the root of the web application (without app-specific path) is also available and provides a listing of all the available scenarios configured in the running instance of the web application.
