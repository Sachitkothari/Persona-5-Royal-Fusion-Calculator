from flask import Flask, request
import ctypes
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.add_dll_directory(BASE_DIR)
dll_path = os.path.join(BASE_DIR, "persona.dll")
lib = ctypes.CDLL(dll_path)
lib.merge.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.merge.restype = ctypes.c_char_p

app = Flask(__name__)

@app.route('/', methods=['GET'])
def base_route():
    return "Add /persona_fusion_calculator?persona1=(p1name)&persona2=(p2name) to the URL"

@app.route('/persona_fusion_calculator', methods=['GET'])
def get_fused_persona():
    persona1 = request.args.get('persona1')
    persona2 = request.args.get('persona2')
    result = lib.merge(persona1.encode(), persona2.encode()).decode()
    return result

if __name__ == '__main__':
    app.run()