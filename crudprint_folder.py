from flask import Blueprint, render_template, abort
from flask import flash, redirect, url_for, session, request
from isloggedin import is_logged_in

######################
# Folder Blueprint
def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

def construct_crudprint_folder(folder_db):
    name = 'folder'
    crudprint_folder = Blueprint(name, __name__, template_folder='templates')

    @crudprint_folder.route('/add_folder', methods=['GET', 'POST'])
    @is_logged_in
    def add_folder():
        form = folder_db.get_from_request(request.form)
        if request.method == 'POST' and form.validate():
            success_flag, result = folder_db.add_item(form, session['username'])
            if not success_flag:
                flash('Error: ' + str(result), 'danger')
            else:
                flash('Created: ' + str(result), 'success')
                return redirect(url_for('dashboard'))
        return render_template('folder_add.html', form=form)

    @crudprint_folder.route('/edit/<folder_pk>/', methods=['GET', 'POST'])
    @is_logged_in
    def edit(folder_pk):
        form = folder_db.get_from_request(request.form)
        if request.method == 'GET':
            form = folder_db.get_item(folder_pk)
            if form is None:
                print ('ugh not found!')
                abort(404)
            return render_template('folder_edit.html', form = form)

        if request.method == 'POST' and form.validate():
            success_flag, result = folder_db.update_item(form, session['username'])
            if not success_flag:
                flash('Error: ' + str(result), 'danger')
            else:
                flash('Updated: ' + str(result), 'success')
            return redirect(url_for('dashboard'))

        return render_template('folder_edit.html')

    @crudprint_folder.route('/delete/<folder_pk>', methods=['GET', 'POST'])
    @is_logged_in
    def delete(folder_pk):
        if request.method == 'GET':
            form = folder_db.get_item(folder_pk)
            if form is None:
                print('ugh not found!')
                abort(404)
            flash('Click Submit Form to Delete', 'danger')
            return render_template('folder_edit.html', form=form)

        result, message = folder_db.delete_item(folder_pk, session['username'])
        flash('Deleted: ' + message, 'success')
        return redirect(url_for('dashboard'))

    @crudprint_folder.route('/view_folder/<folder_pk>', methods=['GET'])
    @is_logged_in
    def view(folder_pk):
        return redirect(url_for('view_folder', folder_pk=folder_pk))

    return crudprint_folder