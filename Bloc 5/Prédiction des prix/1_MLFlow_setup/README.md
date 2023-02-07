## Set up the MLFlow server on Heroku

1. Build your Docker image `docker buildx build --platform linux/amd64 -t YOUR_IMAGE_NAME .`
2. Log in Heroku `heroku login`
3. Create your application `heroku create YOUR_APP_NAME`
4. Install [Heroku Postgres](https://elements.heroku.com/addons/heroku-postgresql)
 et follow this [video](https://vimeo.com/661767872) to set up a Postgresql database for your application
5. Create a S3 bucket that will be used to store artifacts
6. Create `secrets.sh` file containing the environment variables
```
  export ARTIFACT_ROOT='YOUR_S3_BUCKET'
  export AWS_ACCESS_KEY_ID='YOUR_AWS_ACCESS_KEY_ID'
  export AWS_SECRET_ACCESS_KEY='YOUR_AWS_SECRET_ACCESS_KEY'
  export BACKEND_STORE_URI='YOUR_POSTGRESQL_DATABASE_URI'
  export MLFLOW_TRACKING_URI='YOUR_HEROKU_APP_URI'
 ```
7. Set the configuration variables needed by the app. Run `source secrets.sh`and then `source heroku_config.sh`
8. Ship your container to Heroku. Run successively:
```
docker tag YOUR_IMAGE_NAME registry.heroku.com/YOUR_APP_NAME/web
heroku container:login
docker push registry.heroku.com/YOUR_APP_NAME/web
heroku container:release web -a YOUR_APP_NAME
```
9. Check the result ! `heroku open -a YOUR_APP_NAME`

My MLFlow server can be found [here](https://bloc5-pricing-optimization.herokuapp.com/)
