from flask import Blueprint

product=Blueprint('product',__name__,url_prefix='/product')

@product.route('/')
def index():
    return 'product'
