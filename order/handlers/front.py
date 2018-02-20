from flask import Blueprint,render_template
from order.models import Product,User
from flask import request,response,make_response,redirect,jsonify
import json

front=Blueprint('front',__name__)

@front.route('/')
def index():
    products=Product.query.all()
    users=User.query.all()
    return render_template('index.html',products=products,users=users)

@front.route('/order',methods=['Get','POST'])
def order():
    if request.method=='POST':
        itemid=request.form['itemid']
        uid=request.form['uid']
        num=request.form['num']
        content=orderr(itemid,uid,num)
        resp=Response_headers(content)
        return resp

def orderr(itemid,uid,num):
    result={}
    product=Product.query.filter_by(id=itemid).first()
    user=User.query.filter_by(id=uid).first()
    if product.price*num > user.money:
        result['success']=False
        result['msg']='money not enough'
    elif num > product.quantity:
        result['success']=False
        result['msg']='more than quantity'
    else:
        user.money=(user.money-product.price*num)
        product.quantity=(product.quantity-num)
        result['success']=True
        result['msg']='order success'
    result['time']=datetime.now()
    return json.dumps(result)

