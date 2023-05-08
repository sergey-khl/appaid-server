from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import json
import uuid
from json import JSONDecoder, loads

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

components = r"""Here is an example JSON for the checkout page JSX of a workout application:

```
{
  "jsx": {
    "type": "View",
    "props": {
      "style": {
        "flex": 1,
        "padding": 20
      }
    },
    "children": [
      {
        "type": "Text",
        "props": {
          "style": {
            "fontSize": 24,
            "fontWeight": "bold",
            "marginBottom": 10
          }
        },
        "children": "Checkout"
      },
      {
        "type": "View",
        "props": {
          "style": {
            "borderWidth": 1,
            "borderColor": "#ccc",
            "padding": 10,
            "marginBottom": 20
          }
        },
        "children": [
          {
            "type": "Text",
            "props": {
              "style": {
                "fontSize": 16
              }
            },
            "children": "Total: $50"
          }
        ]
      },
      {
        "type": "TextInput",
        "props": {
          "style": {
            "borderWidth": 1,
            "borderColor": "#ccc",
            "padding": 10,
            "marginBottom": 20
          },
          "placeholder": "Name on Card"
        }
      },
      {
        "type": "TextInput",
        "props": {
          "style": {
            "borderWidth": 1,
            "borderColor": "#ccc",
            "padding": 10,
            "marginBottom": 20
          },
          "placeholder": "Card Number"
        }
      },
      {
        "type": "View",
        "props": {
          "style": {
            "flexDirection": "row",
            "justifyContent": "space-between"
          }
        },
        "children": [
          {
            "type": "TextInput",
            "props": {
              "style": {
                "borderWidth": 1,
                "borderColor": "#ccc",
                "padding": 10,
                "width": "48%"
              },
              "placeholder": "Expiry Date"
            }
          },
          {
            "type": "TextInput",
            "props": {
              "style": {
                "borderWidth": 1,
                "borderColor": "#ccc",
                "padding": 10,
                "width": "48%"
              },
              "placeholder": "CVV"
            }
          }
        ]
      },
      {
        "type": "TouchableOpacity",
        "props": {
          "style": {
            "backgroundColor": "#4CAF50",
            "padding": 10,
            "marginTop": 20,
            "alignItems": "center"
          },
          "onPress": "submit"
        },
        "children": [
          {
            "type": "Text",
            "props": {
              "style": {
                "color": "#fff",
                "fontWeight": "bold"
              }
            },
            "children": "Place Order"
          }
        ]
      }
    ]
  }
}
```

Note that this is just an example and the actual JSX for a checkout page may vary depending on the specific requirements and design of the workout application."""




@app.route('/components', methods=["GET"])
@cross_origin()
def get_incomes():
    parseString = extract_json_objects(components)
    component = add_uuid(parseString["jsx"])
    print(component, flush=True)
    return jsonify(component)


# @app.route('/incomes', methods=['POST'])
# def add_income():
#     incomes.append(request.get_json())
#     return '', 204