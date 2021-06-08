{
'name': 'Library Members and Borrowing',
'description': 'Use library cards for people to borrow books.',
'author': 'Daniel Reis',
'data': [
    'views/book_view.xml',
    'security/ir.model.access.csv',
    'security/library_security.xml',
],
'depends': [
    'library_app',
],
'application': False,
}

