from jinja2 import Environment, FileSystemLoader
env = Environment(loader = FileSystemLoader('templates'))
template = env.get_template('end_date_state.jinja')
output = template.render()

with open("renders/end_date_state_rendered.txt", 'w') as f:
    print(output, file = f)