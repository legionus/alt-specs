%define _unpackaged_files_terminate_build 1
%define dist IPTables-Parse
Name: perl-%dist
Version: 1.6
Release: alt1

Summary: Perl extension for parsing iptables firewall rulesets
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/MR/MRASH/IPTables-Parse-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Oct 20 2011
BuildRequires: perl-devel

%description
The IPTables::Parse package provides an interface to parse iptables rules
on Linux systems through the direct execution of iptables commands, or from
parsing a file that contains an iptables policy listing.  You can get the
current policy applied to a table/chain, look for a specific user-defined
chain, check for a default DROP policy, or determing whether or not logging
rules exist.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/IPTables

%changelog
* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated CPAN update

* Mon Sep 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1
- automated CPAN update

* Thu Oct 20 2011 Alexey Tourbin <at@altlinux.ru> 0.7-alt1
- initial revision
