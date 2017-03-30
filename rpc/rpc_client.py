import oslo_messaging as om

import conf
from conf.release_mappings import RELEASE_MAPPINGS
from objects.base import UrlObjectSerializer

CONF = conf.CONF

transport = om.get_transport(CONF)
target = om.Target(topic='shortener')


def get_client():
    return om.RPCClient(transport, target)


class TaskClient(object):
    """
    Client side of shortener api for API
    API version history:

        2.0 - Initial version
    """

    def __init__(self):
        upgrade_level = CONF.pin_release
        release_version = RELEASE_MAPPINGS.get(upgrade_level)
        serializer = UrlObjectSerializer()
        version_cap = release_version['rpc']
        self.rpc_client = om.RPCClient(transport, target,
                                       version_cap=version_cap, serializer=serializer)

    def _cast(self, cctx, name, version, **kwargs):
        client = self.rpc_client.prepare(version=version)
        return client.cast(cctx, name, **kwargs)

    def _call(self, cctx, name, version, **kwargs):
        client = self.rpc_client.prepare(version=version)
        return client.call(cctx, name, **kwargs)

    def insert_database(self, record):
        version = 2.0
        return self._call({}, 'insert_database',
                          version=version, record=record.to_dict())

    def query_database(self, short_link):
        version = 2.0
        return self._call({}, 'query_database',
                          version=version, short_link=short_link)
