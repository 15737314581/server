# coding = utf-8
# NAME: api
from flask import Flask

app = Flask(__name__)


@app.route('/api/test')
def hello_world():
    '''
    测试接口123456
    :return: success
    '''
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)