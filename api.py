# coding = utf-8
# NAME: api
from flask import Flask

app = Flask(__name__)


@app.route('/api/test')
def hello_world():
    '''
    测试接口1234569999
    :return: success
    '''
    return 'success777'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)