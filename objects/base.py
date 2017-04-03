"""
This is testing module with O.VO base objects
"""
from oslo_versionedobjects import base as ovoo_base, fields
from oslo_utils import versionutils
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from app.models import Url
import config

URL_OPTIONAL_ATTRS = []
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)
db_api = Session()

class BaseUrlObject(ovoo_base.VersionedObject, ovoo_base.VersionedObjectDictCompat):
    # OBJ_SERIAL_NAMESPACE = 'test_amqp'
    OBJ_PROJECT_NAMESPACE = 'test'


@ovoo_base.VersionedObjectRegistry.register
class UrlObject(BaseUrlObject):
    # Version 1.0: Init version
    VERSION = '1.0'

    fields = {
        'id': fields.IntegerField(),
        'org_link': fields.StringField(nullable=True),
        'short_link': fields.StringField(nullable=True),
        'foo': fields.StringField(nullable=True),
    }

    def __init__(self, *args, **kwargs):
        super(UrlObject, self).__init__(*args, **kwargs)

    def obj_make_compatible(self, primitive, target_version):
        super(UrlObject, self).obj_make_compatible(primitive, target_version)
        target_version = versionutils.convert_version_to_tuple(target_version)
        if target_version < (1, 0) and 'device_metadata' in primitive:
            pass

    @ovoo_base.remotable
    def create(self, context):
        """
        Connect with db and do something
        :return:
        """
        rc = Url(org_link=self.org_link,
                 short_link=self.short_link)
        try:
            db_api.add(rc)
            db_api.commit()
        except Exception as e:
            raise e

    @ovoo_base.remotable
    def save(self, context):
        """
        Connect with db and do something
        :param context:
        :return:
        """
        pass

    @ovoo_base.remotable
    def get_from_short_link(self, context):
        origin_link = db_api.query(Url).filter(
            Url.short_link == self.short_link).one()
        self.org_link = origin_link.org_link

    def obj_load_attr(self, attrname):
        """
        # NOTE(daidv): Nothing for lazy-loaded right now
        :param attrname:
        :return:
        """
        pass

class UrlObjectSerializer(ovoo_base.VersionedObjectSerializer):
    """Url serializer."""
    OBJ_BASE_CLASS = UrlObject
