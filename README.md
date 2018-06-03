build
```
docker build -t docdk/bcdb:latest .

```

dev setup
```
conda env create -f conda.yml
activate flask_b4
git clone --branch bootstrap-v4 https://github.com/rakelkar/flask-bootstrap/bootstrap-v4
cd flask-bootstrap
pip install -e .
```

db setup
1. install mongodb
2. run mongod!


test
```
python -m unittest tests.py
```