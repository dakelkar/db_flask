from flask import Blueprint, render_template, abort
from flask import Flask, flash, redirect, url_for, session, request
from isloggedin import is_logged_in
from create_hash import decodex

######################
# Section Blueprint
def construct_crudprint(name, section_db):
    crudprint = Blueprint(name, __name__, template_folder='templates')

    # @repeater.route('/', defaults={'page': 'index'})
    @crudprint.route('/<folder_hash>', methods=['GET', 'POST'])
    @is_logged_in
    def add_or_edit(folder_hash):
        folder_number = decodex(folder_hash)
        form = section_db.get_from_request(request.form, folder_number)

        # here we want to get the value of mode (i.e. ?mode=add)
        is_add = request.args.get('mode') == "add"

        if request.method == 'GET':
            existing_form = section_db.get_item(folder_number)
            if is_add:
                if existing_form is not None:
                    # ugh already exists?
                    abort(409)
            else:
                form = existing_form
                if existing_form is None:
                    # ugh not found!
                    abort(404)
            
        if request.method == 'POST' and form.validate():
            op = section_db.update_item
            if is_add:
                op = section_db.add_item

            success_flag, error = op(form)

            if not success_flag:
                flash('Error: ' + str(error), 'danger')
            else:
                flash('Updated', 'success')

            return redirect(url_for('view_folder', folder_hash=folder_hash))

        return render_template('section_item.html', form=form)

    @crudprint.route('/delete/<folder_hash>', methods=['POST'])
    @is_logged_in
    def delete(folder_hash):
        folder_number = decodex(folder_hash)
        success_flag, error = section_db.delete_item(folder_number)

        if not success_flag:
            flash('Error deleting: ' + str(error), 'danger')
        else:
            flash('Deleted', 'success')

        return redirect(url_for('view_folder', folder_hash=folder_hash))

    return crudprint

