%define _unpackaged_files_terminate_build 1
#
#   - Archive::Any -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --debug --version 0.0932 Archive::Any
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Archive-Any
%define m_distro Archive-Any
%define m_name Archive::Any
%define m_author_id CMOORE
%define _enable_test 1

Name: perl-Archive-Any
Version: 0.0945
Release: alt1

Summary: Single interface to deal with file archives.

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Archive-Any/

BuildArch: noarch
Source: http://www.cpan.org/authors/id/O/OA/OALDERS/Archive-Any-%{version}.tar.gz

BuildRequires: perl-Archive-Tar
# Automatically added by buildreq on Wed Sep 03 2008 (-bi)
BuildRequires: perl-Archive-Any perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage perl-Test-Warn perl-version

%description
This module is a single interface for manipulating different archive formats.
Tarballs, zip files, etc.


%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Archive*

%changelog
* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.0945-alt1
- automated CPAN update

* Wed Apr 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.0944-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.0942-alt1
- automated CPAN update

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.0941-alt1
- automated CPAN update

* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.0940-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.0932-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 03 2008 Michael Bochkaryov <misha@altlinux.ru> 0.0932-alt2
- directory ownership bug fixed

* Fri Jun 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.0932-alt1
- first build for ALT Linux Sisyphus

