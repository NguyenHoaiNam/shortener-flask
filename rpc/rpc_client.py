import oslo_messaging as om

import conf
from conf.release_mappings import RELEASE_MAPPINGS
from objects.base import UrlObjectSerializer

CONF = conf.CONF
RPC_API_VERSION = '2.0'
transport = om.get_transport(CONF)
target = om.Target(topic='shortener', version=RPC_API_VERSION)


def get_client(version_cap, serializer):
    return om.RPCClient(transport, target, version_cap=version_cap,
                        serializer=serializer)


class TaskClient(object):
    """
    Client side of shortener api for API
    API version history:

        2.0 - Initial version
    """
    def __init__(self):
        upgrade_level = CONF.pin_release
        release_version = RELEASE_MAPPINGS.get(upgrade_level)
        if release_version:
            release_version = RELEASE_MAPPINGS.get(upgrade_level)
            version_cap = release_version['rpc']
        else:
            version_cap = None
        serializer = UrlObjectSerializer()
        self.client = get_client(version_cap, serializer)

    def insert_database(self, record):
        version = '2.0'
        cctx = self.client.prepare(version=version)
        return cctx.cast({}, 'insert_database', record=record)

    def query_database(self, record):
        version = '2.0'
        cctx = self.client.prepare(version=version)
        return cctx.call({}, 'query_database', record=record)
