%define py3bdir ../%name-%version-python3-build
%define realversion 0.9.8

%def_with python3

Name: httpie
Version: 0.9.9
Release: alt1.qa1
Summary: A Curl-like tool for humans

Group: Networking/WWW
License: BSD
Url: http://httpie.org
Source0: %name-%version.tar
Patch0: %name-%version-system-urllib3.patch
BuildRequires: python-devel python-module-Pygments python-module-requests help2man python-module-setuptools rpm-build-python python-modules-json
BuildArch: noarch

Requires: python-module-requests >= 2.11.0
Requires: python-module-Pygments >= 2.1.3

%if_with python3
BuildRequires: python3-dev python3-module-Pygments python3-module-requests
BuildRequires: python3-module-setuptools rpm-build-python3
%endif

%description
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.

%if_with python3
%package -n httpie-python3
Summary: A Curl-like tool for humans
Group: Networking/WWW

Requires: python3-module-requests >= 2.11.0
Requires: python3-module-Pygments >= 2.1.3

%description -n httpie-python3
HTTPie is a CLI HTTP utility built out of frustration with existing tools. The
goal is to make CLI interaction with HTTP-based services as human-friendly as
possible.

HTTPie does so by providing an http command that allows for issuing arbitrary
HTTP requests using a simple and natural syntax and displaying colorized
responses.
%endif

%prep
%setup
%patch0 -p0
sed -i '/#!\/usr\/bin\/env/d' %name/__main__.py

%if_with python3
rm -rf %py3bdir
cp -a . %py3bdir
%endif

%build
python setup.py build

%if_with python3
pushd %py3bdir
python3 setup.py build
popd
%endif

%install
%if_with python3
pushd %py3bdir
python3 setup.py install --skip-build --root %buildroot
mv %buildroot%_bindir/http %buildroot%_bindir/http.python3
popd
%endif

python setup.py install --root %buildroot

mkdir -p %buildroot/%_man1dir
export PYTHONPATH=%buildroot%python_sitelibdir
help2man --no-discard-stderr %buildroot/%_bindir/http > %buildroot/%_man1dir/http.1

%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
help2man --no-discard-stderr %buildroot/%_bindir/http.python3 > %buildroot/%_man1dir/http.python3.1
%endif

%files
%_bindir/http
%python_sitelibdir/%name
%python_sitelibdir/%name-%{realversion}*
%_man1dir/http.1.*
%doc LICENSE README.rst

%if_with python3
%files -n httpie-python3
%_bindir/http.python3
%python3_sitelibdir/%name
%python3_sitelibdir/%name-%{realversion}*
%_man1dir/http.python3.1.*
%doc LICENSE README.rst
%endif

%changelog
* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.9.9-alt1.qa1
- NMU: applied repocop patch

* Fri Sep 21 2018 Terechkov Evgenii <evg@altlinux.org> 0.9.9-alt1
- 0.9.9

* Wed Jul 18 2018 Grigory Ustinov <grenka@altlinux.org> 0.9.8-alt3
- Fixed FTBFS (Add BR python3-module-setuptools).

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt2
- Update requires
- Added patch - fixed import 'urllib3'

* Wed Jul 19 2017 Evgeniy Korneechev <ekorneechev@altlinux.org> 0.9.8-alt1
- Build new version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Sep  6 2014 Terechkov Evgenii <evg@altlinux.org> 0.8.0-alt1
- Initial build for ALT Linux Sisyphus
