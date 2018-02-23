# dev

## make a virtual env and install requirements

```bash
$ mkvirtualenv {name}
$ pip install -r requirements.txt
```

## start

```bash
$ make start
```

## deploy

```bash
$ heroku apps:create {app_name}
$ git push heroku master
```
