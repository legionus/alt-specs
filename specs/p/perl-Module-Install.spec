%define _unpackaged_files_terminate_build 1
%define dist Module-Install
Name: perl-%dist
Version: 1.19
Release: alt1

Summary: Standalone, extensible Perl module installer
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# ignore CPANPLUS for now
%filter_from_requires /CPANPLUS/d

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Archive-Tar perl-File-Remove perl-JSON perl-Module-CoreList perl-Module-ScanDeps perl-PAR-Dist perl-Parse-CPAN-Meta perl-Pod-Escapes perl-YAML-Tiny perl(autodie.pm)

%description
This module provides a drop-in replacement for ExtUtils::MakeMaker.
For first-time users, Brian Ingerson's Creating Module Distributions
with Module::Install in June 2003 issue of The Perl Journal
http://www.tpj.com/issues/ provides a gentle introduction to how this
module works.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

mkdir -p %buildroot/etc/buildreqs/files/ignore.d
cat <<EOF >%buildroot/etc/buildreqs/files/ignore.d/%name
# %name buildreq filter.
^%perl_vendor_privlib/inc/Module/Install
EOF

%files
%doc Changes README
%perl_vendor_privlib/Module
%perl_vendor_privlib/inc
/etc/buildreqs/files/ignore.d/%name

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1
- automated CPAN update

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1
- automated CPAN update

* Sat Mar 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.08-alt1
- automated CPAN update

* Sat Sep 29 2012 Vladimir Lettiev <crux@altlinux.ru> 1.06-alt1
- 1.04 -> 1.06

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 1.02 -> 1.04
- reverted all previous changes
- added buildreq filter for */inc/Module/Install*

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.00 -> 1.02

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- 0.95 -> 1.00

* Mon Mar 29 2010 Alexey Tourbin <at@altlinux.ru> 0.95-alt2
- Metadata.pm: enabled dependency on Pod::Escapes

* Wed Mar 17 2010 Alexey Tourbin <at@altlinux.ru> 0.95-alt1
- 0.77 -> 0.95

* Wed Nov 05 2008 Alexey Tourbin <at@altlinux.ru> 0.77-alt3
- Module/Install/Makefile.pm: do not add configure_requires
  dependency on current ExtUtils::MakeMaker version

* Mon Oct 13 2008 Alexey Tourbin <at@altlinux.ru> 0.77-alt2
- eliminate dependency on Module::CoreList (again)

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 0.77-alt1
- 0.67 -> 0.77

* Tue Aug 14 2007 Alexey Tourbin <at@altlinux.ru> 0.67-alt1
- 0.64 -> 0.67

* Wed Oct 25 2006 Alexey Tourbin <at@altlinux.ru> 0.64-alt1
- 0.36 -> 0.64
- imported sources into git and build with gear
- hacked for use with rpm; the following features are disabled
  when RPM_ARCH and RPM_OS environment variables are set:
  + skip autoinstall
  + skip even version check, except for core features
  + skip includes
  + skip scan_dependencies
- hid CPAN and CPANPLUS dependencies with eval blocks

* Sat Sep 10 2005 Alexey Tourbin <at@altlinux.ru> 0.36-alt1
- initial revision
