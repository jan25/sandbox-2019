# Jaeger HOTROD app written in Python3

## Run or develop

- Setup virtual env
```
$ venv .venv
$ source .venv/bin/activate
```
- Start up services
```
$ sh run.sh frontend
$ sh run.sh customer
$ sh run.sh route
$ sh run.sh driver
```
- Open HotR.O.D. app at [localhost:8080](localhost:8080)
------------------------
### Done
- setup services and connect them

### Todo
- add driver file to kick start all services from one place
- add logging to each service
- instrument services and push traces to jaeger
- Update `dependencies.txt`

>
> **Credits** Blog post on HotR.O.D application https://medium.com/opentracing/take-opentracing-for-a-hotrod-ride-f6e3141f7941
>