import unittest
import jinja2
from schema_forms.models import MammographyInfo
from schema_forms.mammo_form import MammographyForm

class FakeSession:
    def __init__(self):
        self.name = "fakeUser"

def mock_get_flashed_messages(with_categories):
    return None

def mock_url_for(endpoint, **values):
    return "someUrl"

class MammoTestCase(unittest.TestCase):
    def setUp(self):
        self.path = './templates'
        self.filename = 'dashboard.html'

        self.test_model = MammographyInfo(folder_number="some number", mammo_location="some location",
             mammo_details='mammo_details', mammo_date='mammo_date',
             mammo_accesion='mammo_accesion', mammo_number='mammo_number',
             mammo_report_previous='mammo_report_previous',mammo_breast_density='mammo_breast_density',
             mammo_mass_present='mammo_mass_present',mammo_mass_number='mammo_mass_number',
             mammo_mass_location_right_breast='mammo_mass_location_right_breast',
             mammo_mass_location_left_breast='mammo_mass_location_left_breast',
             mammo_mass_depth='mammo_mass_depth',mammo_mass_dist='mammo_mass_dist',
             mammo_mass_pect='mammo_mass_pect',mammo_mass_shape='mammo_mass_shape',
             mammo_mass_margin='mammo_mass_margin', mammo_mass_density='mammo_mass_density',
             mammo_calcification_present='mammo_calcification_present', mammo_calc_number='mammo_calc_number',
             mammo_calc_location_right_breast='mammo_calc_location_right_breast', mammo_calc_location_left_breast='mammo_calc_location_left_breast', 
             mammo_calc_depth='mammo_calc_depth',mammo_calc_dist='mammo_calc_dist', mammo_calcification_type='mammo_calcification_type',
             mammo_calcification_diagnosis='mammo_calcification_diagnosis', mammo_arch_present='mammo_arch_present',
             mammo_arch_location_right_breast='mammo_arch_location_right_breast',
             mammo_arch_location_left_breast='mammo_arch_location_left_breast', mammo_arch_depth='mammo_arch_depth',mammo_arch_dist='mammo_arch_dist',mammo_assym_present='mammo_assym_present',
             mammo_assym_location_right_breast='mammo_assym_location_right_breast',
             mammo_assym_location_left_breast='mammo_assym_location_left_breast',
             mammo_assym_depth='mammo_assym_depth', mammo_assym_type_right_breast='mammo_assym_type_right_breast',
             mammo_assym_type_left_breast='mammo_assym_type_left_breast',
             mammo_intra_mammary_lymph_nodes_present='mammo_intra_mammary_lymph_nodes_present',
             mammo_intra_mammary_lymph_nodes_description='mammo_intra_mammary_lymph_nodes_description',
             mammo_lesion='mammo_lesion',mammo_lesion_right_breast='mammo_lesion_right_breast',
             mammo_lesion_left_breast='mammo_lesion_left_breast',mammo_asso_feature_skin_retraction='mammo_asso_feature_skin_retraction', 
             mammo_asso_feature_nipple_retraction='mammo_asso_feature_nipple_retraction', mammo_asso_feature_skin_thickening='mammo_asso_feature_skin_thickening', 
             mammo_asso_feature_trabecular_thickening='mammo_asso_feature_trabecular_thickening', 
             mammo_asso_feature_axillary_adenopathy='mammo_asso_feature_axillary_adenopathy', 
             mammo_asso_feature_architectural_distortion='mammo_asso_feature_architectural_distortion', 
             mammo_asso_feature_calicifications='mammo_asso_feature_calicifications', mammo_birad='mammo_birad'
        )

    def getRendered(self, context):
        env = jinja2.Environment(loader=jinja2.FileSystemLoader(self.path))
        env.globals.update(get_flashed_messages=mock_get_flashed_messages)
        env.globals.update(url_for=mock_url_for)
        rendered = env.get_template(self.filename).render(context)
        return rendered

    def test_from_model(self):
        form = MammographyForm()
        form.from_model(self.test_model)
        self.assertEqual(form.folder_number.data, self.test_model.folder_number, "exepected equal values")

    def test_to_model(self):
        form = MammographyForm()
        form.from_model(self.test_model)
        form.mammo_arch_depth.data = "amazing edited value"
        new_model = form.to_model()
        self.assertEqual(new_model.folder_number, self.test_model.folder_number, "exepected equal values")
        self.assertEqual(new_model.mammo_arch_depth, "amazing edited value")

    # def test_dashboard_golden_path(self):
    #     patients = [
    #         models.Patient_bio_info_Info(123, 123, "someone", "123", "123", "123", "123", "123", "123", "123", "123", "123",
    #                            "123", "123", "123"),
    #         models.Patient_bio_info_Info(123, 123, "someoneElse", "123", "123", "123", "123", "123", "123", "123", "123", "123",
    #                            "123", "123", "123")
    #     ]
    #     context = {  # your variables to pass to template
    #         'patients': patients,
    #         'session': FakeSession()
    #     }

    #     rendered = self.getRendered(context)

    #     # `rendered` is now a string with rendered template
    #     # do some asserts on `rendered` string
    #     assert 'fakeUser' in rendered
    #     assert 'someone' in rendered
    #     assert 'someoneElse' in rendered

if __name__ == '__main__':
    unittest.main()