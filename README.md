&nbsp_place_holder;

&nbsp_place_holder;

**netstatus** (version 0.1)
[index](.)

[/home/rwilson/Scripts/Python/netstatus/netstatus/netstatus.py](file:/home/rwi
lson/Scripts/Python/netstatus/netstatus/netstatus.py)

`This&nbsp_place_holder;module&nbsp_place_holder;is&nbsp_place_holder;for&nbsp
_place_holder;checking&nbsp_place_holder;a&nbsp_place_holder;networks&nbsp_pla
ce_holder;status.`

&nbsp_place_holder;

**Modules**

`&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&
nbsp_place_holder;&nbsp_place_holder;`

&nbsp_place_holder;

[errno](errno.html)

[os](os.html)

[signal](signal.html)

[socket](socket.html)

&nbsp_place_holder;

**Classes**

`&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&
nbsp_place_holder;&nbsp_place_holder;`

&nbsp_place_holder;

[__builtin__.object](__builtin__.html#object)

    

[NetworkStatus](netstatus.html#NetworkStatus)

[exceptions.Exception](exceptions.html#Exception)([exceptions.BaseException](e
xceptions.html#BaseException))

    

[AnonymousError](netstatus.html#AnonymousError)

&nbsp_place_holder;

class **AnonymousError**([exceptions.Exception](exceptions.html#Exception))

`&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;`

`Same&nbsp_place_holder;as&nbsp_place_holder;except&nbsp_place_holder;[Excepti
on](exceptions.html#Exception).

&nbsp_place_holder;`

&nbsp_place_holder;

Method resolution order:

    [AnonymousError](netstatus.html#AnonymousError)
    [exceptions.Exception](exceptions.html#Exception)
    [exceptions.BaseException](exceptions.html#BaseException)
    [__builtin__.object](__builtin__.html#object)

* * *

Data descriptors defined here:

**__weakref__**
    `list&nbsp_place_holder;of&nbsp_place_holder;weak&nbsp_place_holder;references&nbsp_place_holder;to&nbsp_place_holder;the&nbsp_place_holder;object&nbsp_place_holder;(if&nbsp_place_holder;defined)`

* * *

Methods inherited from [exceptions.Exception](exceptions.html#Exception):

**__init__**(...)
    `x.__init__(...)&nbsp_place_holder;initializes&nbsp_place_holder;x;&nbsp_place_holder;see&nbsp_place_holder;help(type(x))&nbsp_place_holder;for&nbsp_place_holder;signature`

* * *

Data and other attributes inherited from
[exceptions.Exception](exceptions.html#Exception):

**__new__** = <built-in method __new__ of type object>    `T.__new__(S,&nbsp_place_holder;...)&nbsp_place_holder;->&nbsp_place_holder;a&nbsp_place_holder;new&nbsp_place_holder;[object](__builtin__.html#object)&nbsp_place_holder;with&nbsp_place_holder;type&nbsp_place_holder;S,&nbsp_place_holder;a&nbsp_place_holder;subtype&nbsp_place_holder;of&nbsp_place_holder;T`

* * *

Methods inherited from
[exceptions.BaseException](exceptions.html#BaseException):

**__delattr__**(...)
    `x.__delattr__('name')&nbsp_place_holder;<==>&nbsp_place_holder;del&nbsp_place_holder;x.name`

**__getattribute__**(...)
    `x.__getattribute__('name')&nbsp_place_holder;<==>&nbsp_place_holder;x.name`

**__getitem__**(...)
    `x.__getitem__(y)&nbsp_place_holder;<==>&nbsp_place_holder;x[y]`

**__getslice__**(...)
    `x.__getslice__(i,&nbsp_place_holder;j)&nbsp_place_holder;<==>&nbsp_place_holder;x[i:j]  
&nbsp_place_holder;

Use&nbsp_place_holder;of&nbsp_place_holder;negative&nbsp_place_holder;indices&
nbsp_place_holder;is&nbsp_place_holder;not&nbsp_place_holder;supported.`

**__reduce__**(...)

**__repr__**(...)
    `x.__repr__()&nbsp_place_holder;<==>&nbsp_place_holder;repr(x)`

**__setattr__**(...)
    `x.__setattr__('name',&nbsp_place_holder;value)&nbsp_place_holder;<==>&nbsp_place_holder;x.name&nbsp_place_holder;=&nbsp_place_holder;value`

**__setstate__**(...)

**__str__**(...)
    `x.__str__()&nbsp_place_holder;<==>&nbsp_place_holder;str(x)`

**__unicode__**(...)

* * *

Data descriptors inherited from
[exceptions.BaseException](exceptions.html#BaseException):

**__dict__**

**args**

**message**

&nbsp_place_holder;

class **NetworkStatus**([__builtin__.object](__builtin__.html#object))

`&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;`

&nbsp_place_holder;

Methods defined here:

**check**(*args, **kwargs)
    `Check&nbsp_place_holder;if&nbsp_place_holder;the&nbsp_place_holder;network&nbsp_place_holder;is&nbsp_place_holder;up.`

**if_offline**(self, func, *args, **kw)
    `Call&nbsp_place_holder;a&nbsp_place_holder;function&nbsp_place_holder;if&nbsp_place_holder;the&nbsp_place_holder;network&nbsp_place_holder;is&nbsp_place_holder;down.`

**if_online**(self, func, *args, **kw)
    `Call&nbsp_place_holder;a&nbsp_place_holder;function&nbsp_place_holder;if&nbsp_place_holder;the&nbsp_place_holder;network&nbsp_place_holder;is&nbsp_place_holder;up.`

**offline**(self, **kw)
    `return&nbsp_place_holder;False&nbsp_place_holder;if&nbsp_place_holder;the&nbsp_place_holder;network&nbsp_place_holder;is&nbsp_place_holder;DOWN.`

**online**(self, **kw)
    `return&nbsp_place_holder;True&nbsp_place_holder;is&nbsp_place_holder;the&nbsp_place_holder;network&nbsp_place_holder;is&nbsp_place_holder;UP.`

**run_test**(self)
    `Continuously&nbsp_place_holder;check&nbsp_place_holder;if&nbsp_place_holder;the&nbsp_place_holder;network&nbsp_place_holder;is&nbsp_place_holder;UP&nbsp_place_holder;or&nbsp_place_holder;DOWN.`

**set_timeout**(self, limit)
    `Update&nbsp_place_holder;limit`

**timeout**(seconds=1, error_message='Timer expired')
    `If&nbsp_place_holder;a&nbsp_place_holder;function&nbsp_place_holder;does&nbsp_place_holder;not&nbsp_place_holder;finish&nbsp_place_holder;in&nbsp_place_holder;a&nbsp_place_holder;given&nbsp_place_holder;time  
send&nbsp_place_holder;an&nbsp_place_holder;alarm&nbsp_place_holder;signal.`

* * *

Data descriptors defined here:

**__dict__**
    `dictionary&nbsp_place_holder;for&nbsp_place_holder;instance&nbsp_place_holder;variables&nbsp_place_holder;(if&nbsp_place_holder;defined)`

**__weakref__**
    `list&nbsp_place_holder;of&nbsp_place_holder;weak&nbsp_place_holder;references&nbsp_place_holder;to&nbsp_place_holder;the&nbsp_place_holder;object&nbsp_place_holder;(if&nbsp_place_holder;defined)`

* * *

Data and other attributes defined here:

**limit** = 2

&nbsp_place_holder;

**Functions**

`&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&
nbsp_place_holder;&nbsp_place_holder;`

&nbsp_place_holder;

**sleep**(...)
    `sleep(seconds)  
&nbsp_place_holder;

Delay&nbsp_place_holder;execution&nbsp_place_holder;for&nbsp_place_holder;a&nb
sp_place_holder;given&nbsp_place_holder;number&nbsp_place_holder;of&nbsp_place
_holder;seconds.&nbsp_place_holder;&nbsp_place_holder;The&nbsp_place_holder;ar
gument&nbsp_place_holder;may&nbsp_place_holder;be

a&nbsp_place_holder;floating&nbsp_place_holder;point&nbsp_place_holder;number&
nbsp_place_holder;for&nbsp_place_holder;subsecond&nbsp_place_holder;precision.
`

&nbsp_place_holder;

**Data**

`&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&
nbsp_place_holder;&nbsp_place_holder;`

&nbsp_place_holder;

**__author__** = 'Ricky Wilson'  
**__version__** = '0.1'

&nbsp_place_holder;

**Author**

`&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&nbsp_place_holder;&
nbsp_place_holder;&nbsp_place_holder;`

&nbsp_place_holder;

Ricky&nbsp_place_holder;Wilson

