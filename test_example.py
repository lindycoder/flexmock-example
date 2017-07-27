import flexmock
import subprocess


def test_flexmock_method_call_error():
    flexmock(subprocess).should_receive("call").once()\
        .with_args(["echo", "hello"])

    raise Exception("I'd like to see this error...")
