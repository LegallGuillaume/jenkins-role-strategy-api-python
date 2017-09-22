## RoleStrategy
----------


### Import
----------


```python
from pyjars import Role
```


### Start Connection
----------

```python

from pyjars import RoleStrategy

rs = RoleStrategy('https://127.0.0.1:8080', 'admin', 'azerty123', ssl_verify=True, ssl_cert=None)
```

*ssl_cert is path/to/your/cert.crt*


### Exception
----------

RoleStrategy function can raise a PyjarsException:

- message *string*

- status code *int*

- data *dict*
