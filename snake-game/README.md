# snake-game

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

## Run app using Docker*
```
docker build -t snake-image
docker run --rm -d -p 8080:80 --name snake-app snake-image
```