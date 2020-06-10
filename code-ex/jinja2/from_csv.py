import csv
from jinja2 import Environment, FileSystemLoader

# python2 and python3 compatibility
try:
    input = raw_input
except NameError:
    pass


if __name__ == "__main__":

    # where to find templates
    env = Environment(loader=FileSystemLoader('./templates'))

    # select a template
    template = env.get_template('standard_router.cfg')

    # prompt user for variables
    f = open('devices.csv')
    devices = csv.DictReader(f)

    for device in devices:
        # device is now an OrderedDict that can be passed as args directly
        # to template
        config = template.render(**device)

        # Save rendered config to new file
        hostname = device['hostname']
        filename = "{}.cfg".format(hostname)
        with open(filename, 'w') as fh:
            fh.write(config)
