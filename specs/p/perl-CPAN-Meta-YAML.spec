%define _unpackaged_files_terminate_build 1
# fresh Test::More -not in perl 5.18.2
%def_without test
%define dist CPAN-Meta-YAML
Name: perl-%dist
Version: 0.018
Release: alt1

Summary: Read and write a subset of YAML for CPAN Meta files
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DA/DAGOLDEN/CPAN-Meta-YAML-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Nov 14 2011
BuildRequires: perl-YAML perl-YAML-Syck perl-devel


%description
This module implements a subset of the YAML specification for use in
reading and writing CPAN metadata files like META.yml and MYMETA.yml.
It should not be used for any other general YAML parsing or generation
task.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/CPAN

%changelog
* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.018-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.016-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.014-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.012-alt1
- automated CPAN update

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.010-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 0.004-alt1
- initial revision
