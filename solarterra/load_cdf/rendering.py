def render_dynamic_field_definition(dynamic_field):
    data_type_instance = getattr(dynamic_field, "data_type_instance", None)
    base_type = data_type_instance.django_field if data_type_instance is not None else "models.TextField"
    storage_mode = getattr(dynamic_field, "storage_mode", "scalar")

    if storage_mode == "array":
        return f"ArrayField({base_type}(blank=True, null=True), blank=True, null=True)"
    return f"{base_type}(blank=True, null=True)"


def build_rendered_fields(dynamic_model):
    rendered_fields = []
    for field in dynamic_model.fields.select_related("data_type_instance").all():
        rendered_fields.append({
            "name": field.field_name,
            "definition": render_dynamic_field_definition(field),
        })
    return rendered_fields
