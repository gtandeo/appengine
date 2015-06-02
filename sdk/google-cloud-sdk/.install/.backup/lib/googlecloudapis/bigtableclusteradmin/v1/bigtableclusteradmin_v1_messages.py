"""Generated message classes for bigtableclusteradmin version v1.

This is a OnePlatform service.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages

from googlecloudapis.apitools.base.py import encoding


package = 'bigtableclusteradmin'


class BigtableclusteradminOperationsCancelRequest(messages.Message):
  """A BigtableclusteradminOperationsCancelRequest object.

  Fields:
    cancelOperationRequest: A CancelOperationRequest resource to be passed as
      the request body.
    name: A string attribute.
  """

  cancelOperationRequest = messages.MessageField('CancelOperationRequest', 1)
  name = messages.StringField(2, required=True)


class BigtableclusteradminOperationsDeleteRequest(messages.Message):
  """A BigtableclusteradminOperationsDeleteRequest object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1, required=True)


class BigtableclusteradminOperationsGetRequest(messages.Message):
  """A BigtableclusteradminOperationsGetRequest object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1, required=True)


class BigtableclusteradminOperationsListRequest(messages.Message):
  """A BigtableclusteradminOperationsListRequest object.

  Fields:
    filter: A string attribute.
    name: A string attribute.
    pageSize: A integer attribute.
    pageToken: A string attribute.
  """

  filter = messages.StringField(1)
  name = messages.StringField(2, required=True)
  pageSize = messages.IntegerField(3, variant=messages.Variant.INT32)
  pageToken = messages.StringField(4)


class BigtableclusteradminProjectsAggregatedClustersListRequest(messages.Message):
  """A BigtableclusteradminProjectsAggregatedClustersListRequest object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesClustersDeleteRequest(messages.Message):
  """A BigtableclusteradminProjectsZonesClustersDeleteRequest object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesClustersGetRequest(messages.Message):
  """A BigtableclusteradminProjectsZonesClustersGetRequest object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesClustersUndeleteRequest(messages.Message):
  """A BigtableclusteradminProjectsZonesClustersUndeleteRequest object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1, required=True)


class BigtableclusteradminProjectsZonesListRequest(messages.Message):
  """A BigtableclusteradminProjectsZonesListRequest object.

  Fields:
    name: A string attribute.
  """

  name = messages.StringField(1, required=True)


class CancelOperationRequest(messages.Message):
  """A CancelOperationRequest object."""


class Cluster(messages.Message):
  """A Cluster object.

  Fields:
    currentOperation: A Operation attribute.
    deleteTime: A string attribute.
    displayName: A string attribute.
    hddBytes: A string attribute.
    name: A string attribute.
    serveNodes: A integer attribute.
    ssdBytes: A string attribute.
  """

  currentOperation = messages.MessageField('Operation', 1)
  deleteTime = messages.StringField(2)
  displayName = messages.StringField(3)
  hddBytes = messages.IntegerField(4)
  name = messages.StringField(5)
  serveNodes = messages.IntegerField(6, variant=messages.Variant.INT32)
  ssdBytes = messages.IntegerField(7)


class CreateClusterRequest(messages.Message):
  """A CreateClusterRequest object.

  Fields:
    cluster: A Cluster attribute.
    clusterId: A string attribute.
    name: A string attribute.
  """

  cluster = messages.MessageField('Cluster', 1)
  clusterId = messages.StringField(2)
  name = messages.StringField(3)


class Empty(messages.Message):
  """A Empty object."""


class ListClustersResponse(messages.Message):
  """A ListClustersResponse object.

  Fields:
    clusters: A Cluster attribute.
    failedZones: A Zone attribute.
  """

  clusters = messages.MessageField('Cluster', 1, repeated=True)
  failedZones = messages.MessageField('Zone', 2, repeated=True)


class ListOperationsResponse(messages.Message):
  """A ListOperationsResponse object.

  Fields:
    nextPageToken: A string attribute.
    operations: A Operation attribute.
  """

  nextPageToken = messages.StringField(1)
  operations = messages.MessageField('Operation', 2, repeated=True)


class ListZonesResponse(messages.Message):
  """A ListZonesResponse object.

  Fields:
    zones: A Zone attribute.
  """

  zones = messages.MessageField('Zone', 1, repeated=True)


class Operation(messages.Message):
  """A Operation object.

  Messages:
    MetadataValue: A MetadataValue object.
    ResponseValue: A ResponseValue object.

  Fields:
    done: A boolean attribute.
    error: A Status attribute.
    metadata: A MetadataValue attribute.
    name: A string attribute.
    response: A ResponseValue attribute.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class MetadataValue(messages.Message):
    """A MetadataValue object.

    Messages:
      AdditionalProperty: An additional property for a MetadataValue object.

    Fields:
      additionalProperties: Additional properties of type MetadataValue
    """

    class AdditionalProperty(messages.Message):
      """An additional property for a MetadataValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = messages.StringField(1)
      value = messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = messages.MessageField('AdditionalProperty', 1, repeated=True)

  @encoding.MapUnrecognizedFields('additionalProperties')
  class ResponseValue(messages.Message):
    """A ResponseValue object.

    Messages:
      AdditionalProperty: An additional property for a ResponseValue object.

    Fields:
      additionalProperties: Additional properties of type ResponseValue
    """

    class AdditionalProperty(messages.Message):
      """An additional property for a ResponseValue object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = messages.StringField(1)
      value = messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = messages.MessageField('AdditionalProperty', 1, repeated=True)

  done = messages.BooleanField(1)
  error = messages.MessageField('Status', 2)
  metadata = messages.MessageField('MetadataValue', 3)
  name = messages.StringField(4)
  response = messages.MessageField('ResponseValue', 5)


class StandardQueryParameters(messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    AltValueValuesEnum: Data format for the response.

  Fields:
    alt: Data format for the response.
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters. Overrides userIp if both are provided.
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
    userIp: IP address of the site where the request originates. Use this if
      you want to enforce per-user limits.
  """

  class AltValueValuesEnum(messages.Enum):
    """Data format for the response.

    Values:
      json: Responses with Content-Type of application/json
    """
    json = 0

  alt = messages.EnumField('AltValueValuesEnum', 1, default=u'json')
  fields = messages.StringField(2)
  key = messages.StringField(3)
  oauth_token = messages.StringField(4)
  prettyPrint = messages.BooleanField(5, default=True)
  quotaUser = messages.StringField(6)
  trace = messages.StringField(7)
  userIp = messages.StringField(8)


class Status(messages.Message):
  """A Status object.

  Messages:
    DetailsValueListEntry: A DetailsValueListEntry object.

  Fields:
    code: A integer attribute.
    details: A DetailsValueListEntry attribute.
    message: A string attribute.
  """

  @encoding.MapUnrecognizedFields('additionalProperties')
  class DetailsValueListEntry(messages.Message):
    """A DetailsValueListEntry object.

    Messages:
      AdditionalProperty: An additional property for a DetailsValueListEntry
        object.

    Fields:
      additionalProperties: Additional properties of type
        DetailsValueListEntry
    """

    class AdditionalProperty(messages.Message):
      """An additional property for a DetailsValueListEntry object.

      Fields:
        key: Name of the additional property.
        value: A extra_types.JsonValue attribute.
      """

      key = messages.StringField(1)
      value = messages.MessageField('extra_types.JsonValue', 2)

    additionalProperties = messages.MessageField('AdditionalProperty', 1, repeated=True)

  code = messages.IntegerField(1, variant=messages.Variant.INT32)
  details = messages.MessageField('DetailsValueListEntry', 2, repeated=True)
  message = messages.StringField(3)


class Zone(messages.Message):
  """A Zone object.

  Enums:
    StatusValueValuesEnum:

  Fields:
    displayName: A string attribute.
    name: A string attribute.
    status: A StatusValueValuesEnum attribute.
  """

  class StatusValueValuesEnum(messages.Enum):
    """StatusValueValuesEnum enum type.

    Values:
      EMERGENCY_MAINENANCE: <no description>
      OK: <no description>
      PLANNED_MAINTENANCE: <no description>
      UNKNOWN: <no description>
    """
    EMERGENCY_MAINENANCE = 0
    OK = 1
    PLANNED_MAINTENANCE = 2
    UNKNOWN = 3

  displayName = messages.StringField(1)
  name = messages.StringField(2)
  status = messages.EnumField('StatusValueValuesEnum', 3)


