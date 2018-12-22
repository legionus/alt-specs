%define _unpackaged_files_terminate_build 1
%define dist Data-Dumper-Concise
Name: perl-%dist
Version: 2.023
Release: alt1

Summary: Less indentation and newlines plus sub deparsing
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/E/ET/ETHER/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Devel-ArgNames perl-Pod-Escapes perl-devel

%description
This module always exports a single function, Dumper, which can be called
with an array of values to dump those values or with no arguments to
return the Data::Dumper object it's created.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Data*
%perl_vendor_privlib/Devel*

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 2.023-alt1
- automated CPAN update

* Mon Mar 24 2014 Igor Vlasenko <viy@altlinux.ru> 2.022-alt1
- automated CPAN update

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 2.021-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 2.020-alt2
- disabled build dependency on perl-Module-Install

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 2.020-alt1
- automated CPAN update

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 1.200-alt1
- initial revision, for perl-DBIx-Class
