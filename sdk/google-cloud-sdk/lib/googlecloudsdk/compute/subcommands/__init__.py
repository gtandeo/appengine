# Copyright 2014 Google Inc. All Rights Reserved.
"""The super-group for the compute CLI."""
import argparse
import sys

from googlecloudsdk.calliope import actions
from googlecloudsdk.calliope import base
from googlecloudsdk.compute.lib import utils
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


DETAILED_HELP = {
    'brief': 'Read and manipulate Google Compute Engine resources',
}


def _Args(parser):
  """Set up argument parsing."""
  parser.add_argument(
      '--endpoint',
      help=argparse.SUPPRESS,
      action=actions.StoreProperty(
          properties.VALUES.api_endpoint_overrides.compute))


def _DoFilter(context, http, api_client_default, args):
  """Set up paramter defaults and endpoints."""
  if args.endpoint:
    log.warn('The --endpoint flag is deprecated and will be removed.  '
             'Set the api_endpoint_overrides/compute property instead.  '
             'e.g. gcloud config set api_client_overrides/compute beta')
  utils.SetResourceParamDefaults()
  utils.UpdateContextEndpointEntries(context, http, api_client_default)


@base.ReleaseTracks(base.ReleaseTrack.GA)
class Compute(base.Group):
  """Read and manipulate Google Compute Engine resources."""
  detailed_help = DETAILED_HELP

  @staticmethod
  def Args(parser):
    _Args(parser)

  def Filter(self, context, args):
    _DoFilter(context, self.Http(), 'v1', args)


@base.ReleaseTracks(base.ReleaseTrack.BETA)
class ComputeBeta(base.Group):
  """Read and manipulate Google Compute Engine resources."""
  detailed_help = DETAILED_HELP

  @staticmethod
  def Args(parser):
    _Args(parser)

  def Filter(self, context, args):
    _DoFilter(context, self.Http(), 'beta', args)


@base.ReleaseTracks(base.ReleaseTrack.ALPHA)
class ComputeAlpha(base.Group):
  """Read and manipulate Google Compute Engine resources."""
  detailed_help = DETAILED_HELP

  @staticmethod
  def Args(parser):
    _Args(parser)

  def Filter(self, context, args):
    _DoFilter(context, self.Http(), 'alpha', args)
