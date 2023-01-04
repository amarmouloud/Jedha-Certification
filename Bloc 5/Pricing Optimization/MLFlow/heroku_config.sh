APP_NAME="bloc5-pricing-optimization"
heroku config:set ARTIFACT_ROOT=$ARTIFACT_ROOT -a $APP_NAME
heroku config:set AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID -a $APP_NAME
heroku config:set AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY -a $APP_NAME
heroku config:set BACKEND_STORE_URI=$BACKEND_STORE_URI -a $APP_NAME
