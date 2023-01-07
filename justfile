@_default:
    just --list

# installs/updates all dependencies
@bootstrap:
    docker-compose pull
    docker-compose build

# invoked by continuous integration servers to run tests
@cibuild:
    just bootstrap

@clean:
    rm -rf .vendor _site Gemfile.lock

@fmt:
    just --fmt --unstable

@restart:
    docker-compose restart

# starts app
@server *ARGS:
    docker-compose up {{ ARGS }}

# sets up a project to be used for the first time
@setup:
    just bootstrap

@start +ARGS="--detach":
    just server {{ ARGS }}

@stop:
    docker-compose down

@tail:
    docker-compose logs --follow --tail 100

# runs tests
@test:
    echo "TODO: test"

# updates a project to run at its current version
@update:
    just bootstrap
