#
#   - Config::Mini -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --debug Config::Mini
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Config-Mini
%define m_distro Config-Mini
%define m_name Config::Mini
%define m_author_id unknown
%define _enable_test 1

Name: perl-Config-Mini
Version: 0.04
Release: alt1.1.1

Summary: Very simple INI-style configuration parser

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Config-Mini/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org//CPAN/authors/id/J/JH/JHIVER/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon Aug 04 2008 (-bi)
BuildRequires: perl-devel

%description
Easy to use INI-style configuration files processing module.


%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%doc README LICENSE Changes
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Mon Aug 04 2008 Michael Bochkaryov <misha@altlinux.ru> 0.04-alt1
- first build for ALT Linux Sisyphus

