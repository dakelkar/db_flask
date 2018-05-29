from flask import Blueprint, render_template, abort
from flask import Flask, flash, redirect, url_for, session, request
from isloggedin import is_logged_in
from create_hash import decodex

######################
# Section Blueprint
def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)
           
def construct_crudprint(name, section_db):
    crudprint = Blueprint(name, __name__, template_folder='templates')

    @crudprint.route('/edit/<folder_hash>/<pk>', methods=['GET', 'POST'])
    @is_logged_in
    def edit(folder_hash, pk):
        form = section_db.get_from_request(request.form)

        if request.method == 'GET':
            form = section_db.get_item(pk)
            if form is None:
                # ugh not found!
                abort(404)
            
        if request.method == 'POST' and form.validate():
            success_flag, result = section_db.update_item(form, session['username'])

            if not success_flag:
                flash('Error: ' + str(result), 'danger')
            else:
                flash('Updated: ' + str(result), 'success')

            return redirect(url_for('view_folder', folder_hash=folder_hash))

        return render_template('section_item.html', form=form)

    @crudprint.route('/add/<folder_hash>', methods=['GET', 'POST'])
    @is_logged_in
    def add(folder_hash):
        folder_number = decodex(folder_hash)
        form = section_db.get_from_request(request.form)
        form.fld_folder_number.data = folder_number

        if request.method == 'POST' and form.validate():
            success_flag, result = section_db.add_item(form, session['username'])

            if not success_flag:
                flash('Error: ' + str(result), 'danger')
            else:
                flash('Created: ' + str(result), 'success')

            return redirect(url_for('view_folder', folder_hash=folder_hash))

        return render_template('section_item.html', form=form)

    @crudprint.route('/delete/<folder_hash>/<pk>', methods=['GET', 'POST'])
    @is_logged_in
    def delete(folder_hash, pk):
        if request.method == 'GET':
            form = section_db.get_item(pk)
            if form is None:
                # ugh not found!
                abort(404)

            flash('Click Submit Form to Delete', 'danger')
            return render_template('section_item.html', form=form)


        if request.method == 'POST':
            success_flag, error = section_db.delete_item(pk)
            if not success_flag:
                flash('Error deleting: ' + str(error), 'danger')
            else:
                flash('Deleted', 'success')

        return redirect(url_for('view_folder', folder_hash=folder_hash))

    return crudprint

