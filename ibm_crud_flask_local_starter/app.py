# IBM Generative AI Engineering / Flask CRUD Lab
# Local starter version for VS Code.
# Complete the TODOs yourself as you move through the lab.

# TODO 1: Import the Flask tools required by the lab:
# Flask, request, url_for, redirect, render_template

# TODO 2: Instantiate the Flask application as `app`.

# IBM-provided sample data (optional in the official lab)
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300},
]

# READ OPERATION
# TODO: Create get_transactions() and map it to `/`.
# It should render transactions.html and pass `transactions` to the template.


# CREATE OPERATION
# TODO: Create add_transaction() for `/add` handling GET and POST.
# GET  -> render form.html
# POST -> read form data, create a transaction, append it, redirect to the list


# UPDATE OPERATION
# TODO: Create edit_transaction(transaction_id) for
# `/edit/<int:transaction_id>` handling GET and POST.
# GET  -> find the transaction and render edit.html
# POST -> update it and redirect to the list


# DELETE OPERATION
# TODO: Create delete_transaction(transaction_id) for
# `/delete/<int:transaction_id>`.
# Find the matching transaction, remove it, then redirect to the list.


# FINAL STEP
# TODO: Add the __main__ guard and run the Flask development server.
