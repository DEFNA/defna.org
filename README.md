# defna.org website

## Getting Started

### to build the project

```shell
docker-compose build
```

### to start the project's web servers

To make development easier, the DEFNA website runs locally on two ports (tl;dr: use http://localhost:8000)

- http://localhost:8000 - (the one you want to use) devd proxy which will autoload changes without you having to refresh
- http://localhost:4000 - Jekyll running in auto-build mode


```shell
docker-compose up

# or in detached mode
docker-compose up --detached
```

### to stop the project

```shell
docker-compose down
```
