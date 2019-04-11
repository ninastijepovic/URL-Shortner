# URL-Shortner
Requirements: install flask using

```sudo apt install python-pip```

```sudo pip install flask flask-restful```

Run:
```python shortner.py```

TEST on localhost:
successful req:

```curl http://127.0.0.1:5000/  -X GET -i```

```curl http://127.0.0.1:5000/ -d "url=https://example.com" -X POST -i```

```curl http://127.0.0.1:5000/0 -X DELETE -i```

