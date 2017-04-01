import oslo_messaging as om
import conf
import config

from app.models import Url

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from objects.base import UrlObjectSerializer


CONF = conf.CONF
transport = om.get_transport(CONF)
RPC_API_VERSION = '1.9'
target = om.Target(topic='shortener', server='shortener')


engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)


class InteractDB(object):
    """
    Server side of shortener for API
    """
    target = om.Target(version=RPC_API_VERSION)

    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def insert_database(self, cctx, record):
        if type(record) is dict:
            rc = Url(org_link=record['org_link'],
                     short_link=record['short_link'])
            try:
                self.session.add(rc)
                self.session.commit()
            except Exception as e:
                raise e
        else:
            record.create(cctx)

    def query_database(self, cctx, **karg):
        short_link = karg.pop('short_link', None)
        record = karg.pop('record', None)
        if short_link:
            # backward compatible with Newton release
            origin_link = self.session.query(Url).filter(
                Url.short_link == short_link).one()
            return {
                'org_link': origin_link.org_link
            }
        else:
            record.get_from_short_link(cctx)
            return record


def main():
    endpoints = [InteractDB(), ]
    serializer = UrlObjectSerializer()
    server_rpc = om.get_rpc_server(transport, target,
                                   endpoints, serializer=serializer,
                                   executor='blocking')
    server_rpc.start()
    server_rpc.wait()
