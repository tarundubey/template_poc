import os
from jinja2 import Environment, PackageLoader, select_autoescape

jinja_env = Environment(
    loader=PackageLoader("template_project"),
    autoescape=select_autoescape()
)


def generate_template(_template, _data):
    return _template.render(_data)


def handle_template_generation(data):
    vs_template = generate_template(
        _template=jinja_env.get_template("terraform_sample_template.jinja2"),
        _data={
            "resource_name": data.get("resource_name"),
            "vs_name": data.get("vs_name"),
            "vs_ip": "10.20.30.40"
        }
    )

    with open(os.getcwd() + "/template_project/output/example.tf", "a") as fd:
        fd.write(vs_template)
