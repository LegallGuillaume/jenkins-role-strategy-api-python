## Permission
----------


### Import
----------


```python
from pyjars import permission
```


### Permission Type
----------

**Agent Permission:** *AgentPermission()*
> - Create
> - Build
> - Configure
> - Connect
> - Delete
> - Disconnect
> - Provision

**Job Permission:** *JobPermission()*
> - Build
> - Cancel
> - Configure
> - Create
> - Delete
> - Discover
> - Move
> - Read
> - Workspace

**Run Permission:** *RunPermission()*
> - Artifacts
> - Delete
> - Replay
> - Update

**View Permission:** *ViewPermission()*
> - Configure
> - Create
> - Delete
> - Read

**Scm Permission:** *ScmPermission()*
> - Tag

**Credential Permission:** *CredentialPermission()*
> - Create
> - Delete
> - ManageDomains
> - Update
> - View

**Overall Permission:** *OverallPermission()*
> - Administer
> - Read

```python
from pyjars import permission

agent_perm = permission.AgentPermission()
job_perm = JobPermission()
run_perm = RunPermission()
view_perm = ViewPermission()
scm_perm = ScmPermission()
credential_perm = CredentialPermission()
overall_perm = OverallPermission()
```

### Functions & Attributes
----------

```python
agent_perm = permission.AgentPermission()
agent_perm.Build = True
agent_perm.attributes
```
> ***Result:*** 
> ```python
 {'Build': True,
  'Configure': False,
  'Connect': False,
  'Create': False,
  'Delete': False,
  'Disconnect': False,
  'Provision': False}
```

```python
agent_perm.get_true_permission()
```
> ***Result:*** 
> ```python
'hudson.model.Computer.Build'
```

```python
agent_perm.get_false_permission()
```
> ***Result:*** 
> ```python
'hudson.model.Computer.Configure,hudson.model.Computer.Delete,
 hudson.model.Computer.Disconnect,hudson.model.Computer.Provision,
 hudson.model.Computer.Connect,hudson.model.Computer.Create'
```

```python
agent_perm.get_details()
```
> ***Result:*** 
> ```python
[hudson.model.Computer.Build]
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

