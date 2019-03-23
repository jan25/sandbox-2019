# Build nginx static file container

## Builds static files from vue files and spits them into public folder
```
./build.sh
```

## One off run docker container
```
docker run  -d -p 8080:80 simple-vue-app
```
- visit [localhost:8080](localhost:8080) to see index.html being served

# simple-app [Vue app]

- created using
```
vue create simple-app
```
- ^ This comes with whole build process within

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
