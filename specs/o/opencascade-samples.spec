Name: opencascade-samples
Version: 6.8.0
Release: alt1
Summary: Samples for Open CASCADE
License: BSD-like
Group: Development/Documentation
Url: http://www.opencascade.org
BuildArch: noarch
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: OpenCASCADE_src.tar

%description
Open CASCADE Technology version 6.5.0, a minor release, which introduces quite a
number of new features and improved traditional functionality along with certain
changes over the previous public release and maintenance releases exclusively
available to the customers.

This package contains sample data for Open CASCADE.

%prep
%setup

%install
install -d %buildroot%_datadir/%name/samples
cp -fR * %buildroot%_datadir/%name/samples/

# It is the file in the package named Thumbs.db or Thumbs.db.gz, 
# which is normally a Windows image thumbnail database. 
# Such databases are generally useless in packages and were usually 
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT \( -name 'Thumbs.db' -o -name 'Thumbs.db.gz' \) -print -delete

%files
%dir %_datadir/%name
%_datadir/%name/samples

%changelog
* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.8.0-alt1
- Version 6.8.0

* Fri Sep 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.6.0-alt1
- Version 6.6.0

* Thu Feb 07 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.4-alt1
- Version 6.5.4

* Wed Aug 22 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.3-alt1
- Version 6.5.3

* Wed Feb 29 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.2-alt1
- Version 6.5.2

* Mon Oct 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.1-alt1
- Version 6.5.1

* Tue May 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt2
- Applied repocop patch: remove Thumbs.db*

* Mon May 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.5.0-alt1
- Version 6.5.0

* Wed Dec 23 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 6.3.0-alt1
- Initial build for Sisyphus

