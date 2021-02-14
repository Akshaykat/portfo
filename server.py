from flask import Flask,render_template,url_for,request,redirect
app = Flask(__name__)#We use Flask class to instanstiate app...
print(__name__)


@app.route('/') 
def home():
	
	return render_template('index.html')
	

@app.route('/<string:page_name>')
def home1(page_name):
	
	return render_template(page_name)    


# @app.route('/about.html')
# def about():
#     return render_template('about.html')  


# @app.route('/works.html') 
# def works():
#     return render_template('works.html') 

# @app.route('/submit_form', methods=['POST', 'GET'])
# def submit_form():
#     return "Thank you! for submitting the form"

def write_to_file(data):
	with open('database.txt',mode='a') as database:
		email=data['email']
		subject=data['subject']
		message=data['message']
		file=database.write(f'\n{email},{subject},{message}')



@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
	if request.method =='POST':
	 data=request.form.to_dict() 
	 # print(data)
	 write_to_file(data)
	 return redirect('/Thanks.html')
	else:
	 return 'something went wrong!Try again'

   



  