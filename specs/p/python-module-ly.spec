%def_with python3

%define modulename ly
Name: python-module-ly
Version: 0.9.5
Release: alt3.qa1

Summary: Tool and library for manipulating LilyPond files

Url: https://github.com/wbsoft/python-ly
License: GPL
Group: Development/Python

#Source-url: https://pypi.io/packages/source/a/%modulename/%modulename-%version.tar.gz
# Source-url: https://github.com/wbsoft/python-ly/archive/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %name-%version.tar

BuildRequires: python-devel

BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

#setup_python_module %modulename

%description
This package provides a Python library `ly` containing various Python
modules to parse, manipulate or create documents in LilyPond format.
A command line program `ly` is also provided that can be used to do various
manipulations with LilyPond files.

The LilyPond format is a plain text input format that is used by the
GNU music typesetter LilyPond (www.lilypond.org).

The python-ly package is Free Software, licensed under the GPL. This package
is written by the Frescobaldi developers and is used extensively by the
Frescobaldi project. The main author is Wilbert Berendsen.

You can also read the docs online at http://python-ly.readthedocs.org/.


%package -n python3-module-ly
Summary: Tool and library for manipulating LilyPond files
Group: Development/Python3

%description -n python3-module-ly
This package provides a Python library `ly` containing various Python
modules to parse, manipulate or create documents in LilyPond format.
A command line program `ly` is also provided that can be used to do various
manipulations with LilyPond files.

The LilyPond format is a plain text input format that is used by the
GNU music typesetter LilyPond (www.lilypond.org).

The python-ly package is Free Software, licensed under the GPL. This package
is written by the Frescobaldi developers and is used extensively by the
Frescobaldi project. The main author is Wilbert Berendsen.

You can also read the docs online at http://python-ly.readthedocs.org/.


%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%if_without python3
%_bindir/ly
%_bindir/ly-server
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-ly
%_bindir/ly
%_bindir/ly-server
%python3_sitelibdir/*
%endif


%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.5-alt3.qa1
- NMU: applied repocop patch

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt3
- real build with python3

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt2
- build python3 module

* Tue Jun 13 2017 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- initial build for ALT Sisyphus

