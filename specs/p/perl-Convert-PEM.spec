#
#   - Convert-PEM -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --spec-only Convert::PEM
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Convert-PEM
%define m_distro Convert-PEM
%define m_name Convert-PEM
%define m_author_id unknown
%define _enable_test 1

Name: perl-Convert-PEM
Version: 0.08
Release: alt1

Summary: Convert-PEM - Read/write encrypted ASN.1 PEM files

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/~btrott/Convert-PEM-0.07

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/B/BT/BTROTT/Convert-PEM-0.08.tar.gz

# Automatically added by buildreq on Sat Aug 27 2005
BuildRequires: perl-Class-ErrorHandler perl-Convert-ASN1 perl-Crypt-DES perl-Crypt-DES_EDE3 perl-Encode perl-Math-BigInt perl-devel

%description
This is Convert::PEM, a module implementing read/write access
to ASN.1-encoded PEM files (with optional encryption).

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Convert/

%changelog
* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt2
- fix directory ownership violation

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- first build for ALT Linux Sisyphus