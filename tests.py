import unittest
import jinja2
from schema_forms import models


class FakeSession:
    def __init__(self):
        self.name = "fakeUser"

def mock_get_flashed_messages(with_categories):
    return None

def mock_url_for(endpoint, **values):
    return "someUrl"

class WidgetTestCase(unittest.TestCase):
    def setUp(self):
        self.path = './templates'
        self.filename = 'dashboard.html'

    def getRendered(self, context):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.path))
        env.globals.update(get_flashed_messages=mock_get_flashed_messages)
        env.globals.update(url_for=mock_url_for)
        rendered = env.get_template(self.filename).render(context)
        return rendered

    # def test_dashboard(self):
    #     context = {  # your variables to pass to template
    #         'test_var': 'test_value'
    #     }

    def test_dashboard_golden_path(self):
        patients = [
            models.Patient_bio_info_Info(123, 123, "someone", "123", "123", "123", "123", "123", "123", "123", "123", "123",
                               "123", "123", "123"),
            models.Patient_bio_info_Info(123, 123, "someoneElse", "123", "123", "123", "123", "123", "123", "123", "123", "123",
                               "123", "123", "123")
        ]
        context = {  # your variables to pass to template
            'patients': patients,
            'session': FakeSession()
        }

        rendered = self.getRendered(context)

        # `rendered` is now a string with rendered template
        # do some asserts on `rendered` string
        assert 'fakeUser' in rendered
        assert 'someone' in rendered
        assert 'someoneElse' in rendered

if __name__ == '__main__':
    unittest.main()

