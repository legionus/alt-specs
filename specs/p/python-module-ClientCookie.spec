%define oname ClientCookie

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.2

Summary: Python module for handling HTTP cookies on the client side
Source0: %oname-%version.tar.gz
License: BSD
Group: Development/Python
Requires: python
Url: http://wwwsearch.sourceforge.net/ClientCookie
BuildRequires: python-devel python-module-setuptools
Provides: python-%oname
Obsoletes: python-%oname
BuildArch: noarch

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
ClientCookie is a Python module for handling HTTP cookies on the
client side, useful for accessing web sites that require cookies to be
set and then returned later. It also provides some other (optional)
useful stuff: HTTP-EQUIV and Refresh handling, automatic adding of the
Referer [sic] header and lazily-seek()able responses. These extras are
implemented using an extension that makes it easier to add new
functionality to urllib2. It has developed from a port of Gisle Aas'
Perl module HTTP::Cookies, from the [4]libwww-perl library.

%package -n python3-module-%oname
Summary: Python module for handling HTTP cookies on the client side
Group: Development/Python3
%add_python3_req_skip bsddb

%description -n python3-module-%oname
ClientCookie is a Python module for handling HTTP cookies on the
client side, useful for accessing web sites that require cookies to be
set and then returned later. It also provides some other (optional)
useful stuff: HTTP-EQUIV and Refresh handling, automatic adding of the
Referer [sic] header and lazily-seek()able responses. These extras are
implemented using an extension that makes it easier to add new
functionality to urllib2. It has developed from a port of Gisle Aas'
Perl module HTTP::Cookies, from the [4]libwww-perl library.

%prep
%setup -n %oname-%version

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install --record=INSTALLED_FILES

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files -f INSTALLED_FILES
%doc *.html *.txt

%if_with python3
%files -n python3-module-%oname
%doc *.html *.txt
%python3_sitelibdir/*
%endif

%changelog
* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.3.0-alt1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Aug 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1
- Version 1.3.0
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt0.1.1.1.1.1.1
- Rebuild with Python-2.7

* Fri Nov 13 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt0.1.1.1.1.1
- Rebuilt with python 2.6
- Built as noarch

* Thu Jan 24 2008 Grigory Batalov <bga@altlinux.ru> 1.0.2-alt0.1.1.1.1
- Rebuilt with python-2.5.

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt0.1.1.1
- Rebuilt using rpm-build-python-0.29-alt4.

* Tue Mar 29 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.2-alt0.1.1
- Rebuilt with python-2.4.

* Wed Jan 26 2005 Andrey Khavryuchenko <akhavr@altlinux.ru> 1.0.2-alt0.1
- Updated to 1.0.2

* Sat Aug 7 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.19-alt0.1
- Updated to 0.4.19

* Tue Jan 6 2004 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.18-alt0.1
- Updated to 0.4.18

* Tue Dec 30 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.14-alt0.1
- Updated to 0.4.14

* Wed Dec 17 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.11-alt0.1
- Updated to 0.4.11
- Updated to python 2.3

* Sun Dec 7 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.10-alt0.1
- Updated to 0.4.10

* Wed Nov 5 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.9-alt0.1
- Updated to 0.4.9

* Mon Sep 29 2003 Andrey Khavryuchenko <akhavr@altlinux.ru> 0.4.5a-alt0.1
  Initial build
