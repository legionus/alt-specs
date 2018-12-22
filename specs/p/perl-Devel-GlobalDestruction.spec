%define _unpackaged_files_terminate_build 1
%define dist Devel-GlobalDestruction
Name: perl-%dist
Serial: 1
Version: 0.14
Release: alt1

Summary: Expose the flag which marks global destruction
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/H/HA/HAARG/Devel-GlobalDestruction-%{version}.tar.gz

BuildArch: noarch

# New global variable ${^GLOBAL_PHASE}
Requires: perl-base >= 1:5.14
BuildRequires: perl-base >= 1:5.14

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-Sub-Exporter perl-devel perl-Sub-Exporter-Progressive

%description
Perl's global destruction is a little tricky to deal with WRT finalizers
because it's not ordered and objects can sometimes disappear.

Writing defensive destructors is hard and annoying, and usually if global
destruction is happenning you only need the destructors that free up non
process local resources to actually execute.

For these constructors you can avoid the mess by simply bailing out if global
destruction is in effect.

%prep
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/Devel

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1:0.14-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1:0.13-alt1
- automated CPAN update

* Wed Nov 06 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.12-alt1
- automated CPAN update

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 1:0.11-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 0.011-alt1
- 0.009 -> 0.011

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.09-alt1
- 0.04 -> 0.09
- built for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.04-alt2
- rebuilt for perl-5.14
- now noarch

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.02-alt2.1
- rebuilt with perl 5.12

* Wed Apr 14 2010 Alexey Tourbin <at@altlinux.ru> 0.02-alt2
- fixed directory packaging

* Mon Oct 20 2008 Mikhail Pokidko <pma@altlinux.org> 0.02-alt1
- initial build for ALT Linux Sisyphus

