%define oname logilab-database

%def_with python3

Name: python-module-%oname
Version: 1.15.0
Release: alt2
Summary: Provides some classes to make unified access to different RDBMS possible

Group: Development/Python
License: LGPLv2.1+
URL: http://www.logilab.org/project/logilab-database
# hg clone http://hg.logilab.org/logilab/database
Source: database-%version.tar
BuildArch: noarch

BuildRequires: python-module-logilab-common
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-logilab-common
%endif

%description
logilab-database provides some classes to make unified access to
different RDBMS possible:

* actually compatible db-api from different drivers to postgres, mysql,
  sqlite and sqlserver
* additional api for full text search
* extensions functions for common tasks such as creating database,
  index, users, dump and restore, etc...
* sql generation for INSERT/UPDATE/DELETE (in sqlgen.py)

%if_with python3
%package -n python3-module-%oname
Summary: Provides some classes to make unified access to different RDBMS possible (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
logilab-database provides some classes to make unified access to different
RDBMS possible:

* actually compatible db-api from different drivers to postgres, mysql,
  sqlite and sqlserver
* additional api for full text search
* extensions functions for common tasks such as creating database, index,
  users, dump and restore, etc...
* sql generation for INSERT/UPDATE/DELETE (in sqlgen.py)
%endif

%prep
%setup
touch test/__init__.py
%if_with python3
rm -rf ../python3
cp -a . ../python3
touch ../python3/test/__init__.py
%endif

%build
%python_build
%if_with python3
pushd ../python3
cp setup.py setup.py.bak
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
mv -f setup.py.bak setup.py
%python3_build
popd
%endif

%install
%python_install
rm -f %buildroot%python_sitelibdir/logilab/__init__.py*
%if_with python3
pushd ../python3
%python3_install
popd
rm -f %buildroot%python3_sitelibdir/logilab/__init__.py*
%endif

%files
%doc ChangeLog README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog README
%python3_sitelibdir/*
%endif

%changelog
* Thu Oct 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15.0-alt2
- Rebuilt with updated setuptools.

* Mon Oct 16 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.15.0-alt1
- Updated to upstream version 1.15.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.13.2-alt1.hg20150318.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.13.2-alt1.hg20150318.1
- NMU: Use buildreq for BR.

* Wed Mar 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13.2-alt1.hg20150318
- Version 1.13.2

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13.1-alt1.hg20150105
- Version 1.13.1

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.2-alt1.hg20140513
- Version 1.12.2

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1.hg20131009
- Version 1.10.0

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt2.hg20130321
- Use 'find... -exec...' instead of 'for ... $(find...'

* Mon Apr 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.9.0-alt1.hg20130321
- Version 1.9.0

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1.8.2-alt1.hg20120210.1
- Rebuild with Python-3.3

* Fri Jun 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.2-alt1.hg20120210
- Initial build for Sisyphus

