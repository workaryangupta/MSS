# -*- coding: utf-8 -*-
"""

    mslib.conftest
    ~~~~~~~~~~~~~~

    common definitions for py.test

    This file is part of mss.

    :copyright: Copyright 2016-2017 Reimar Bauer
    :copyright: Copyright 2016-2017 by the mss team, see AUTHORS.
    :license: APACHE-2.0, see LICENSE for details.

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""


import imp
import os
import sys
import shutil
import pytest

from mslib.mswms.demodata import DataFiles
import mslib._tests.utils as utils


try:
    # package currently on pypi only
    from pyvirtualdisplay import Display
except ImportError:
    Display = None

sys.path.insert(0, utils.BASE_DIR)


@pytest.fixture(scope="session", autouse=True)
def configure_testdata(request):
    if Display is not None:
        # needs invisible xvfb installed, default backend for visible output is xephyr
        Display(backend="xvfb", visible=0, size=(1680, 1050)).start()
    if not os.path.exists(utils.DATA_DIR):
        print('\n configure testdata')
        examples = DataFiles(data_dir=utils.DATA_DIR,
                             vt_cache=utils.VT_CACHE,
                             server_config_dir=utils.BASE_DIR)
        examples.create_datadir()
        examples.create_server_config(detailed_information=True)
        examples.create_data()
        if not os.path.exists(utils.VT_CACHE):
            os.makedirs(utils.VT_CACHE)
    imp.load_source('mss_wms_settings', utils.SERVER_CONFIG_FILE)

    def unconfigure_testdata():
        print('\n unconfigure testdata')
        if Display is not None:
            Display.stop()
        if os.path.exists(utils.VT_CACHE):
            shutil.rmtree(utils.VT_CACHE)
        if os.path.exists(utils.BASE_DIR):
            shutil.rmtree(utils.BASE_DIR)
    request.addfinalizer(unconfigure_testdata)


@pytest.fixture(scope="function")
def testdata_exists():
    if not os.path.exists(BASE_DIR):
        pytest.skip("testdata not existing")


@pytest.fixture(scope="class")
def testdata_exists():
    if not os.path.exists(BASE_DIR):
        pytest.skip("testdata not existing")
