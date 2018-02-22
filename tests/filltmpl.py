import os
import sys

from jinja2 import Template

dir_path = os.path.dirname(os.path.realpath(__file__))


if __name__ == '__main__':
    image_tag = sys.argv[1]
    template = Template(
        open(os.path.join(dir_path, 'templates', 'Dockerfile.j2')).read()
    )
    dockerfile = template.render({'image_tag': image_tag})

    with open(os.path.join(dir_path, 'Dockerfile.{}'.format(image_tag)), 'w') as fh:
        fh.write(dockerfile)
