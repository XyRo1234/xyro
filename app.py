from flask import Flask, render_template, request, jsonify
import vimeo

client = vimeo.VimeoClient(
   token='{a2564c82673866860bf3a1aa772e652c}',
   key='{108039b6c7c021a4c845f8e19b63b6c6f99de8bd}',
   secret='{RHe7hofOMNr1oHFMfTDkoaOYi7XNyYwGTvFmhd0ZSrBxv4gypVwHCHgYoSl+97viJZP28Z3D7WwcsXCQPAVvBeZN5jEWCobEQQc3P5aq7WrycUL7rcmyJKvNhHtye3Q/}'
)

response = client.get('https://api.vimeo.com/oauth/access_token')
print(response.json())

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/preface_1')
def preface_1():
   return render_template('preface_1.html')

@app.route('/section_1')
def section_1():
   return render_template('section_1.html')

@app.route('/section_2')
def section_2():
   return render_template('section_2.html')

@app.route('/section_3')
def section_3():
   return render_template('section_3.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=3001, debug=True)