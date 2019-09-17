# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License") you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
# pylint: disable=invalid-name, unused-argument
#
# This file is part of DNN compiler maintained at
# https://github.com/ai-techsystems/dnnCompiler

import common

import dnnc as dc
import numpy as np
import unittest

class SqrtTest(unittest.TestCase):
    def setUp(self):
        np.seterr(all="ignore")   # Numpy raises warnings while calling np.sqrt()
        self.len = 24
        self.np_a = np.random.randn(self.len).astype(np.float64)
        # self.np_a += 2 * self.np_a
        self.dc_a = dc.array(list(self.np_a))

    def test_Sqrt1D (self):
        npr = np.sqrt(self.np_a)
        dcr = dc.sqrt(self.dc_a)
        np.testing.assert_allclose(npr, np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)
    
    def test_Sqrt2D (self):
        np_a = np.reshape(self.np_a, (6,4))
        dc_a = dc.reshape(self.dc_a, (6,4))
        npr = np.sqrt(np_a)
        dcr = dc.sqrt(dc_a)
        np.testing.assert_allclose(npr.flatten(), np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)

    def test_Sqrt3D (self):
        np_a = np.reshape(self.np_a, (2,4,3))
        dc_a = dc.reshape(self.dc_a, (2,4,3))
        npr = np.sqrt(np_a)
        dcr = dc.sqrt(dc_a)
        np.testing.assert_allclose(npr.flatten(), np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)
    
    def test_Sqrt4D (self):
        np_a = np.reshape(self.np_a, (2,2,2,3))
        dc_a = dc.reshape(self.dc_a, (2,2,2,3))
        npr = np.sqrt(np_a)
        dcr = dc.sqrt(dc_a)
        np.testing.assert_allclose(npr.flatten(), np.array(dcr.data()).astype(np.float32),
                rtol=1e-3, atol=1e-3)

    def tearDown(self):
        return "test finished"

if __name__ == '__main__':
    unittest.main()
    
