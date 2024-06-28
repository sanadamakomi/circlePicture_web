# circlePicture_web
circlePicture web application composed by python-shiny

# Install 
## Build Image 
```
docker build -t circle_picture:latest .
```
## Run container
```
docker run -it -p 3838:80 circle_picture:latest
```

It can be visited by http://127.0.0.1/3838

OR Run Container By [ShinyProxy](https://github.com/openanalytics/shinyproxy-shiny-for-python-demo).

`application.yml` containing:

```
  specs:
  - id: circle
    display-name: Circle Picture
    port: 53838
    container-image: circle_picture
```
