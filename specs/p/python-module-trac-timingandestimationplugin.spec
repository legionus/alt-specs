%define tarname timingandestimationplugin_branches_trac0.12-Permissions
Name: python-module-trac-timingandestimationplugin
%define r_minor r14061
Version: 1.3.7b
Release: alt1.%r_minor

Summary: Plugin to make Trac support time estimation and tracking with permissions

Group: Development/Python
# FIXME: unknown?
License: http://www.opensource.org/licenses/mit-license.php
Url: http://trac-hacks.org/wiki/TimingAndEstimationPlugin

Source: %{tarname}-%r_minor.zip

BuildArch: noarch

# manually removed: python-module-Pyrex python-module-Rabbyt python-module-lxml
# Automatically added by buildreq on Sun Jan 06 2008
BuildRequires: python-module-MySQLdb python-module-ruledispatch python-module-setuptools unzip

%description
Plugin to make Trac support time estimation and tracking with permissions

%prep
%setup -n timingandestimationplugin

%build
%python_build

%install
%python_install

#Fix rights for template
chmod -R a+r %buildroot%python_sitelibdir/timingandestimationplugin/htdocs
chmod -R a+r %buildroot%python_sitelibdir/timingandestimationplugin/templates

%files
%doc
%python_sitelibdir/*

%changelog
* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7b-alt1.r14061
- Version 1.3.7b

* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.6b-alt1.r9433.1
- Rebuild with Python-2.7

* Tue Nov 16 2010 Slava Dubrovskiy <dubrsl@altlinux.org> 1.0.6b-alt1.r9433
- Build for ALT
