# Include the jinja2 library
import os
import jinja2


# creating the jinja environment variable for locating and loading the template files
template_dir = os.path.join(os.path.dirname(__file__), 'template')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),
                               autoescape=True)


# rendering the page
page = jinja_env.get_template('addswitch.html')
self.response.out.write(page.render(user=user))
