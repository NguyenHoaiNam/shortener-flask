from openstack import connection
from openstack import profile


def create_connection(auth_url, region, project_name, username, password,
                      user_domain_id, project_domain_id):
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, region)
    connect_output = connection.Connection(profile=prof,
                                           auth_url=auth_url,
                                           project_name=project_name,
                                           username=username,
                                           password=password,
                                           user_domain_id=user_domain_id,
                                           project_domain_id=project_domain_id)
    return connect_output
