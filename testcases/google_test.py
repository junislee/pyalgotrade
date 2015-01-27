# PyAlgoTrade
#
# Copyright 2011-2015 Gabriel Martin Becedillas Ruiz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

import os

import common

from pyalgotrade.tools import googlefinance
from pyalgotrade.barfeed import googlefeed


class ToolsTestCase(common.TestCase):
    def testDownloadAndParseDaily(self):
        instrument = "orcl"

        common.init_temp_path()
        path = os.path.join(common.get_temp_path(), "orcl-2010.csv")
        googlefinance.download_daily_bars(instrument, 2010, path)
        bf = googlefeed.Feed()
        bf.addBarsFromCSV(instrument, path)
        bf.loadAll()
        self.assertEqual(bf[instrument][-1].getOpen(), 31.22)
        self.assertEqual(bf[instrument][-1].getClose(), 31.30)

    def testBuildDailyFeed(self):
        with common.TmpDir() as tmpPath:
            instrument = "orcl"
            bf = googlefinance.build_feed([instrument], 2010, 2010, storage=tmpPath)
            bf.loadAll()
            self.assertEqual(bf[instrument][-1].getOpen(), 31.22)
            self.assertEqual(bf[instrument][-1].getClose(), 31.30)
