"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file creates your application.
"""

import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash, session, abort, send_from_directory
from werkzeug.utils import secure_filename
from app.forms import PropertyForm
from app.models import Properties

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/properties/create', methods=['POST', 'GET'])
def create_property():
    form = PropertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            title = form.proptitle.data
            description = form.description.data
            rooms = form.beds.data
            baths = form.baths.data
            price = form.price.data
            ptype = form.proptype.data
            location = form.location.data
            file = form.photo.data

            #getting the filename of the image uploaded
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            propentry = Properties(title, description, rooms, baths, price, ptype, location, filename)
            db.session.add(propentry)
            db.session.commit()

            flash('Property added!', 'success')
            return redirect(url_for("view_all_properties"))
        else:
            fflash_errors(form)
    return render_template("create.html", form=form)


#helper function which iterates over the contents of the uploads folder and returns the filenames in a list 
def get_uploaded_images():
    import os
    rootdir = os.getcwd()
    file_list = []

    for subdir, dirs, files in os.walk(rootdir + '/uploads'):
        for file in files:
            file_list.append(os.path.join(file))
    return file_list



@app.route('/uploads/<filename>')
def get_image(filename):
    return send_from_directory(os.path.join(os.getcwd(),app.config['UPLOAD_FOLDER']), filename)

@app.route('/properties')
def view_all_properties():
    prop = Properties.query.all()
    return render_template('proplist.html', prop = prop)

@app.route('/properties/<propertyid>')

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port="8080")
