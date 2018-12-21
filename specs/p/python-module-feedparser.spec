Name: python-module-feedparser
Version: 5.2.1
Release: alt1
Epoch: 1

%define sname feedparser
%def_with doc

Summary: Universal feed parser for Python
Group: Development/Python
License: BSD-style
Url: https://github.com/kurtmckee/feedparser
BuildArch: noarch

%setup_python_module feedparser

BuildRequires: python-module-distribute
%{?_with_doc:BuildRequires: python-module-sphinx}

# http://feedparser.googlecode.com/files/feedparser-%version.tar.bz2
Source: %sname-%version.tar
Patch:  %sname-disable-test_gzip_struct_error.patch

%description
Universal feed parser is a Python module for downloading and parsing
syndicated feeds.  It can handle RSS 0.90, Netscape RSS 0.91,
Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0,
Atom 0.3, Atom 1.0, and CDF feeds.  It also parses several popular
extension modules, including Dublin Core and Apple's iTunes extensions.
It provides the same API to all formats, and sanitizes URIs and HTML.

%package doc
Summary: Documentation for the Universal feed parser for Python
Group: Development/Python
Requires: %name = %epoch:%version-%release

%description doc
This package contains documentation for the Universal feed parser.

%prep
%setup -n %sname-%version
#patch -p2
find -type f -print0 |
	xargs -r0 sed -i 's/\r//' --

%build
%python_build
%{?_with_doc:sphinx-build -b html docs html}

%install
%python_install

%define docdir %_docdir/%name
mkdir -p %buildroot%docdir
install -pm644 LICENSE NEWS README.rst %buildroot%docdir/
%{?_with_doc:cp -a html %buildroot%docdir/}

%check
# this test may fail, disable it
rm -f feedparser/tests/illformed/chardet/big5.xml

cd %sname
PYTHONPATH=%buildroot%python_sitelibdir %__python feedparsertest.py

%files
%python_sitelibdir/*
%dir %docdir
%docdir/[LNR]*

%if_with doc
%files doc
%dir %docdir
%docdir/html
%endif

%changelog
* Wed Nov 08 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:5.2.1-alt1
- Updated to upstream version 5.2.1.

* Sun Apr 21 2013 Andrey Cherepanov <cas@altlinux.org> 1:5.1.3-alt1.1
- Disable test_gzip_struct_error until http://bugs.python.org/issue1159051
  is completely fixed

* Wed Apr 03 2013 Dmitry V. Levin <ldv@altlinux.org> 1:5.1.3-alt1
- Updated to 5.1.3.

* Thu Sep 06 2012 Dmitry V. Levin <ldv@altlinux.org> 1:5.1.2-alt1
- Updated to 5.1.2.

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1:4.1-alt1.1
- Rebuild with Python-2.7

* Mon Feb 01 2010 Dmitry V. Levin <ldv@altlinux.org> 1:4.1-alt1
- Initial revision.
