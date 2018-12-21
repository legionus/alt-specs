%define _unpackaged_files_terminate_build 1
%define dist ExtUtils-LibBuilder
Name: perl-%dist
Version: 0.08
Release: alt1

Summary: A tool to build C libraries
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/A/AM/AMBS/ExtUtils-LibBuilder-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-Module-Build perl-Test-Pod perl-Test-Pod-Coverage

%description
Some Perl modules need to ship C libraries together with their Perl
code. Although there are mechanisms to compile and link (or glue) C
code in your Perl programs, there isn't a clear method to compile
standard, self-contained C libraries.

This module main goal is to help in that task.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/ExtUtils

%changelog
* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision
