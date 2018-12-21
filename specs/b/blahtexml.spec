Name: blahtexml
Version: 0.9
Release: alt1

Summary: TeX / MathML converter

Group: Office
License: GPLv2+
Url: http://gva.noekeon.org/blahtexml/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://gva.noekeon.org/blahtexml/blahtexml-%version-src.tar
Patch: blahtexml-0.9-alt-unistd.patch

# Automatically added by buildreq on Mon Feb 08 2010
BuildRequires: gcc-c++ libxerces-c-devel

%description
Blahtex is a program written in C++, which converts an equation given in a
syntax close to TeX into MathML. It is designed by David Harvey and is aimed
at supporting equations in MediaWiki.
Blahtexml is a simple extension of blahtex. In addition to the functionality
of blahtex, blahtexml has XML processing in mind and is able to process a
whole XML document into another XML document. Instead of converting only one
formula at a time, blahtexml can convert all the formulas of the given XML
file into MathML.

%prep
%setup
%patch -p2

%build
%make_build blahtexml-linux

%install
install -p -D -m0755 blahtexml %buildroot%_bindir/blahtexml

%files
%doc README Documentation/example?.xml
%_bindir/blahtexml

%changelog
* Sat Aug 03 2013 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt1
- new version 0.9 (with rpmrb script)

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6-alt1.1
- Fixed build with glibc 2.16

* Mon Feb 08 2010 Vitaly Lipatov <lav@altlinux.ru> 0.6-alt1
- initial build for ALT Linux Sisyphus

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Jasper Capel <jasper@fedoraproject.org> - 0.6-4
- Changes for review, by Michael Schwendt's suggestions: preserve timestamps
  when installing, use global compiler flags, dropped xerces-c dependency, in
  favour of automatic dependency generation.
* Wed Feb 25 2009 Jasper Capel <jasper@fedoraproject.org> - 0.6-3
- Added parallel build make flags, as Jon Levell suggested.
* Mon Feb 23 2009 Jasper Capel <jasper@fedoraproject.org> - 0.6-2
- Corrected Source0, Description and BuildRequires as Jeroen van Meeuwen suggested.
* Fri Feb 20 2009 Jasper Capel <jasper@fedoraproject.org> - 0.6-1
- Initial build
