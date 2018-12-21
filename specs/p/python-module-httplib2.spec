%define packagename python-module-httplib2
%define origname httplib2

%def_with python3

Summary: A comprehensive HTTP client library in Python
Name: %packagename
Version: 0.9.1
Release: alt1.2
Source0: %origname-%version.tar.gz
License: MIT
Group: Development/Python
URL: http://code.google.com/p/httplib2/
BuildArch: noarch

# Automatically added by buildreq on Sat Apr 05 2008
BuildRequires: python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
%endif

%description
A comprehensive HTTP client library that supports many features left out
of other HTTP libraries.

%if_with python3
%package -n python3-module-%origname
Summary: A comprehensive HTTP client library in Python 3
Group: Development/Python3

%description -n python3-module-%origname
A comprehensive HTTP client library that supports many features left out
of other HTTP libraries.
%endif

%prep
%setup  -n %origname-%version
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


%files
#doc CHANGELOG *.html *.md doc/html
%python_sitelibdir/%origname/
%python_sitelibdir/*.egg-info

%if_with python3
%files -n python3-module-%origname
#doc CHANGELOG *.html *.md doc/html
%python3_sitelibdir/*
%endif


%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.9.1-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Aug 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1
- Version 0.9.1

* Thu Aug 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Version 0.9

* Tue Dec 03 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1
- Version 0.8

* Sun Mar 24 2013 Aleksey Avdeev <solo@altlinux.ru> 0.7.7-alt1.1
- Rebuild with Python-3.3

* Thu Feb 14 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.7-alt1
- Version 0.7.7

* Mon Jun 11 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.4-alt1
- Version 0.7.4

* Sat May 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1.1
- Rebuilt with python 2.6

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.5.0-alt1
- Building 0.5.0-alt instead of 0.4.0-alt2. Version up + fixed packaging errors.

* Mon Sep 28 2009 Mikhail Pokidko <pma@altlinux.org> 0.4.0-alt2
- Fixing packaging errors.

* Wed Oct 08 2008 Mikhail Pokidko <pma@altlinux.org> 0.4.0-alt1
- Initial ALT build


