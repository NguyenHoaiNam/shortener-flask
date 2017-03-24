import oslo_messaging as om
import conf
from app.models import Url


CONF = conf.CONF
transport = om.get_transport(CONF)
target = om.Target(topic='shortener', server='10.164.180.110')


class InteractDB(object):
    def insert_database(self, cctx, record):
        try:
            cctx.add(record)
            cctx.commit()
        except Exception as e:
            raise e

    def querry_database(self, cctx, short_link):
        origin_link = cctx.query(Url).filter(
            Url.short_link == short_link).one()
        return origin_link.org_link


def main():
    endpoints = [InteractDB(), ]
    access_policy = om.rpc.dispatcher.DefaultRPCAccessPolicy
    server_rpc = om.get_rpc_server(transport, target, endpoints,
                                   executor='eventlet',
                                   access_policy=access_policy)
    server_rpc.start()
    server_rpc.wait()

