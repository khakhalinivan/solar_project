from types import SimpleNamespace

from django.test import SimpleTestCase

from load_cdf.rendering import build_rendered_fields, render_dynamic_field_definition


class RenderingHelpersTests(SimpleTestCase):
    def test_render_dynamic_field_definition_for_scalar(self):
        field = SimpleNamespace(
            storage_mode="scalar",
            data_type_instance=SimpleNamespace(django_field="models.BigIntegerField"),
        )

        definition = render_dynamic_field_definition(field)

        self.assertEqual(definition, "models.BigIntegerField(blank=True, null=True)")

    def test_render_dynamic_field_definition_for_array(self):
        field = SimpleNamespace(
            storage_mode="array",
            data_type_instance=SimpleNamespace(django_field="Float32Field"),
        )

        definition = render_dynamic_field_definition(field)

        self.assertEqual(
            definition,
            "ArrayField(Float32Field(blank=True, null=True), blank=True, null=True)",
        )

    def test_render_dynamic_field_definition_fallback_type(self):
        field = SimpleNamespace(storage_mode="scalar", data_type_instance=None)

        definition = render_dynamic_field_definition(field)

        self.assertEqual(definition, "models.TextField(blank=True, null=True)")

    def test_build_rendered_fields(self):
        fields = [
            SimpleNamespace(
                field_name="epoch_1",
                storage_mode="scalar",
                data_type_instance=SimpleNamespace(django_field="models.BigIntegerField"),
            ),
            SimpleNamespace(
                field_name="se_1",
                storage_mode="array",
                data_type_instance=SimpleNamespace(django_field="Float32Field"),
            ),
        ]

        class FakeFieldsManager:
            def __init__(self, items):
                self.items = items

            def select_related(self, *_args, **_kwargs):
                return self

            def all(self):
                return self.items

        dynamic_model = SimpleNamespace(fields=FakeFieldsManager(fields))

        rendered = build_rendered_fields(dynamic_model)

        self.assertEqual(rendered[0]["name"], "epoch_1")
        self.assertEqual(
            rendered[0]["definition"],
            "models.BigIntegerField(blank=True, null=True)",
        )
        self.assertEqual(rendered[1]["name"], "se_1")
        self.assertEqual(
            rendered[1]["definition"],
            "ArrayField(Float32Field(blank=True, null=True), blank=True, null=True)",
        )
