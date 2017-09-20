#!/usr/bin/env python3
"""Permissions For Jenkins Roles"""

from collections import OrderedDict


class PermissionModel:
    def __init__(self):
        self._base = ''
        self.attributes = {}

    def __getattr__(self, attr):
        try:
            super().__getattribute__(attr)
        except AttributeError:
            try:
                return self.attributes[attr]
            except KeyError:
                raise AttributeError

    def __setattr__(self, attr, value):
        try:
            if attr in self.attributes:
                self.attributes[attr] = value
                return
        except:
            pass
        super().__setattr__(attr, value)

    def attributes(self):
        return self.attributes

    def get_true_permission(self):
        return ','.join(self.get_details())

    def get_false_permission(self):
        return ','.join([
            '{}.{}'.format(self._base, perm)
            for perm, value in self.attributes.items() if value == False
        ])

    def get_details(self):
        return [
            '{}.{}'.format(self._base, perm)
            for perm, value in self.attributes.items() if value == True
        ]


class JobPermission(PermissionModel):
    def __init__(self):
        self._base = 'hudson.model.Item'
        self.attributes = OrderedDict(
            Build=False,
            Cancel=False,
            Configure=False,
            Create=False,
            Delete=False,
            Discover=False,
            Move=False,
            Read=False,
            Workspace=False)


class ViewPermission(PermissionModel):
    def __init__(self):
        self._base = 'hudson.model.View'
        self.attributes = OrderedDict(
            Configure=False, Create=False, Delete=False, Read=False)


class RunPermission(PermissionModel):
    def __init__(self):
        self._base = 'hudson.model.Run'
        self.attributes = OrderedDict(
            Artifacts=False, Delete=False, Replay=False, Update=False)


class AgentPermission(PermissionModel):
    def __init__(self):
        self._base = 'hudson.model.Computer'
        self.attributes = OrderedDict(
            Create=False,
            Build=False,
            Configure=False,
            Connect=False,
            Delete=False,
            Disconnect=False,
            Provision=False)


class ScmPermission(PermissionModel):
    def __init__(self):
        self._base = 'hudson.scm.SCM'
        self.attributes = OrderedDict(Tag=False)


class CredentialPermission(PermissionModel):
    def __init__(self):
        self._base = 'com.cloudbees.plugins.credentials.CredentialsProvider'
        self.attributes = OrderedDict(
            Create=False,
            Delete=False,
            ManageDomains=False,
            Update=False,
            View=False)


class OverallPermission(PermissionModel):
    def __init__(self):
        self._base = 'hudson.model.Hudson'
        self.attributes = OrderedDict(Administer=False, Read=False)
