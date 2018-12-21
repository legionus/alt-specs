%define sname unicodecsv

%def_with python3

Name: python-module-%sname
Version: 0.14.1
Release: alt1.2
Summary: Drop-in replacement for Python csv module which supports unicode strings
Group: Development/Python
License: BSD
URL: https://github.com/jdunck/python-unicodecsv
Source: %name-%version.tar

BuildRequires: python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-unittest2

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-unittest2
%endif

BuildArch: noarch

%description
The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle.

%if_with python3
%package -n python3-module-%sname
Summary: Drop-in replacement for Python csv module which supports unicode strings
Group: Development/Python3

%description -n python3-module-%sname
The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle.
%endif

%prep
%setup

# Remove bundled egg-info
rm -rf %sname.egg-info

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

# Delete tests
rm -fr %buildroot%python_sitelibdir/*/test*
rm -fr %buildroot%python3_sitelibdir/*/test*

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%sname
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.14.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.14.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Oct 29 2015 Alexey Shabalin <shaba@altlinux.ru> 0.14.1-alt1
- Initial release

