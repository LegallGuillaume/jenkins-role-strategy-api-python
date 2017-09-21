#!/usr/bin/env python3
"""Management Role Strategy Plugin from Jenkins with Python"""

import logging
import requests


def convert_string(convert):
    if not convert:
        return ''
    if isinstance(convert, list):
        return ','.join(convert)
    return convert


class RoleStrategy(object):
    def __init__(self, url, login, password, ssl_verify=True, ssl_cert=None):
        if 'http' not in url:
            raise PyjarsException('Missing http or https', 400, dict(url=url))
        if url[-1:] == '/':
            url = url[-1:]
        self._url = url + '/role-strategy/strategy'
        self._session = self._connect(login, password, ssl_verify, ssl_cert)
        crumb = self._get(
            url +
            '/crumbIssuer/api/xml?xpath=concat(//crumbRequestField,":",//crumb)'
        )
        #if there are no crumb we don't need this below
        if crumb.status_code == 200:
            head = crumb.text.split(':')
            self._session.headers = {str(head[0]): str(head[1])}
        if not is_connected():
            raise PyjarsException('Authentification Failed', 401,
                                  dict(
                                      login=login,
                                      password='****',
                                      url=url,
                                      ssl=self.ssl_verify,
                                      cert=ssl_cert))

    def is_connected(self):
        return self._get(self._url + '/getAllRoles').status_code == 200

    def _connect(self, login, password, ssl_verify, ssl_cert, header=None):
        _s = requests.Session()
        _s.auth = (login, password)
        _s.cert = ssl_cert
        _s.verify = ssl_verify
        _s.headers = header
        return _s

    def _post(self, api_url, data):
        """Return requests.models.Response"""
        return self._session.post(api_url, data=data)

    def _get(self, api_url, data=None):
        """Return requests.models.Response"""
        return self._session.get(api_url, data=data)

    def _delete(self, api_url):
        """Return requests.models.Response"""
        return self._session.delete(api_url, data=data)

    def Unassign_sid_from_all(self, type, sid):
        url = self._url + '/deleteSid'
        data = dict(
            type=type,
            sid=sid, )
        return self._post(url, data=data)


class Role:
    def __init__(self, parent, type, roleName):
        self.type = type
        self.roleName = roleName
        self._parent = parent
        self._permissions = []

    def create(self, pattern=None):
        url = self._parent._url + '/addRole'
        data = dict(
            type=self.type,
            roleName=self.roleName,
            permissionIds=','.join(self.details_permission()),
            overwrite=True, )
        if pattern:
            data['pattern'] = pattern
        return self._parent._post(url, data=data)

    def add_permission(self, permissionModel):
        permission = permissionModel
        if not isinstance(permission, list):
            permission = [permission]
        ref_ret = []
        for perm in permission:
            has_perm = self.has_permissionModel(perm)
            if has_perm:
                self._permissions = list(
                    set(self._permissions) - set([has_perm]))
            self._permissions.append(perm)
            ref_ret += [perm in self._permissions]
        return all(ref_ret)

    def remove_permission(self, permissionModel):
        permission = permissionModel
        if not isinstance(permission, list):
            permission = [permission]
        ref_ret = []
        for perm in permission:
            has_perm = has_permissionModel(perm)
            if has_perm:
                self._permissions = list(
                    set(self._permissions) - set([has_perm]))
            ref_ret += [perm not in self._permissions]
        return all(ref_ret)

    def details_permission(self, permissionModel=None):
        if not permissionModel:
            return [per.get_true_permission() for per in self._permissions]
        else:
            return permissionModel.get_details()

    def has_permissionModel(self, permissionModel):
        if self._permissions:
            for perm in self.list_permission():
                if perm._base == permissionModel._base:
                    return perm._base
        return None

    def list_permission(self):
        return self._permissions

    def delete(self):
        url = self._parent._url + '/removeRoles'
        data = dict(type=self.type, roleNames=self.roleName)
        return self._parent._post(url, data=data)

    def assign_sid(self, sid):
        url = self._parent._url + '/assignRole'
        data = dict(
            type=self.type,
            roleName=self.roleName,
            sid=convert_string(sid), )
        return self._parent._post(url, data=data)

    def unassign_sid(self, sid):
        url = self._parent._url + '/unassignRole'
        data = dict(
            type=self.type,
            roleName=self.roleName,
            sid=convert_string(sid), )
        return self._parent._post(url, data=data)

    def unassign_all(self):
        ref_ret = []
        for us_gr in self.list_sid():
            ref_ret += [self.unassign_sid(us_gr).status_code == 200]
        return all(ref_ret)

    def list_sid(self):
        url = self._parent._url + '/getAllRoles'
        query = self._parent._get(url)
        if query.status_code != 200:
            query.raise_for_status()
        try:
            return query.json()[self.roleName]
        except KeyError:
            return []


class PyjarsException(Exception):
    def __init__(self, message, code, data):
        self.error = dict(
            message=message,
            status_code=code, )
