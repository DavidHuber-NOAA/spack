# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlDatetimeLocale(PerlPackage):
    """DateTime::Locale - Localization support for DateTime.pm"""

    homepage = "https://metacpan.org/pod/DateTime::Locale"
    url = "https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Locale-1.40.tar.gz"

    maintainers("EbiArnie")

    version("1.40", sha256="7490b4194b5d23a4e144976dedb3bdbcc6d3364b5d139cc922a86d41fdb87afb")

    depends_on("perl@5.8.4:", type=("build", "link", "run", "test"))
    depends_on("perl-cpan-meta-check@0.011:", type=("build", "test"))
    depends_on("perl-dist-checkconflicts@0.02:", type=("build", "run", "test"))
    depends_on("perl-file-sharedir", type=("build", "run", "test"))
    depends_on("perl-file-sharedir-install@0.06:", type=("build"))
    depends_on("perl-ipc-system-simple", type=("build", "test"))
    depends_on("perl-namespace-autoclean@0.19:", type=("build", "run", "test"))
    depends_on("perl-params-validationcompiler@0.13:", type=("build", "run", "test"))
    depends_on("perl-path-tiny", type=("build", "test"))
    depends_on("perl-specio", type=("build", "run", "test"))
    depends_on("perl-test-file-sharedir", type=("build", "test"))
    depends_on("perl-test2-plugin-nowarnings", type=("build", "test"))
    depends_on("perl-test2-suite", type=("build", "test"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use DateTime::Locale; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
