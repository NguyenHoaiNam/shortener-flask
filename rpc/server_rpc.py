import  json

import oslo_messaging as om

import conf
from app.models import Url
from db_create import engine
from sqlalchemy.orm import sessionmaker


CONF = conf.CONF
transport = om.get_transport(CONF)
target = om.Target(topic='shortener', server="10.164.178.141")


class InteractDB(object):

    def __init__(self):
        self.Session = sessionmaker(bind=engine)
        self.session = self.Session()

    def insert_database(self, cctx, record):
        rc = Url(org_link=record['org_link'],
                 short_link=record['short_link'])
        try:
            self.session.add(rc)
            self.session.commit()
        except Exception as e:
            raise e

    def query_database(self, cctx, short_link):
        origin_link = self.session.query(Url).filter(
            Url.short_link == short_link).one()
        return origin_link.org_link


def main():
    endpoints = [InteractDB(), ]
    # access_policy = om.rpc.dispatcher.DefaultRPCAccessPolicy
    server_rpc = om.get_rpc_server(transport, target,
                                   endpoints, executor='blocking')
    server_rpc.start()
    server_rpc.wait()

##################################################################

