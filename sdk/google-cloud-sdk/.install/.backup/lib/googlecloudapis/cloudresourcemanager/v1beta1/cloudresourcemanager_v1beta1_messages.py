"""Generated message classes for cloudresourcemanager version v1beta1.

The Google Cloud Resource Manager API provides methods for creating, reading,
and updating of project metadata, including IAM policies, and will shortly
provide the same for other high-level entities (e.g. customers and resource
groups). Longer term, we expect the cloudresourcemanager API to encompass
other Cloud resources as well.
"""
# NOTE: This file is autogenerated and should not be edited by hand.

from protorpc import messages

from googlecloudapis.apitools.base.py import encoding


package = 'cloudresourcemanager'


class CloudresourcemanagerProjectsDeleteRequest(messages.Message):
  """A CloudresourcemanagerProjectsDeleteRequest object.

  Fields:
    projectId: The project ID (for example, `foo-bar-123`).  Required.
  """

  projectId = messages.StringField(1, required=True)


class CloudresourcemanagerProjectsGetRequest(messages.Message):
  """A CloudresourcemanagerProjectsGetRequest object.

  Fields:
    projectId: The project ID (for example, `my-project-123`).  Required.
  """

  projectId = messages.StringField(1, required=True)


class CloudresourcemanagerProjectsListRequest(messages.Message):
  """A CloudresourcemanagerProjectsListRequest object.

  Fields:
    filter: An expression for filtering the results of the request.  Filter
      rules are case insensitive. The fields eligible for filtering are:
      name   id   labels.<key> where <key> is a the name of a label  Examples:
      name:*          ==> The project has a name.   name:Howl       ==> The
      project\u2019s name is `Howl` or 'howl'.   name:HOWL       ==> Equivalent to
      above.   NAME:howl       ==> Equivalent to above.   labels.color:*   ==>
      The project has the label "color".   labels.color:red ==> The project\u2019s
      label `color` has the value `red`.   labels.color:red label.size:big ==>
      The project's label `color` has the value `red` and its label     `size`
      has the value `big`.  Optional.
    pageSize: The maximum number of Projects to return in the response. The
      server can return fewer projects than requested. If unspecified, server
      picks an appropriate default.  Note: pagination is not yet supported;
      the server ignores this field.  Optional.
    pageToken: A pagination token returned from a previous call to ListProject
      that indicates from where listing should continue.  Note: pagination is
      not yet supported; the server ignores this field.  Optional.
  """

  filter = messages.StringField(1)
  pageSize = messages.IntegerField(2, variant=messages.Variant.INT32)
  pageToken = messages.StringField(3)


class CloudresourcemanagerProjectsUndeleteRequest(messages.Message):
  """A CloudresourcemanagerProjectsUndeleteRequest object.

  Fields:
    projectId: The project ID (for example, `foo-bar-123`).  Required.
  """

  projectId = messages.StringField(1, required=True)


class Empty(messages.Message):
  """A generic empty message that you can re-use to avoid defining duplicated
  empty messages in your APIs. A typical example is to use it as the request
  or the response type of an API method. For instance:      service Foo {
  rpc Bar(google.protobuf.Empty) returns (google.protobuf.Empty);     }
  """



class ListProjectsResponse(messages.Message):
  """A page of the response received from the
  [ListProjects][cloudresourcemanager.projects.v1beta1.Projects.ListProjects]
  method.  A paginated response where more pages are available has
  `next_page_token` set. This token can be used in a subsequent request to
  retrieve the next request page.

  Fields:
    nextPageToken: Pagination token.  If the result set is too large to fit in
      a single response, this token is returned. It encodes the position of
      the current result cursor. Feeding this value into a new list request
      with the `page_token` parameter gives the next page of the results.
      When `next_page_token` is not filled in, there is no next page and the
      list returned is the last page in the result set.  Pagination tokens
      have a limited lifetime.  Note: pagination is not yet supported; the
      server will not set this field.
    projects: The list of projects that matched the list filter. This list can
      be paginated.
  """

  nextPageToken = messages.StringField(1)
  projects = messages.MessageField('Project', 2, repeated=True)


class Project(messages.Message):
  """A Project is a high-level Google Cloud Platform entity.  It is a
  container for ACLs, APIs, AppEngine Apps, VMs, and other Google Cloud
  Platform resources.  Projects are subordinate to Customers.

  Enums:
    LifecycleStateValueValuesEnum: The project lifecycle state.  Read-only.

  Messages:
    LabelsValue: The labels associated with this project.  Label keys must be
      between 1 and 63 characters long and must conform to the following
      regular expression: [a-z]([-a-z0-9]*[a-z0-9])?.  Label values must be
      between 0 and 63 characters long and must conform to the regular
      expression ([a-z]([-a-z0-9]*[a-z0-9])?)?.  No more than 256 labels can
      be associated with a given resource.  Note that additional character may
      be included in labels in the future. Clients should store labels in a
      representation such as JSON that does not depend on specific characters
      being disallowed.  Example: "environment" : "dev"  Read-write.

  Fields:
    createTime: Creation time.  Read-only.
    labels: The labels associated with this project.  Label keys must be
      between 1 and 63 characters long and must conform to the following
      regular expression: [a-z]([-a-z0-9]*[a-z0-9])?.  Label values must be
      between 0 and 63 characters long and must conform to the regular
      expression ([a-z]([-a-z0-9]*[a-z0-9])?)?.  No more than 256 labels can
      be associated with a given resource.  Note that additional character may
      be included in labels in the future. Clients should store labels in a
      representation such as JSON that does not depend on specific characters
      being disallowed.  Example: "environment" : "dev"  Read-write.
    lifecycleState: The project lifecycle state.  Read-only.
    name: The user-assigned name of the project. This field is optional and
      can remain unset.  Allowed characters are: lower- and upper-case
      letters, numbers, hyphen, single-quote, double-quotes, space, and
      exclamation point.  Example: "My Project"  Read-write.
    projectId: The unique, user-assigned id of the project. It must be 6 to 30
      lowercase letters, digits, or hyphens. It must start with a letter.
      Trailing hyphens are prohibited.  Example: "tokyo-rain-123"  Read-only
      after creation.
    projectNumber: The number uniquely identifying the project.  Example:
      415104041262.  Read-only.
  """

  class LifecycleStateValueValuesEnum(messages.Enum):
    """The project lifecycle state.  Read-only.

    Values:
      LIFECYCLE_STATE_UNSPECIFIED: Unspecified state.  This is only
        used/useful for distinguishing unset values.
      ACTIVE: The normal and active state.
      DELETE_REQUESTED: The project has been marked for deletion by the user
        (by invoking DeleteProject) or by the system (Google Cloud Platform).
        This can generally be reversed by invoking UndeleteProject.
      DELETE_IN_PROGRESS: The process of deleting the project has begun.
        Reversing the deletion is no longer possible.
    """
    LIFECYCLE_STATE_UNSPECIFIED = 0
    ACTIVE = 1
    DELETE_REQUESTED = 2
    DELETE_IN_PROGRESS = 3

  @encoding.MapUnrecognizedFields('additionalProperties')
  class LabelsValue(messages.Message):
    """The labels associated with this project.  Label keys must be between 1
    and 63 characters long and must conform to the following regular
    expression: [a-z]([-a-z0-9]*[a-z0-9])?.  Label values must be between 0
    and 63 characters long and must conform to the regular expression
    ([a-z]([-a-z0-9]*[a-z0-9])?)?.  No more than 256 labels can be associated
    with a given resource.  Note that additional character may be included in
    labels in the future. Clients should store labels in a representation such
    as JSON that does not depend on specific characters being disallowed.
    Example: "environment" : "dev"  Read-write.

    Messages:
      AdditionalProperty: An additional property for a LabelsValue object.

    Fields:
      additionalProperties: Additional properties of type LabelsValue
    """

    class AdditionalProperty(messages.Message):
      """An additional property for a LabelsValue object.

      Fields:
        key: Name of the additional property.
        value: A string attribute.
      """

      key = messages.StringField(1)
      value = messages.StringField(2)

    additionalProperties = messages.MessageField('AdditionalProperty', 1, repeated=True)

  createTime = messages.StringField(1)
  labels = messages.MessageField('LabelsValue', 2)
  lifecycleState = messages.EnumField('LifecycleStateValueValuesEnum', 3)
  name = messages.StringField(4)
  projectId = messages.StringField(5)
  projectNumber = messages.IntegerField(6)


class StandardQueryParameters(messages.Message):
  """Query parameters accepted by all methods.

  Enums:
    FXgafvValueValuesEnum: V1 error format.
    AltValueValuesEnum: Data format for response.

  Fields:
    f__xgafv: V1 error format.
    access_token: OAuth access token.
    alt: Data format for response.
    bearer_token: OAuth bearer token.
    callback: JSONP
    fields: Selector specifying which fields to include in a partial response.
    key: API key. Your API key identifies your project and provides you with
      API access, quota, and reports. Required unless you provide an OAuth 2.0
      token.
    oauth_token: OAuth 2.0 token for the current user.
    pp: Pretty-print response.
    prettyPrint: Returns response with indentations and line breaks.
    quotaUser: Available to use for quota purposes for server-side
      applications. Can be any arbitrary string assigned to a user, but should
      not exceed 40 characters.
    trace: A tracing token of the form "token:<tokenid>" or "email:<ldap>" to
      include in api requests.
    uploadType: Legacy upload protocol for media (e.g. "media", "multipart").
    upload_protocol: Upload protocol for media (e.g. "raw", "multipart").
  """

  class AltValueValuesEnum(messages.Enum):
    """Data format for response.

    Values:
      json: Responses with Content-Type of application/json
      media: Media download with context-dependent Content-Type
      proto: Responses with Content-Type of application/x-protobuf
    """
    json = 0
    media = 1
    proto = 2

  class FXgafvValueValuesEnum(messages.Enum):
    """V1 error format.

    Values:
      _1: v1 error format
      _2: v2 error format
    """
    _1 = 0
    _2 = 1

  f__xgafv = messages.EnumField('FXgafvValueValuesEnum', 1)
  access_token = messages.StringField(2)
  alt = messages.EnumField('AltValueValuesEnum', 3, default=u'json')
  bearer_token = messages.StringField(4)
  callback = messages.StringField(5)
  fields = messages.StringField(6)
  key = messages.StringField(7)
  oauth_token = messages.StringField(8)
  pp = messages.BooleanField(9, default=True)
  prettyPrint = messages.BooleanField(10, default=True)
  quotaUser = messages.StringField(11)
  trace = messages.StringField(12)
  uploadType = messages.StringField(13)
  upload_protocol = messages.StringField(14)


encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_1', '1')
encoding.AddCustomJsonEnumMapping(
    StandardQueryParameters.FXgafvValueValuesEnum, '_2', '2')
encoding.AddCustomJsonFieldMapping(
    StandardQueryParameters, 'f__xgafv', '$.xgafv')
