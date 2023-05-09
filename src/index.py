from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import uuid
from json import JSONDecoder, loads
from dotenv import load_dotenv
import os


load_dotenv()
SECRET_KEY = os.getenv("open_ai_key")
print(SECRET_KEY, flush=True)


app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})
#app.config['CORS_HEADERS'] = 'application/json'



def extract_json_objects(text, decoder=JSONDecoder()):
    pos = 0
    while True:
        match = text.find('{', pos)
        if match == -1:
            break
        try:
            result, index = decoder.raw_decode(text[match:])
            return result
        except ValueError:
            pos = match + 1

def add_uuid(comp):
    comp["uuid"] = str(uuid.uuid4())
    
    try:
        for child in comp["children"]:
            add_uuid(child)
    except Exception as e:
        print(e)
    return comp    

components = r"""Here is an example JSON for the JSX of a Tic Tac Toe game component in React Native:

```
{
  "jsx": {
    "type": "View",
    "props": {
      "style": {
        "flex": 1,
        "justifyContent": "center",
        "alignItems": "center"
      }
    },
    "children": [
      {
        "type": "Text",
        "props": {
          "style": {
            "fontSize": 24,
            "fontWeight": "bold",
            "marginBottom": 20
          },
          "children": "Tic Tac Toe"
        }
      },
      {
        "type": "View",
        "props": {
          "style": {
            "flexDirection": "row"
          }
        },
        "children": [
          {
            "type": "View",
            "props": {
              "style": {
                "borderWidth": 2,
                "borderColor": "#000",
                "width": 100,
                "height": 100,
                "alignItems": "center",
                "justifyContent": "center"
              },
              "children": [
                {
                  "type": "Text",
                  "props": {
                    "style": {
                      "fontSize": 50
                    },
                    "children": ""
                  }
                }
              ]
            }
          },
          {
            "type": "View",
            "props": {
              "style": {
                "borderWidth": 2,
                "borderColor": "#000",
                "width": 100,
                "height": 100,
                "alignItems": "center",
                "justifyContent": "center"
              },
              "children": [
                {
                  "type": "Text",
                  "props": {
                    "style": {
                      "fontSize": 50
                    },
                    "children": ""
                  }
                }
              ]
            }
          },
          {
            "type": "View",
            "props": {
              "style": {
                "borderWidth": 2,
                "borderColor": "#000",
                "width": 100,
                "height": 100,
                "alignItems": "center",
                "justifyContent": "center"
              },
              "children": [
                {
                  "type": "Text",
                  "props": {
                    "style": {
                      "fontSize": 50
                    },
                    "children": ""
                  }
                }
              ]
            }
          }
        ]
      },
      {
        "type": "View",
        "props": {
          "style": {
            "marginTop": 20
          }
        },
        "children": [
          {
            "type": "Button",
            "props": {
              "title": "Reset",
              "onPress": "() => {}"
            }
          }
        ]
      }
    ]
  }
}
```

Note that this is just an example and there are many ways to implement a Tic Tac Toe game in React Native."""




@app.route('/components', methods=["GET"])
@cross_origin()
def get_incomes():
    parseString = extract_json_objects(components)
    component = add_uuid(parseString["jsx"])
    return jsonify(component)


# @app.route('/incomes', methods=['POST'])
# def add_income():
#     incomes.append(request.get_json())
#     return '', 204