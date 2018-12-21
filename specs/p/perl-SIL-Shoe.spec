#
#   - SIL::Shoe -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       SIL::Shoe
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module SIL-Shoe
%define m_distro SIL-Shoe
%define m_name SIL::Shoe
%define m_author_id unknown
%define _enable_test 1

Name: perl-SIL-Shoe
Version: 1.37
Release: alt3

Summary: Shoebox support utilities

License: Artistic
Group: Text tools
Url: http://www.cpan.org

Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch
Source: %m_distro-%version.tar
Patch0: SIL-Shoe-perl-522.patch
Patch1: SIL-Shoe-perl-526.patch

# Automatically added by buildreq on Mon Mar 30 2009 (-bi)
BuildRequires: perl-Algorithm-Merge perl-Encode-CN perl-Encode-JP perl-Encode-KR perl-Encode-Registry perl-Encode-TECkit perl-Encode-TW perl-Image-Size perl-OpenOffice-OODoc perl-Unicode-Collate perl-XML-XPath perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This module has support for SIL Shoebox and SIL Toolbox files that are stored using Standard Format which is a textual format in which a field is marked by a Standard Format Marker (SFM) at the start of a line. An SFM is simply \ followed by some non space characters.

A key field marker is used to mark the start of a record. Records may have multiple key fields with the same contents and a field marker (other than the key field marker) may occur multiple times within a record.

In addition to the core data, there are various settings files that facilitate the database program itself. This module interacts with those as well.

Scripts that come with the module are key programs: cvs2sh, sh2cvs, sh2sh, sh2xml, shadd, shdiff3, shdiffn, shed, shintr, shlex, sh_rtf, zipdiff, zipmerge, zippatch

%prep
%setup -q -n %m_distro-%version
%patch0 -p1
%patch1 -p1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install
# upstream distribution contains verbatim copy of file from Unicode::Collate,
# FIXME: better to remove it before building but that require  patching of Makefile.PL
rm -vf %buildroot%perl_vendor_privlib/Unicode/Collate/allkeys.txt
# we don't need win32-specific stuff
rm -vf %buildroot%_bindir/{addpath,zvs.bat}
# avoid name clash with libzip and other possible clashes
pushd %buildroot%_bindir
for f in zip* ; do mv "$f" "sh${f}" ; done
popd

%files
%_bindir/*
%perl_vendor_privlib/SIL/*
%perl_vendor_privlib/Text/*
%_man1dir/*
%doc readme.txt docs/* README.ALT.txt

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.37-alt3
- fixed build with new perl 5.26

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 1.37-alt2.2
- bugfixes for perl 5.22 (SIL-Shoe-perl-522.patch)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.37-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Apr 03 2009 Kirill Maslinsky <kirill@altlinux.org> 1.37-alt2
- avoid filename conflict with libzip (zipmerge)
  zipmerge, zipdiff, zippatch renamed to shzipmerge, shzipdiff, shzippatch
- add README.ALT.txt describing this change

* Mon Mar 30 2009 Kirill Maslinsky <kirill@altlinux.ru> 1.37-alt1
- initial build for ALT Linux Sisyphus

