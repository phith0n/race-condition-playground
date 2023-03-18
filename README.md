# Race Condition Playground

This project is to demonstrate a vulnerable app that can be exploited by race condition attack.

Runs on Linux:

```
gunicorn -w 2 -k gevent -b 0.0.0.0:8000 race_condition_playground.wsgi
```

Runs on Windows:

```
waitress-serve --port=8000 race_condition_playground.wsgi:application
```

There is 4 routers that you can try to attack:

- `/ucenter/1/`
- `/ucenter/2/`
- `/ucenter/3/`
- `/ucenter/4/`

The first two contain race condition issues, the last two are secure.
