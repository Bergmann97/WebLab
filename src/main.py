import os

from flask import Flask, request
from flask import render_template

from protoBtnClick import onRetrieveClick, onWikidataRetrievalClick
from protoBtnClick import onRetrieveTwitterClick
from protoBtnClick import onApproveClick
from protoBtnClick import onListClick
from protoBtnClick import onListApprovedClick


app = Flask(__name__)


def cleanLog():
    with open('templates/test.html', 'w') as f:
        f.write('<p>Waiting for log!</p>')


@app.route('/', methods=['POST', 'GET'])
def index():
    cleanLog()
    content = "Nothing happend!"
    if request.method == 'POST':
        if request.form['protoBtn'] == '1':
            content = onRetrieveClick(app)
        if request.form['protoBtn'] == '2':
            content = onRetrieveTwitterClick(app)
        if request.form['protoBtn'] == '3':
            content = onApproveClick(app)
        if request.form['protoBtn'] == '4':
            content = onListClick(app)
        if request.form['protoBtn'] == '5':
            content = onListApprovedClick(app)
        if request.form['protoBtn'] == '6':
            content = onWikidataRetrievalClick(app)

    return render_template('index.html', content=content)


@app.route('/test.html')
def test():
    return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
