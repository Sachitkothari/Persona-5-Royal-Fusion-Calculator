from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/', methods=['GET'])
def base_route():
    return "Add /persona_fusion_calculator?persona1=(p1name)&persona2=(p2name) to the URL"

@app.route('/persona_fusion_calculator', methods=['GET'])
def get_fused_persona():
    persona1 = request.args.get('persona1')
    persona2 = request.args.get('persona2')
    return (persona1 + persona2)

if __name__ == '__main__':
    app.run()