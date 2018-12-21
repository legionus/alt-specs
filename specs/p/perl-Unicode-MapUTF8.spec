#
#   - Unicode::MapUTF8 -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --version=1.11 Unicode::MapUTF8 Unicode-MapUTF8-1.11.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Unicode-MapUTF8
%define m_distro Unicode-MapUTF8
%define m_name Unicode::MapUTF8
%define m_author_id unknown
%define _enable_test 1

Name: perl-Unicode-MapUTF8
Version: 1.11
Release: alt2.1

Summary: Unicode-MapUTF8 - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Slava Dubrovskiy <dubrsl@altlinux.ru>

BuildArch: noarch
Source: %m_distro-%version.tar.gz

# Automatically added by buildreq on Wed Nov 22 2006
BuildRequires: perl-Encode-JP perl-Jcode perl-Module-Build perl-Test-Pod perl-Unicode-Map perl-Unicode-Map8

%description
None.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Unicode

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.11-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 11 2008 Slava Dubrovskiy <dubrsl@altlinux.org> 1.11-alt2
- Fix build

* Wed Nov 22 2006 Slava Dubrovskiy <dubrsl@altlinux.ru> 1.11-alt1
- first build for ALT Linux Sisyphus

