# circlePicture_web
[circlePicture](https://github.com/sanadamakomi/circlePicture) web application composed by python-shiny, [Example](https://makotofan.xyz/app/circle)

# Install 
## Build Image 
```
docker build -t circle_picture:latest .
```
## Run container
```
docker run -it -p 53838:53838 circle_picture:latest
```

It can be visited by http://127.0.0.1/53838

OR Run Container By [ShinyProxy](https://github.com/openanalytics/shinyproxy-shiny-for-python-demo).

`application.yml` containing:

```
  specs:
  - id: circle
    display-name: Circle Picture
    port: 53838
    container-image: circle_picture
```


# Update

* 2024.08.19: add note.png
