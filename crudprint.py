from flask import Blueprint, render_template, abort
from flask import flash, redirect, url_for, session, request
from isloggedin import is_logged_in

######################
# Section Blueprint
def redirect_url(default='index'):
    return request.args.get('next') or \
           request.referrer or \
           url_for(default)
           
def construct_crudprint(name, section_db, folder_db):
    crudprint = Blueprint(name, __name__, template_folder='templates')

    @crudprint.route('/edit/<folder_pk>/<pk>', methods=['GET', 'POST'])
    @is_logged_in
    def edit(folder_pk, pk):
        folder_number = folder_db.folder_check(folder_pk)
        if folder_number is None:
            flash(folder_pk + ' not found', 'danger')
            return redirect(url_for('dashboard'))
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

            return redirect(url_for('view_folder', folder_pk=folder_pk))

        return render_template('section_item.html', form=form, folder_number = folder_number)



    @crudprint.route('/add/<folder_pk>', methods=['GET', 'POST'])
    @is_logged_in
    def add(folder_pk):
        folder_number = folder_db.folder_check(folder_pk)
        if folder_number is None:
            flash(folder_pk + ' not found', 'danger')
            return redirect(url_for('dashboard'))

        form = section_db.get_from_request(request.form)
        form.fld_folder_pk.data = folder_pk

        if request.method == 'POST' and form.validate():
            success_flag, result = section_db.add_item(form, session['username'])

            if not success_flag:
                flash('Error: ' + str(result), 'danger')
            else:
                flash('Created: ' + str(result), 'success')

            return redirect(url_for('view_folder', folder_pk=folder_pk))

        return render_template('section_item.html', form=form, folder_number = folder_number)

    @crudprint.route('/delete/<folder_pk>/<pk>', methods=['GET', 'POST'])
    @is_logged_in
    def delete(folder_pk, pk):
        if request.method == 'GET':
            form = section_db.get_item(pk)
            if form is None:
                flash('Item not found, already deleted', 'success')
                return redirect(url_for('view_folder', folder_pk=folder_pk))

            flash('Click Submit Form to Delete', 'danger')
            return render_template('section_item.html', form=form)

        result, message = section_db.delete_item(pk, session['username'])
        flash('Deleted: ' + message, 'success')
        return redirect(url_for('view_folder', folder_pk=folder_pk))

    return crudprint

