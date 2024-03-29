#!/usr/bin/python3
"""Definition of unittests for console.py.

Unittest classes:
        TestHBNBCommand_prompting
            TestHBNBCommand_help
                TestHBNBCommand_exit
                    TestHBNBCommand_create
                        TestHBNBCommand_show
                            TestHBNBCommand_all
                                TestHBNBCommand_destroy
                                    TestHBNBCommand_update
                                    """
                                    import os
                                    import sys
                                    import unittest
                                    from models import storage
                                    from models.engine.file_storage import FileStorage
                                    from console import HBNBCommand
                                    from io import StringIO
                                    from unittest.mock import patch

