# jenkins-role-strategy-api-python **Pyjars**
API python from Jenkins Plugin - Role Strategy Plugin - https://github.com/jenkinsci/role-strategy-plugin

----------

## I. Introduction

This API allow to manage Role from [Role Strategy Plugin](https://github.com/jenkinsci/role-strategy-plugin)

> Author: Le Gall Guillaume <gulegall13@gmail.com>

> Date: 09/2017 | Based: python3


This API python allow to :

- Create **Role** *Role is (globalRoles, projectRoles, slaveRoles)*

- Delete Role

- Assign User/Group to Role

- Unassign User/Group to Role

- Unassign All User/Group to Role

- Unassign User/Group from All Roles

- Get All User/Group from Role *Only globalRoles for the moment*

- Custom permission easy to make

Todo:

- [x] <strike>setup.py **Most Important**</strike>

- [ ] Get All User/Group from Role **(globalRoles, projectRoles, slaveRoles)**

- [ ] Get Role **(know his permissions), Role Strategy Plugin to modify**

- [ ] *maybe your request*


----------

## II. Installation


```bash
$ pip install .
```

**or**

```bash
$ python3 setup.py install 
```


----------

## III. Python DEV


### a. Create function

**Example:**

```python

from pyjars import RoleStrategy, permission, Role

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

new_role = Role(rs, 'globalRoles', 'builder')

agentPerm = permission.AgentPermission()
agentPerm.Build = True

jobPerm = permission.JobPermission()
jobPerm.Build = True

new_role.add_permission([jobPerm, agentPerm])

response = new_role.create(pattern=None)
if response.status_code == 200:
    print('created successfully')
else:
    print('Failed create role')

```

### b. Delete function

**Example:**

```python

from pyjars import RoleStrategy, Role

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

builder_role = Role(rs, 'globalRoles', 'builder')

response = builder_role.delete()
if response.status_code == 200:
    print('deleted successfully')
else:
    print('Failed delete role')

```

### c. Assign function

**Example:**

```python

from pyjars import RoleStrategy, Role

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

builder_role = Role(rs, 'globalRoles', 'builder')

response = builder_role.assign_sid('username_or_group')
if response.status_code == 200:
    print('Assign successfully')
else:
    print('Failed assign role')

```

### d. Unassign function

**Example:**

```python

from pyjars import RoleStrategy, Role

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

builder_role = Role(rs, 'globalRoles', 'builder')

response = builder_role.unassign_sid('username_or_group')
if response.status_code == 200:
    print('Unassign successfully')
else:
    print('Failed unassign role')

```

### e. Unassign All function

**Example:**

```python

from pyjars import RoleStrategy, Role

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

builder_role = Role(rs, 'globalRoles', 'builder')

response = builder_role.unassign_all()
if response.status_code == 200:
    print('Unassign all user/group successfully')
else:
    print('Failed unassign all user/group role')

```

### f. list user/group from role function

**Example:**

```python

from pyjars import RoleStrategy, Role

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

builder_role = Role(rs, 'globalRoles', 'builder')

members = builder_role.list_sid()
if members:
    print('list of members is:', members)
else:
    print('There are no members')

```

### g. Permissions

> **Agent Permission:** *AgentPermission()*
> - Create
> - Build
> - Configure
> - Connect
> - Delete
> - Disconnect
> - Provision

> **Job Permission:** *JobPermission()*
> - Build
> - Cancel
> - Configure
> - Create
> - Delete
> - Discover
> - Move
> - Read
> - Workspace

> **Run Permission:** *RunPermission()*
> - Artifacts
> - Delete
> - Replay
> - Update

> **View Permission:** *ViewPermission()*
> - Configure
> - Create
> - Delete
> - Read

> **Scm Permission:** *ScmPermission()*
> - Tag

> **Credential Permission:** *CredentialPermission()*
> - Create
> - Delete
> - ManageDomains
> - Update
> - View

> **Overall Permission:** *OverallPermission()*
> - Administer
> - Read

```python

overPerm = OverallPermission()
overPerm.Administer = True

overPerm.attributes
#---------Result-------
{
    'Administer': True,
    'Read': False 
}
#---------Result-------

overPerm.get_true_permission()
#---------Result-------
['hudson.model.Hudson.Administer']
#---------Result-------

overPerm.get_false_permission()
#---------Result-------
['hudson.model.Hudson.Read']
#---------Result-------
```
