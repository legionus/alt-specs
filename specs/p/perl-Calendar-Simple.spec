%define _unpackaged_files_terminate_build 1
#
#   - Calendar::Simple -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Calendar::Simple --version 1.13
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Calendar-Simple
%define m_distro Calendar-Simple
%define m_name Calendar::Simple
%define m_author_id unknown
%define _enable_test 1

Name: perl-Calendar-Simple
Version: 1.23
Release: alt2

Summary: Calendar-Simple - Perl module

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Vitaly Lipatov <lav@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/D/DA/DAVECROSS/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Fri Jun 23 2006
BuildRequires: perl-devel perl-Module-Build

%description
A very simple module that exports one function called calendar.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

# who need it?
rm -f %buildroot%_bindir/pcal

%files
%doc Changes README
%perl_vendor_privlib/Calendar/

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.23-alt2
- fixed unpackaged files

* Wed Mar 07 2018 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 1.20-alt2
- fix directory ownership violation

* Sat Jun 14 2008 Vitaly Lipatov <lav@altlinux.ru> 1.20-alt1
- new version 1.20 (with rpmrb script)

* Fri Jun 23 2006 Vitaly Lipatov <lav@altlinux.ru> 1.13-alt1
- initial build for ALT Linux Sisyphus
