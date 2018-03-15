def average_project_latency(latencies, packages):
    lats = []
    tot_units = []
    for provider, latency in latencies.items():
        for pkg, units in packages[provider]:
            pkg_units = pkg * sum(units)
            lats.append(latency * pkg_units)
            tot_units.append(pkg_units)

    if not tot_units:
        return 0

    return sum(lats) / sum(tot_units)


def service_availability_index(units):
    if not units:
        return 0
    return (sum(units) ** 2) / sum([u ** 2 for u in units])


def overall_availability_index(service_units):
    indexes = []
    for unit in service_units:
        indexes.append(service_availability_index(unit))
    if not indexes:
        return 0
    return sum(indexes) / len(indexes)


def sla_penalty(base_project_penalty, units_needed, allocated_units):
    if not units_needed:
        return 0
    return (
        base_project_penalty *
        ((allocated_units - min(units_needed, allocated_units)) / allocated_units)
    )


def total_sla_penalty(base_penalty, needed_units, service_units):
    slas = []
    for allocated in service_units:
        slas.append(sla_penalty(base_penalty, needed_units, sum(allocated)))
    if not slas:
        return 0
    return sum(slas) / len(slas)


def total_project_cost(packages_fees):
    return sum([num * fee for num, fee in packages_fees])


def project_score(base_penalty, needed_units, service_units, packages_fees,
        latencies, packages):
    return (
        10 ** 9 /
        (
            total_project_cost(packages_fees) *
            average_project_latency(latencies, packages) /
            max(1, overall_availability_index(service_units)) + 
            total_sla_penalty(base_penalty, needed_units, service_units)
        )
    )


if __name__ == '__main__':
    latencies = {
        '1': 50,
        '2': 90,
        '3': 80,
        '4': 35,
        '5': 48,
    }
    packages = {
        '1': [
            (1, [960]),
        ],
        '2': [
            (1, [165]),
        ],
        '3': [
            (1, [352]),
        ],
        '4': [
            (1, [640]),
        ],
        '5': [
            (1, [500]),
        ],
    }

    assert int(average_project_latency(latencies, packages)) == int(52.51)

    units = [30, 70]
    assert service_availability_index(units) == 10000 / (900 + 4900)

    service_units = [[600, 15, 96, 40, 250], [300, 50, 64, 100, 250], [60, 100, 192, 500]]
    assert int(overall_availability_index(service_units)) == int(2.73)

    packages_fees = [(60, 0.32), (1, 0.7), (8, 1.5), (1, 1.5), (10, 1)]
    assert total_project_cost(packages_fees) == 43.4

    assert total_sla_penalty(base_penalty=10000, needed_units=1001, service_units=service_units) == 0, total_sla_penalty(base_penalty=10000, needed_units=1001, service_units=service_units)

    score = project_score(10000, 1001, service_units, packages_fees, latencies, packages)
    assert int(score) == int(1196396.13)
