
def group(lst, n):
    """group([0,3,4,10,2,3], 2) => [(0,3), (4,10), (2,3)]
    
    Group a list into consecutive n-tuples. Incomplete tuples are
    discarded e.g.
    
    >>> group(range(10), 3)
    [(0, 1, 2), (3, 4, 5), (6, 7, 8)]
    """
    return zip(*[lst[i::n] for i in range(n)]) 

def parse_region(reg):
    parse = reg[1].split()

    region = {
        'name': reg[0],
        'pkgs': int(parse[0]),
        'cost': float(parse[1]),
        'units': [int(x) for x in parse[2:]],
        'latencies': [int(x) for x in reg[2].split()]
    }
    return region

def parse_service(lines):
    parse = lines[0].split()
    name = parse[0]
    n_region = int(parse[1])
    service = {
        'name': name,
        'regions': []
        }
    lines = lines[1:]
    reg_tutles = group(lines[: 3*n_region], 3)
    for reg in reg_tutles:
        service['regions'].append(parse_region(reg))

    lines = lines[3*n_region:]
    return service, lines

def parse_project(line):
    parse = line.split()
    project = {
        'penalty': int(parse[0]),
        'country': parse[1],
        'units': [int(u) for u in parse[2]]
    }
    return project

def parse_file(filename):
    n_providers = 0
    n_services = 0
    n_contries = 0
    n_projects = 0
    data= {
        'nums': [],
        'prividers': [],
        'services': [],
        'contries': [],
        'projects': [],
    }
    with open(filename) as f:
        lines =  [l.strip() for l in f.readlines()]
    n_providers, n_services, n_contries, n_projects = (int(x) for x in lines[0].split())
    data['nums'] = [n_providers, n_services, n_contries, n_projects]
    data["services"] = lines[1].split()
    data["contries"] = lines[2].split()

    lines = lines[3:]
    services = {}
    for _ in range(n_services):
        service, lines = parse_service(lines)

    for line in lines:
        project = parse_project(line)
        data["projects"].append(project)
    return data

if __name__ == '__main__':
    import pprint
    pp = pprint.PrettyPrinter(indent=4)
    data = parse_file('./inputs/test.in')
    # pp.pprint(data)

    ps = data['projects']
    assert len(ps) == 5
    ps[0]['country'] == 'Italy'
    ps[1]['country'] == 'Spain'
    