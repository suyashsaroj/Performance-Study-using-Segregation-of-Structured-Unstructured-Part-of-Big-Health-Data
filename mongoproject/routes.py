from flask import render_template, url_for, flash, redirect, request
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components

from mongoproject import app, mongo
import time

@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',title='Home')	

@app.route("/about")
def about():
	return render_template('about.html', title='About')

@app.route("/query")
def query():
	return render_template('query.html',title='Query')

@app.route('/upload', methods=['POST','GET'])
def uploadFile():
	if 'document' in request.files:
		document = request.files['document']
		mongo.save_file(document.filename, document)
		mongo.db.ECG.insert({'Patient_ID': request.form.get('Patient_ID'), 'document_name': document.filename})
		flash(f'Image Uploaded Successfully.','success')
	return render_template('upload.html')

@app.route('/file/<filename>')
def file(filename):
	return mongo.send_file(filename)

@app.route("/query/q1", methods=['POST','GET'])
def q1():
	x = [100, 500, 1000, 5000, 10000, 20000, 35000, 50000, 75000, 100000]
	y = [2, 2.99, 3.31, 4.99, 8.17, 16.97, 24.99, 42.98, 59.98, 79.97]
	plot = figure(title = 'Query 1', x_axis_label = 'Number of Records', y_axis_label = 'Execution Time(in ms)', plot_width = 700, plot_height = 400)
	plot.line(x, y, legend='f(x)', line_width=2)
	script, div = components(plot)
	context = {
		'timep': "Time Performance(in ms): ",
		'script' : script ,
		'div' : div
	}
	start_time = time.time()
	organisation = request.form.get('organisation')
	if organisation is None:
		return render_template('q1.html')
	doctors = mongo.db.mongo_doctor.find({"Organisation": organisation})
	print(doctors.explain())
	end_time = time.time()
	timep = (end_time - start_time)*1000
	return render_template('query1.html',title='Query 1', context=context, timep=timep, doctors=doctors)

@app.route("/query/q2", methods=['POST','GET'])
def q2():
	x = [100, 500, 1000, 5000, 10000, 20000, 35000, 50000, 75000, 100000]
	y = [4.99, 5.99, 8.99, 11.99, 17.94, 30.97, 46.98, 56.60, 61.96, 80.99]
	plot = figure(title = 'Query 2',x_axis_label = 'Number of Records', y_axis_label = 'Execution Time(in ms)', plot_width = 700, plot_height = 400)
	plot.line(x, y, legend='f(x)', line_width=2)
	script, div = components(plot)
	context = {
		'timep': "Time Performance(in ms): ",
		'script' : script ,
		'div' : div
	}
	start_time = time.time()
	specialization = request.form.get('specialization')
	if specialization is None:
		return render_template('q2.html')
	doctors = mongo.db.mongo_doctor.find({"Specialization": specialization})
	print(doctors.explain())
	end_time = time.time()
	timep = (end_time - start_time)*1000
	return render_template('query2.html',title='Query 2', context=context, timep=timep, doctors=doctors)

@app.route("/query/q3", methods=['POST','GET'])
def q3():
	x = [100, 500, 1000, 5000, 10000, 20000, 35000, 50000, 75000, 100000]
	y = [3.19, 5.12, 6.99, 9.37, 16.50, 27.96, 39.87, 49.23, 62.98, 76.97]
	plot = figure(title = 'Query 3', x_axis_label = 'Number of Records', y_axis_label = 'Execution Time(in ms)', plot_width = 700, plot_height = 400)
	plot.line(x, y, legend='f(x)', line_width=2)
	script, div = components(plot)
	context = {
		'name': "Name",
		'demo': "Demographic Information",
		'habit': "Food Habit",
		'timep': "Time Performance(in ms): ",
		'script': script,
		'div': div
	}
	start_time = time.time()
	person_id = request.form.get('ID')
	if person_id is None:
		return render_template('q3.html')
	persons = mongo.db.mongo_person.find({"Person_Id": person_id})
	print(persons.explain())
	end_time = time.time()
	timep = (end_time - start_time)*1000
	return render_template('query3.html',title='Query 3', timep=timep, context=context, persons=persons)

@app.route("/query/q4", methods=['POST','GET'])
def q4():
	x = [100, 500, 1000, 5000, 10000, 20000, 35000, 50000, 75000, 100000]
	y = [3.97, 5.32, 6.04, 12.98, 16.09, 28.98, 32.93, 40.01, 53.95, 63.16]
	plot = figure(title = 'Query 4', x_axis_label = 'Number of Records', y_axis_label = 'Execution Time(in ms)', plot_width = 700, plot_height = 400)
	plot.line(x, y, legend='f(x)', line_width=2)
	script, div = components(plot)
	context = {
		'name': "Name",
		'complaint_details': "Complaint Details",
		'timep': "Time Performance(in ms): ",
		'script': script,
		'div': div
	}
	start_time = time.time()
	patient_id = request.form.get('ID')
	if patient_id is None:
		return render_template('q4.html')
	patients = mongo.db.mongo_patient.find({"Patient_ID": patient_id})
	print(patients.explain())
	end_time = time.time()
	timep = (end_time - start_time)*1000
	return render_template('query4.html',title='Query 4', timep=timep, context=context, patients=patients)

@app.route("/query/q5")
def q5():
	x = [100, 500, 1000, 5000, 10000, 20000, 35000, 50000, 75000, 100000]
	y = [2.00, 3.11, 5.99, 15.21, 22.05, 30.49, 38.97, 54.96, 68.93, 86.13]
	plot = figure(title = 'Query 5', x_axis_label = 'Number of Records', y_axis_label = 'Execution Time(in ms)', plot_width = 700, plot_height = 400)
	plot.line(x, y, legend='f(x)', line_width=2)
	script, div = components(plot)
	context = {
		'name': "Name",
		'complaint_details': "Complaint Details",
		'number': "Number of children: ",
		'timep': "Time Performance(in ms): ",
		'script': script,
		'div': div
	}
	start_time = time.time() 
	children = mongo.db.mongo_patient.find({"Age":{'$gt':5}, "Complaint_Details":"Malnutrition"})
	print(children.explain())
	end_time = time.time()
	timep = (end_time - start_time)*1000
	return render_template('q5.html',title='Query 5',timep=timep, children=children, count=children.count(True),context=context)

@app.route("/query/q6", methods=['POST','GET'])
def q6():
	x = [100, 500, 1000, 5000, 10000, 20000, 35000, 50000]
	y = [2.87, 4.05, 4.98, 7.46, 12.75, 21.93, 37.93, 43.38]
	plot = figure(title = 'Query 6', x_axis_label = 'Number of Records', y_axis_label = 'Execution Time(in ms)', plot_width = 700, plot_height = 400)
	plot.line(x, y, legend='f(x)', line_width=2)
	script, div = components(plot)
	start_time = time.time()
	patient_id=request.form.get('ID')
	context = {
		'name': "Name",
		'complaint_details': "Complaint Details",
		'timep': "Time Performance(in ms): ",
		'script': script,
		'div': div,
		'id':patient_id
	}
	if patient_id is None:
		return render_template('q6.html')
	cursor = mongo.db.ECG.find_one({"Patient_ID":patient_id})
	if cursor is None:
		return render_template('q6.html')
	print(cursor);
	end_time = time.time()
	timep = (end_time - start_time)*1000
	return render_template('query6.html', filename=cursor['document_name'], context=context, timep=timep)

@app.route("/feedback", methods=['POST','GET'])
def feedback():
	Name = request.form.get('Name')
	Email = request.form.get('Email')
	Feedback = request.form.get('Feedback')
	if Email is not None:
		flash(f'Your Feedback is successfully Submitted.')
	cursor = mongo.db.mongo_Feedback.insert_one({"Name": Name, "Email":Email, "Feedback":Feedback})
	return render_template('home.html')