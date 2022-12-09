from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
from pymongo import MongoClient
import parse
# 오라클IP주소 : http://132.226.21.169:5000
# 로컬주소 : http://10.175.76.36:5000

'''DB'''
client = MongoClient('mongodb+srv://xyro:wjddnjstjr@cluster0.4nexu.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.namespace_1

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
all_users = list(db.REF.find({},{'_id':False}))



'''Flask'''
app = Flask(__name__)
CORS(app, resources={r'*': {'origins': '*'}})

@app.route('/test')
def test_home():
   return render_template('test.html')

@app.route('/')
def home():
    return 'access success (Cloud API Server)'
    # return render_template('index.html')

@app.route('/json')
def json2():
    return jsonify(all_users)

@app.route('/vs')
def vs():
    json_value = db.REF.find_one({'model':'vs'})
    output = json_value['link_a']
    return output

#q3
@app.route('/get', methods=['GET']) # /get?data=inputdata
def test_get():
    data = request.args.get('data')
    print(data)
    return jsonify({'result':'success', 'msg':f'GET요청 완료 {data}'})

# q4
@app.route('/test', methods=['POST'])
def test_post():
    aaa = request.form.get['data_1']
    print(aaa)
    return jsonify({'result':'success', 'msg': f'이 요청은 {aaa}'})

# q5
@app.route('/', methods=['POST'])
def q5():
    model = request.form.get('data_1')
    json_value = db.REF.find_one({'model':model})
    output = json_value['link_a']
    print(output)
    return output
    
if __name__ == '__main__':
    app.run('0.0.0.0')

