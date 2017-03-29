"""
This is testing module with O.VO base objects
"""
from oslo_versionedobjects import base as ovoo_base, fields
from oslo_utils import versionutils


URL_OPTIONAL_ATTRS = []

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
    def create(self):
        """
        Connect with db and do something
        :return:
        """
        pass

    @ovoo_base.remotable
    def save(self, context):
        """
        Connect with db and do something
        :param context:
        :return:
        """
        pass

    def obj_load_attr(self, attrname):
        """
        # NOTE(daidv): Nothing for lazy-loaded right now
        :param attrname:
        :return:
        """
        pass
