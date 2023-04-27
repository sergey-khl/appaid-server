from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
#app.config['CORS_HEADERS'] = 'application/json'

components = ["""{
      "jsx": {
      "type": "TouchableOpacity",
      "props": {
      "activeOpacity": 0.8, 
      "style": {
      "backgroundColor": "#3b5998",
      "borderRadius": 10,
      "paddingVertical": 100,
      "paddingHorizontal": 20,
      "flexDirection": "row",
      "alignItems": "center",
      "justifyContent": "center",
      "shadowColor": "#000",
      "shadowOffset": {
      "width": 100,
      "height": 10  
      },
      "shadowOpacity": 0.3,
      "shadowRadius": 3,
      "elevation": 5
      }
      },
      "children": [
      {
      "type": "Text",
      "props": {
      "style": {
      "color": "#fff",
      "fontSize": 18,
      "fontWeight": "bold",
      "marginRight": 10
      }
      },
      "children": "Connect with Facebook"
      }
      ]
      }
      }"""]



@app.route('/components', methods=["GET"])
@cross_origin()
def get_incomes():
    return jsonify(json.loads(components[0]))


# @app.route('/incomes', methods=['POST'])
# def add_income():
#     incomes.append(request.get_json())
#     return '', 204