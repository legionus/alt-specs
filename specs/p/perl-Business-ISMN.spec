%define _unpackaged_files_terminate_build 1
#
#   - Business::ISMN -
#   This spec file was automatically generated by cpan2rpm [ver: 2.028]
#   (ALT Linux revision)
#   The following arguments were used:
#       Business::ISMN
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Business-ISMN
%define m_distro Business-ISMN
%define m_name Business::ISMN
%define m_author_id unknown
%define _enable_test 1

Name: perl-Business-ISMN
Version: 1.201
Release: alt1

Summary: Work with International Standard Music Numbers

License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Kirill Maslinsky <kirill@altlinux.org>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/B/BD/BDFOY/%{module}-%{version}.tar.gz

BuildRequires: perl-Module-Build perl-Tie-Cycle

%description
None.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.pod LICENSE Changes ismns.txt examples
%perl_vendor_privlib/Business/*

%changelog
* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 1.201-alt1
- automated CPAN update

* Fri Jul 20 2018 Igor Vlasenko <viy@altlinux.ru> 1.132-alt1
- automated CPAN update

* Sun Dec 18 2016 Igor Vlasenko <viy@altlinux.ru> 1.131-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1
- automated CPAN update

* Thu Jan 24 2013 Kirill Maslinsky <kirill@altlinux.org> 1.11-alt1
- initial build for ALT Linux Sisyphus
