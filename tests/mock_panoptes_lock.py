"""
Copyright 2018, Oath Inc.
Licensed under the terms of the Apache 2.0 license. See LICENSE file in project root for terms.
"""


from builtins import object
class MockPanoptesLock(object):
    @staticmethod
    def locked():
        return True
