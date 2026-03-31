from django.test import SimpleTestCase

from pages.forms import SourceForm


class SourceFormTests(SimpleTestCase):
    def test_missing_required_fields_does_not_crash(self):
        form = SourceForm(data={}, load_sources_queryset=False)

        self.assertFalse(form.is_valid())
        self.assertIn("sources", form.errors)
        self.assertIn("ts_start", form.errors)
        self.assertIn("ts_end", form.errors)

    def test_invalid_range_adds_non_field_error(self):
        data = {
            "ts_start": "2013-01-02 00:00:00",
            "ts_end": "2013-01-01 00:00:00",
        }
        form = SourceForm(data=data, load_sources_queryset=False)

        self.assertFalse(form.is_valid())
        self.assertTrue(form.non_field_errors())
        self.assertIn("Start time should be before end time.", form.non_field_errors())

    def test_valid_range_does_not_add_non_field_error(self):
        data = {
            "ts_start": "2013-01-01 00:00:00",
            "ts_end": "2013-01-02 00:00:00",
        }
        form = SourceForm(data=data, load_sources_queryset=False)

        self.assertFalse(form.is_valid())  # still missing required `sources`
        self.assertEqual(list(form.non_field_errors()), [])
