## Role
----------


### Import
----------


```python
from pyjars import Role
```


### Create Role
----------

We'll create a role named builder

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


### Delete Role
----------

We'll delete a role named builder

```python

from pyjars import RoleStrategy, permission, Role

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

new_role = Role(rs, 'globalRoles', 'builder')
response = new_role.delete()
if response.status_code == 200:
    print('deleted successfully')
else:
    print('Failed deleted role')

```

### Functions & Attributes
----------

```python
new_role = Role(rs, 'globalRoles', 'builder')
agent_perm = permission.AgentPermission()
agent_perm.Build = True
new_role.add_permission(agent_perm)
new_role.create()
```
> ***Result:*** 
> ```python
True or False
```

```python
new_role = Role(rs, 'globalRoles', 'builder')
agent_perm = permission.AgentPermission()
agent_perm.Build = True
new_role.remove_permission(agent_perm)
new_role.save()
```
> ***Result:*** 
> ```python
True or False
```

```python
new_role = Role(rs, 'globalRoles', 'builder')
new_role.assign_sid('username_or_group')
new_role.save()
```
> ***Result:*** 
> ```python
True or False
```

```python
new_role = Role(rs, 'globalRoles', 'builder')
new_role.unassign_sid('username_or_group')
new_role.save()
```
> ***Result:*** 
> ```python
True or False
```

```python
new_role = Role(rs, 'globalRoles', 'builder')
new_role.unassign_all()
new_role.save()
```
> ***Result:*** 
> ```python
True or False
```

```python
new_role = Role(rs, 'globalRoles', 'builder')
new_role.list_sid()
```
> ***Result:*** 
> ```python
['group1', 'username1', 'user2]
```

```python
new_role = Role(rs, 'globalRoles', 'builder')
agent_perm = permission.AgentPermission()
agent_perm.Build = True
run_perm = permission.RunPermission()
run_perm.Replay = True
new_role.add_permission([agent_perm, run_perm])
new_role.save()
new_role.list_permission()
```
> ***Result:*** 
> ```python
[
    pyjars.permission.RunPermission, pyjars.permission.AgentPermission
]
```

### Example
----------

> We'll create creator into globalRoles 

```python
from pyjars import RoleStrategy, Role, permission

agent_perm = permission.AgentPermission()
agent_perm.Create = True
agent_perm.Delete = True

job_perm = JobPermission()
job_perm.Create = True
job_perm.Delete = True

run_perm = RunPermission()
run_perm.Delete = True

view_perm = ViewPermission()
view_perm.Create = True
view_perm.Delete = True

credential_perm = CredentialPermission()
credential_perm.Create = True
credential_perm.Delete = True

set_permission = [agent_perm, job_perm, run_perm, view_perm, credential_perm]

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)

creator_role = Role(rs, 'globalRoles', 'creator')

response = creator_role.add_permission(set_permission)

```
``response is <Requests.Response> object``

