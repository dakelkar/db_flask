from wtforms import StringField
from flask_wtf import FlaskForm

class OthersForm(FlaskForm):
    class Meta:
        csrf = False

        other = StringField("Details of other input")

    def to_bson(self):
        return {
            'other':self.other.data
        }
    def from_bson(self, p):
        self.other.data = p['other']
