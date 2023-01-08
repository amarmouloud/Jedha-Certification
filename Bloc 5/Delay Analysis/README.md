## Data exploration and preprocessing
An exploratory data analysis can be found in the `EDA.ipynb`. In the same notebook, the data are preprocessed in order to be used in the dashboard.

## Deploy an Streamlit app on Heroku

1. Build your Docker image `docker buildx build --platform linux/amd64 -t YOUR_IMAGE_NAME .`
2. Log in Heroku `heroku login`
3. Ship your container to Heroku. Run successively:
```
docker tag YOUR_IMAGE_NAME registry.heroku.com/YOUR_APP_NAME/web
heroku container:login
docker push registry.heroku.com/YOUR_APP_NAME/web
heroku container:release web -a YOUR_APP_NAME
```
9. Check the result ! `heroku open -a YOUR_APP_NAME`

My Dashboard can be found [here](https://bloc5-delay-analysis.herokuapp.com/)

