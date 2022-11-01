from flask import Flask
import flaskcode
import os
from waitress import serve

app = Flask(__name__)
app.config.from_object(flaskcode.default_config)
app.config['FLASKCODE_RESOURCE_BASEPATH'] = './file'
app.register_blueprint(flaskcode.blueprint, url_prefix='/painel/edit')


@app.route('/painel')
def painel():
    file = open('./file/config.json', 'r')
    insideFile = file.read()
    file.close()
    return insideFile

@app.errorhandler(404)
def page_not_found(error):
    return 'This page not exist', 404

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=5000)