from django.test import TestCase, override_settings
from django.urls import reverse

@override_settings(ROOT_URLCONF='django_dynamic_path.tests.urls')
class DynamicPathTestCase(TestCase):
    def test_normal_path_before_dynamic_returns_correct_response(self):
        r = self.client.get('/path_before/')
        self.assertEqual(r.content, b'path before')
    def test_normal_path_after_dynamic_returns_correct_response(self):
        r = self.client.get('/path_after/')
        self.assertEqual(r.content, b'path after')

    def test_dynamic_path_returns_expected_response(self):
        r = self.client.get('/bar/')
        self.assertEqual(r.content, b'bar from dynamic')

    def test_dynamic_path_func_receives_correct_args(self):
        r = self.client.get('/baz/')
        self.assertEqual(r.status_code, 200)

    def test_included_dynamic_path_func_receives_correct_args(self):
        r = self.client.get('/included/baz/')
        self.assertEqual(r.status_code, 200)

    def test_path_before_can_be_reversed(self):
        self.assertEqual(reverse('path_before_name'), '/path_before/')
    def test_path_after_with_params_can_be_reversed(self):
        self.assertEqual(reverse('path_after_name', kwargs=dict(value='BAZ')), '/path_after/BAZ/')
