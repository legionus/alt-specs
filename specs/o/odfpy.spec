Name: odfpy
Version: 1.3.6
Release: alt1
Summary: Python scripts for manipulating OpenDocument files

Group: Development/Python
License: GPLv2+
Url: https://joinup.ec.europa.eu/software/odfpy/home

# Source-url: https://pypi.io/packages/source/o/%name/%name-%version.tar.gz
Source: %name-%version.tar.gz

%setup_python_module %name

BuildArch: noarch

# Automatically added by buildreq on Tue Feb 02 2010
BuildRequires: python-devel python-module-setuptools
BuildRequires: python3-devel python3-module-setuptools

%description
    csv2odf - Create OpenDocument spreadsheet from comma separated values
    mailodf - Email ODF file as HTML archive
    odf2xhtml - Convert ODF to (X)HTML
    odf2mht - Convert ODF to HTML archive
    odf2xml - Create OpenDocument XML file from OD? package
    odfimgimport - Import external images
    odflint - Check ODF file for problems
    odfmeta - List or change the metadata of an ODF file
    odfoutline - Show outline of OpenDocument
    odfuserfield - List or change the user-field declarations in an ODF file
    xml2odf - Create OD? package from OpenDocument in XML form

%package -n %packagename
Summary: Python library for manipulating OpenDocument files
Group: Development/Python
License: GPLv2+

%description -n %packagename
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.

These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.

%package -n python3-module-%name
Summary: Python3 library for manipulating OpenDocument files
Group: Development/Python3
License: GPLv2+

%description -n python3-module-%name
Odfpy aims to be a complete API for OpenDocument in Python. Unlike
other more convenient APIs, this one is essentially an abstraction
layer just above the XML format. The main focus has been to prevent
the programmer from creating invalid documents. It has checks that
raise an exception if the programmer adds an invalid element, adds an
attribute unknown to the grammar, forgets to add a required attribute
or adds text to an element that doesn't allow it.

These checks and the API itself were generated from the RelaxNG
schema, and then hand-edited. Therefore the API is complete and can
handle all ODF constructions, but could be improved in its
understanding of data types.

%prep
%setup -n %name-%version

%build
%python_build
%python3_build

%install
%python_install
%python3_install

%files -n %packagename
%docdir examples
%docdir contrib
%python_sitelibdir/*egg-info
%python_sitelibdir/odf/

%files
%_bindir/*
%_man1dir/*

%files -n python3-module-%name
%docdir examples
%docdir contrib
%python3_sitelibdir/*egg-info
%python3_sitelibdir/odf/

%changelog
* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 1.3.6-alt1
- Autobuild version bump to 1.3.6

* Mon Aug 14 2017 Fr. Br. George <george@altlinux.ru> 1.3.5-alt1
- Autobuild version bump to 1.3.5
- Introduce python3 module
- Separate binary module

* Sat Jul 22 2017 Vitaly Lipatov <lav@altlinux.ru> 1.3.4-alt1
- new version 1.3.4 (with rpmrb script)

* Tue Jul 26 2016 Fr. Br. George <george@altlinux.ru> 1.3.3-alt1
- Autobuild version bump to 1.3.3

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Tue May 21 2013 Fr. Br. George <george@altlinux.ru> 0.9.6-alt1
- Autobuild version bump to 0.9.6

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.9.2-alt1.1
- Rebuild with Python-2.7

* Tue Feb 02 2010 Vitaly Lipatov <lav@altlinux.ru> 0.9.2-alt1
- initial build for ALT Linux Sisyphus

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Ian Weller <ianweller@gmail.com> - 0.9-1
- Update upstream

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.8-2
- Rebuild for Python 2.6

* Fri Aug 22 2008 Ian Weller <ianweller@gmail.com> 0.8-1
- Update upstream

* Tue Jul 15 2008 Ian Weller <ianweller@gmail.com> 0.7-2
- Change macros
- Remove license file

* Sun Jul 13 2008 Ian Weller <ianweller@gmail.com> 0.7-1
- Add COPYING file
- Use setuptools instead
- sed out shebangs from module files
- Other minor fixes

* Sun Jul 13 2008 Paul W. Frields <stickster@gmail.com> - 0.7-0.1
- Initial RPM package
