import sys
sys.setrecursionlimit(50000)


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
    good_allocations = {
        'score': -100000,
        'allocation': None
    }
    
    def tree_explorer(allocation, project, good_allocation):
        for idx, service in enumerate(allocation):
            allocation = list(allocation)
            allocation[idx]['allocated'] += 1
            if allocation[idx]['allocated'] < allocation[idx]['pkgs']:
                if satisfy_project(allocation, project):
                    score = test_allocation(allocation, data)
                    if score > good_allocation['score']:
                        good_allocation['score'] = score
                        good_allocation['allocation'] = allocation
                else:
                    tree_explorer(allocation, project, good_allocation)

    allocation = []
    for idx, service in enumerate(services):
        allocation.append({'allocated': 0, **service})
    
    tree_explorer(allocation, project, good_allocations)
    return good_allocations

def generate_allocations(projects, services):
    gas = []
    for project in projects:
        gas.append(generate_allocation_project(project, services))
    return gas
    
def generate_output(allocations, data):
    for allocation in allocations:
        output_list = []
        for a in allocation['allocation']:
            names = [p["name"] for p in data['providers']]
            privider = a['provider']
            regions = [p for p in data['providers'] if p['name'] == privider][0]['regions']
            rnames = [r['name'] for r in regions]
            idx, n, allocated =  (names.index(a['provider']), rnames.index(a['name']), a['allocated'])
            output_list.append(str(idx))
            output_list.append(str(n))
            output_list.append(str(allocated))
        print(' '.join(output_list))


from parsing import parse_file

if __name__ == '__main__':
    data = parse_file('inputs/test.in')
    projects = data['projects']
    providers = data['providers']
    services = get_services(providers)
    gal = generate_allocations(projects, services)
    print('----', gal)
