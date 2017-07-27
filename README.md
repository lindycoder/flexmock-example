# flexmock-example
Result is:

```
$ tox
GLOB sdist-make: /.../flexmock-example/setup.py
py36 inst-nodeps: /.../flexmock-example/.tox/dist/UNKNOWN-0.0.0.zip
py36 installed: flexmock==0.10.2,py==1.4.34,pytest==3.1.3,UNKNOWN==0.0.0
py36 runtests: PYTHONHASHSEED='1895786992'
py36 runtests: commands[0] | py.test .
======================================================================================================================== test session starts ========================================================================================================================
platform darwin -- Python 3.6.2, pytest-3.1.3, py-1.4.34, pluggy-0.4.0
rootdir: /.../flexmock-example, inifile:
collected 1 item s

test_example.py F

============================================================================================================================= FAILURES ==============================================================================================================================
__________________________________________________________________________________________________________________ test_flexmock_method_call_error __________________________________________________________________________________________________________________

    def flexmock_teardown():
        """Performs lexmock-specific teardown tasks."""
        saved = {}
        instances = []
        classes = []
        for mock_object, expectations in FlexmockContainer.flexmock_objects.items():
            saved[mock_object] = expectations[:]
            for expectation in expectations:
                _getattr(expectation, 'reset')()
        for mock in saved.keys():
            obj = mock._object
            if not isinstance(obj, Mock) and not _isclass(obj):
                instances.append(obj)
            if _isclass(obj):
                classes.append(obj)
        for obj in instances + classes:
            for attr in UPDATED_ATTRS:
                try:
                    obj_dict = obj.__dict__
                    if _get_code(obj_dict[attr]) is _get_code(Mock.__dict__[attr]):
                        del obj_dict[attr]
                except:
                    try:
                        if _get_code(getattr(obj, attr)) is _get_code(Mock.__dict__[attr]):
                            delattr(obj, attr)
                    except AttributeError:
                        pass
        FlexmockContainer.teardown_properties()
        FlexmockContainer.reset()
    
        # make sure this is done last to keep exceptions here from breaking
        # any of the previous steps that cleanup all the changes
        for mock_object, expectations in saved.items():
            for expectation in expectations:
>               _getattr(expectation, 'verify')()

.tox/py36/lib/python3.6/site-packages/flexmock.py:1180: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
.tox/py36/lib/python3.6/site-packages/flexmock.py:620: in verify
    (_format_args(self.name, self.args), message, self.times_called))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

self = <flexmock.Expectation object at 0x10c196cc0>, exception = <class 'flexmock.MethodCallError'>, message = "call(['echo', 'hello']) expected to be called exactly 1 times, called 0 times"

    def __raise(self, exception, message):
        """Safe internal raise implementation.
    
            In case we're patching builtins, it's important to reset the
            expectation before raising any exceptions or else things like
            open() might be stubbed out and the resulting runner errors are very
            difficult to diagnose.
            """
        self.reset()
>       raise exception(message)
E       flexmock.MethodCallError: call(['echo', 'hello']) expected to be called exactly 1 times, called 0 times

.tox/py36/lib/python3.6/site-packages/flexmock.py:349: MethodCallError
===================================================================================================================== 1 failed in 0.19 seconds ======================================================================================================================
ERROR: InvocationError: '/.../flexmock-example/.tox/py36/bin/py.test .'
______________________________________________________________________________________________________________________________ summary ______________________________________________________________________________________________________________________________
ERROR:   py36: commands failed
```

I would expect the string `I'd like to see this error...` to appear somewhere
