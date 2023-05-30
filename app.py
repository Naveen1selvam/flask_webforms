from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

FAI=Flask(__name__)

class Nameform(Form):
    name=StringField(validators=[DataRequired()])
    submit=SubmitField()
@FAI.route('/webform',methods=['GET','POST'])
def webform():
    NFO=Nameform()
    if request.method=='POST':
        NFD=Nameform(request.form)
        if NFD.validate():
            return NFD.name.data
    return render_template('webform.html',NFO=NFO)

if __name__=='__main__':
    FAI.run(debug=True)