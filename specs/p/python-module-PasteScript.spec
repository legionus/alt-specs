%define _unpackaged_files_terminate_build 1

%define oname PasteScript

%def_without bootstrap

Name: python-module-%oname
Epoch:   1
Version: 2.0.2
Release: alt1
Summary: A pluggable command-line frontend
License: MIT/X11
Group: Development/Python
Url: https://pypi.org/project/PasteScript/

BuildArch: noarch

Source: %oname-%version.tar

Patch1: %oname-%version-alt-deps.patch

Conflicts: python-module-paste.script
Obsoletes: python-module-paste.script
%py_provides %oname

%if_without bootstrap
BuildRequires: python-module-PasteDeploy
BuildRequires: python3-module-PasteDeploy
BuildRequires: python-module-paste
BuildRequires: python3-module-paste
BuildRequires: python2.7(Cheetah)
BuildRequires: python3(Cheetah)
%endif

BuildRequires: python-module-sphinx python-module-Pygments

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx python3-module-Pygments

%if_without bootstrap
%py_requires Cheetah
%endif

%description
A pluggable command-line frontend, including commands to setup
package file layouts.

%package -n python3-module-%oname
Summary: A pluggable command-line frontend (Python 3)
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip new
%if_with bootstrap
%add_python3_req_skip paste.deploy paste.deploy.converters paste.translogger
%add_python3_req_skip paste.util paste.util.template paste.wsgilib
%endif

%if_without bootstrap
%py3_requires Cheetah
%endif

%description -n python3-module-%oname
A pluggable command-line frontend, including commands to setup
package file layouts.

%prep
%setup -n %oname-%version
%patch1 -p2

cp -a . ../python3

%build
export PYTHONPATH=$PWD
pushd ../python3
sed -i 's|%_bindir/env python|%_bindir/env python3|' \
	tests/test_logging_config.py scripts/paster
%python3_build
popd

%python_build
./regen-docs

%install
pushd ../python3
%python3_install
mv %buildroot%_bindir/paster %buildroot%_bindir/paster3
popd

%python_install

%files
%doc docs/_build/*
%python_sitelibdir/paste/script
%python_sitelibdir/%oname-*
%_bindir/paster

%files -n python3-module-%oname
%_bindir/paster3
%python3_sitelibdir/paste/script
%python3_sitelibdir/%oname-*

%changelog
* Thu Aug 09 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:2.0.2-alt1
- Updated to upstream version 2.0.2.

* Mon May 28 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.7.5-alt4.2
- fix requires

* Thu May 24 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.7.5-alt4.1
- rebuild with all requires

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1:1.7.5-alt4
- rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1:1.7.5-alt3.hg20120208.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.5-alt3.hg20120208
- Avoid check version of Paste when build another packages

* Mon Apr 15 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.5-alt2.hg20120208
- Use 'find... -exec...' instead of 'for ... $(find...'

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 1:1.7.5-alt1.hg20120208.1
- Rebuild with Python-3.3

* Fri May 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.5-alt1.hg20120208
- New snapshot
- Added module for Python 3

* Thu Dec 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.5-alt1.hg20111107
- Version 1.7.5

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:1.7.4-alt1.hg20110427.1.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.4-alt1.hg20110427.1
- Added %%py_provides PasteScript

* Tue May 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.4-alt1.hg20110427
- New snapshot

* Wed Nov 24 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:1.7.4-alt1.hg20101117
- New snapshot
- Change upstream repository from svn to hg

* Thu Nov 19 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.svn20090922.2
- Rebuilt with python 2.6

* Tue Sep 29 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.4-alt1.svn20090922.1
- Version 1.7.4

* Sun Apr 05 2009 Denis Klimov <zver@altlinux.org> 1.7.3-alt1
- Initial build for ALT Linux


