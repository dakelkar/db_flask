from flask import Blueprint, render_template, abort
from flask import Flask, flash, redirect, url_for, session, request
from isloggedin import is_logged_in
import uuid

######################
# Folder Blueprint
def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)

def construct_crudprint_folder(folder_db):
    name = 'folder'
    crudprint_folder = Blueprint(name, __name__, template_folder='templates')

    @crudprint_folder.route('/edit/<folder_hash>/<pk>', methods=['GET', 'POST'])
    @is_logged_in
    def edit(folder_hash):
        folder_number = folder_hash
        print('haha_edit')
        form = folder_db.get_from_request(request.form)

        if request.method == 'GET':
            form = folder_db.get_item(folder_number)
            if form is None:
                print ('ugh not found!')
                abort(404)
            
        if request.method == 'POST' and form.validate():
            success_flag, result = folder_db.update_item(form, session['username'])

            if not success_flag:
                flash('Error: ' + str(result), 'danger')
            else:
                flash('Updated: ' + str(result), 'success')

            return redirect(url_for('view_folder', folder_hash=folder_hash))

        return render_template('dashboard.html', form=form)

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

    @crudprint_folder.route('/delete/<folder_hash>', methods=['GET', 'POST'])
    @is_logged_in
    def delete(pk):
        if request.method == 'GET':
            form = folder_db.get_item(pk)
            if form is None:
                # ugh not found!
                abort(404)

            flash('Click Submit Form to Delete', 'danger')
            return render_template('folder_add.html', form=form)


        if request.method == 'POST':
            success_flag, error = folder_db.delete_item(pk)
            if not success_flag:
                flash('Error deleting: ' + str(error), 'danger')
            else:
                flash('Deleted', 'success')

        return redirect(url_for('dashboard'))

    @crudprint_folder.route('/view_folder/<folder_hash>/<pk>', methods=['GET'])
    @is_logged_in
    def view(folder_hash):
        folder_number = folder_hash
        form = folder_db.get_item(folder_number)
        return render_template('folder_add.html', form = form)

    return crudprint_folder