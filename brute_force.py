def test_allocation(allocations, data):

    # TODO: 
    return 10.0


def get_services(providers):
    services_list = []
    for p in providers:
        name = p['name']
        for r in p['regions']:
            services_list.append( {'provider': name, **r} )
    return services_list

def satisfy_project(allocation, project):
    units = list(project['units'])
    for service in allocation:
        units = [ total - allocated * service['allocated'] for total, allocated in zip(units, service['units'])]
    ok = [u < 0 for u in units]
    return all(ok)

def generate_allocation_project(project, services):
    good_allocatios = []
    def tree_explorer(allocation, project, good_allocatios):
        for idx, service in enumerate(allocation):
            allocation = list(allocation)
            allocation[idx]['allocated'] += 1
            if allocation[idx]['allocated'] < allocation[idx]['pkgs']:
                if satisfy_project(allocation, project):
                    good_allocatios.append(allocation)
                else:
                    tree_explorer(allocation, project, good_allocatios)
    
    allocation = []
    for idx, service in enumerate(services):
        allocation.append({'allocated': 0, **service})
    
    tree_explorer(allocation, project, good_allocatios)

    return good_allocatios

def generate_allocations(projects, services):
    gas = []
    for project in projects:
        gas.append(generate_allocation_project(project, services))

    return gas
    


from parsing import parse_file

if __name__ == '__main__':
    data = parse_file('inputs/test.in')
    print('-----', type(data))
    projects = data['projects']
    providers = data['providers']
    services = get_services(providers)
    gal = generate_allocations(projects, services)
    print('----', gal)