from flask import Flask, json
import mimerender
import logic

mimerender = mimerender.FlaskMimeRender()
render_json = lambda **args: json.dumps(args)

app = Flask(__name__)


@app.route('/pay_peroids_remaining', methods=['GET'])
@mimerender(default="json", json=render_json)
def api_pay_peroids_remaining():
    return {'pay_peroids_remaining': logic.pay_peroids_remaining()}

if __name__ == '__main__':
    app.run(debug=True, port=8002)
