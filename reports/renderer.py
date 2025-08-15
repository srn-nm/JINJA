from jinja2 import Environment, FileSystemLoader
import os

template_dir = os.path.dirname(os.path.abspath(__file__))

env = Environment(loader=FileSystemLoader(template_dir))

template = env.get_template("1.j2")

data = {}

output = template.render(data)

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(output)