# -*- coding: utf-8 -*-


def list_networks(conn):
    list_nets = []
    for net in conn.network.networks():
        list_nets.append(net)
    return list_nets


def list_ports(conn):
    list_ps = []
    for port in conn.network.ports():
        list_ps.append(port)
    return list_ps


def list_subnets(conn):
    list_subs = []
    for subnet in conn.network.subnets():
        list_subs.append(subnet)
    return list_subs


def list_security_groups(conn):
    list_sgs = []
    for sg in conn.network.security_groups():
        list_sgs.append(sg)
    return list_sgs


def list_routers(conn):
    list_rs = []
    for router in conn.network.routers():
        list_rs.append(router)
    return list_rs
