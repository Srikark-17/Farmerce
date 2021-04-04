from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import InputRequired

class CreateVendorForm(FlaskForm):
    organic = SelectField('Is your produce organic?', choices=['Yes', 'No', 'Somewhat', 'N/A'],
                          validators=[InputRequired()])
    price = SelectField('How expensive are your goods?', choices=['$', '$$', '$$$'], validators=[InputRequired()])
    name = StringField('Business Name', validators=[InputRequired()])
    description = StringField('Description', validators=[InputRequired()])
    methods = SelectField('What are your methods of farming?', choices=['Sustainable', 'Unsustainable', 'N/A'],
                          validators=[InputRequired()])
    chemical = SelectField('Do you use chemicals?', choices=['Yes', 'No', 'N/A'], validators=[InputRequired()])
    usda = SelectField('Have you received USDA approval?', choices=['Yes', 'No', 'N/A'], validators=[InputRequired()])
    contact = StringField('Contact Information', validators=[InputRequired()])
    produce = StringField('Items Available', validators=[InputRequired()])
    pic = StringField('Image Link', validators=[InputRequired()])

