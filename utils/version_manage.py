# -*- coding: utf-8 -*-
from oslo_utils import versionutils

from conf.release_mappings import *


def get_rpc_version(release):
    """
    Return RPC version for special release
    :param release: String
    :return: version as a tuple ( , )
    """
    version = RELEASE_MAPPINGS[release]['rpc']
    return versionutils.convert_version_to_tuple(version)

def get_object_version(release, class_name):
    """
    Return object version for special release
    :param release: String
    :param class_name: String
    :return: version as a tuple ( , )
    """
    version = RELEASE_MAPPINGS[release]['objects'][class_name]
    return versionutils.convert_version_to_tuple(version)
