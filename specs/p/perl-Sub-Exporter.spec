#
#   - Sub-Exporter -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Sub::Exporter
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Sub-Exporter
%define m_distro Sub-Exporter
%define m_name Sub-Exporter
%define m_author_id unknown
%define _enable_test 1

Name: perl-Sub-Exporter
Version: 0.987
Release: alt1

Summary: a sophisticated exporter for custom-built routines

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Mikhail Pokidko <pma@altlinux.org>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Sub-Exporter-%{version}.tar.gz

# Automatically added by buildreq on Wed May 14 2008
BuildRequires: perl-Data-OptList perl-Module-Install perl-Package-Generator

%description
None.

%prep
%setup -q -n %module-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Sat Oct 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.987-alt1
- automated CPAN update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.986-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.982-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Mar 22 2010 Mikhail Pokidko <pma@altlinux.org> 0.982-alt2
- Fixed barewords and 'strict subs' usage

* Thu Nov 19 2009 Mikhail Pokidko <pma@altlinux.org> 0.982-alt1
- Pulling up 0.982 from upstream

* Thu Nov 19 2009 Mikhail Pokidko <pma@altlinux.org> 0.981-alt1
- Version up

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 0.979-alt2
- sisyphus_check fixes

* Wed May 14 2008 Mikhail Pokidko <pma@altlinux.org> 0.979-alt1
- first build for ALT Linux Sisyphus

