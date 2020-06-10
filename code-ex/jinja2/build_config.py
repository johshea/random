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

    hostname = input("Enter Hostname: ")
    loop0_ip = input("Enter Loopback0 address e.g 1.1.1.1: ")
    loop0_mask = input("Enter Loopback0 mask e.g 255.255.255.255: ")
    snmp_ro = input("Enter SNMP read-only community: ")
    snmp_rw = input("Enter SNMP read-write community: ")
    # render the template with collected variables
    config = template.render(hostname=hostname,
                             loop0_ip=loop0_ip,
                             loop0_mask=loop0_mask,
                             snmp_ro=snmp_ro,
                             snmp_rw=snmp_rw)

    # Save rendered config to new file
    filename = "{}.cfg".format(hostname)
    with open(filename, 'w') as fh:
        fh.write(config)
