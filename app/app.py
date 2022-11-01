from flask import Flask
import flaskcode
import os

app = Flask(__name__)
app.config.from_object(flaskcode.default_config)
app.config['FLASKCODE_RESOURCE_BASEPATH'] = './file'
app.register_blueprint(flaskcode.blueprint, url_prefix='/painel/edit')



@app.error_handler_spec(404)
def hello():
    return "Hello World!"

@app.route('/painel')
def painel():
    file = open('./file/config.json', 'r')
    insideFile = file.read()
    file.close()
    return insideFile

if __name__ == '__main__':
    app.debug = True
    app.run(port=80)