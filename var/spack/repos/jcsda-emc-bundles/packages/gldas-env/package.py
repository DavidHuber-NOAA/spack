# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: Apache-2.0

import sys

from spack import *


class GldasEnv(BundlePackage):
    """Development environment for GLDAS"""

    homepage = "https://github.com/NOAA-EMC/GLDAS"
    git      = "https://github.com/NOAA-EMC/GLDAS.git"

    maintainers = ['kgerheiser']

    version('develop', branch='develop')

    depends_on('w3nco')
    depends_on('w3emc')
    depends_on('nemsio')
    depends_on('bacio')
    depends_on('sp')
    depends_on('netcdf-fortran')
    depends_on('netcdf-c')
    depends_on('esmf')
