from functools import wraps
from flask import request, jsonify
from app import app, auth_required
import os
import re

# ctf{2-y0u_4r3_n0t_supp0sed_t0_b3_h3r3}

@app.route('/this_is_an_endpoint/that_most_wordlists/would_not_find', methods=['GET', 'POST'])
@auth_required
def admin_endpoint():
    # Get the POST parameter containing the command
    command = request.form.get('command')
    # This should be enough for protection, right?
    sanitized_command = re.sub(r'\s+', '', command)
    # Execute the command using os.system()
    os.system(sanitized_command)
    return jsonify({"Command executed successfully."})
