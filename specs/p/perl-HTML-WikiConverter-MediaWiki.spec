#
#   - HTML::WikiConverter::MediaWiki -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       HTML::WikiConverter::MediaWiki
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module HTML-WikiConverter-MediaWiki
%define m_distro HTML-WikiConverter-MediaWiki
%define m_name HTML::WikiConverter::MediaWiki
%define m_author_id unknown
%define _enable_test 1

Name: perl-HTML-WikiConverter-MediaWiki
Version: 0.59
Release: alt2

Summary: Convert HTML to MediaWiki markup

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/D/DI/DIBERRI/%m_distro-%version.tar
Patch: HTML-WikiConverter-MediaWiki-0.59-alt-perl5.26.patch

# Automatically added by buildreq on Thu Jan 03 2008
BuildRequires: perl-HTML-WikiConverter perl-Test-Pod perl-Test-Pod-Coverage

%description
This module contains rules for converting HTML into MediaWiki
markup. See HTML::WikiConverter for additional usage details.

%prep
%setup -n %m_distro-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/HTML/

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.59-alt2
- fixed build with new perl 5.26

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.59-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Feb 03 2010 Vitaly Lipatov <lav@altlinux.ru> 0.59-alt1
- new version 0.59 (with rpmrb script)

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.55-alt2
- fix directory ownership violation

* Thu Jan 03 2008 Vitaly Lipatov <lav@altlinux.ru> 0.55-alt1
- first build for ALT Linux Sisyphus

