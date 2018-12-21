%define _unpackaged_files_terminate_build 1
#
#   - Module::Starter::Smart -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       -debug Module::Starter::Smart
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Module-Starter-Smart
%define m_distro Module-Starter-Smart
%define m_name Module::Starter::Smart
%define m_author_id unknown
%define _enable_test 1

Name: perl-Module-Starter-Smart
Epoch: 1
Version: 0.0.9
Release: alt1

Summary: Add new modules into an existing distribution with this plugin

License: Artistic
Group: Development/Perl
Url: %CPAN %m_distro

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/R/RU/RUEYCHENG/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 27 2009 (-bi)
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage perl-version perl-parent perl(Module/Starter/Simple.pm) perl(Test/TempDir/Tiny.pm)

%description
Module::Starter::Smart is a simple helper plugin for Module::Starter.
It overrides the "create_distro", "create_modules", and "create_t"
subroutines defined in whichever engine plugin in use (say,
Module::Starter::Simple.)  When invoked with a existing distribution,
the plugin may bypass the "create_basedir" subroutine, pull in a list
of existing modules as well as test files, create new modules, and
recreate the manifest file accordingly.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Module/*
%doc Changes README

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.0.9-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1:0.0.8-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 1:0.0.6-alt1
- automated CPAN update

* Wed Jan 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.0.5-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1:0.0.4-alt1
- automated CPAN update

* Thu Jul 15 2010 Igor Vlasenko <viy@altlinux.ru> v0.0.2-alt1
- automated CPAN update

* Tue Oct 27 2009 Michael Bochkaryov <misha@altlinux.ru> 0.0.2-alt1
- initial build for ALT Linux Sisyphus
