%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build/Tiny.pm) perl(Sub/Identify.pm) perl(Test/Requires.pm) perl(Module/Build.pm)
%define dist namespace-autoclean
Name: perl-%dist
Version: 0.28
Release: alt1

Summary: Keep imports out of your namespace
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/namespace-autoclean-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sat Nov 19 2011
BuildRequires: perl-Moose perl-devel perl-namespace-clean perl(Test/CheckDeps.pm)

%description
When you import a function into a Perl package, it will naturally also be
available as a method.

The namespace::autoclean pragma will remove all imported symbols at the end
of the current package's compile cycle. Functions called in the package itself
will still be bound by their name, but they won't show up as methods on your
class or instances.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/namespace

%changelog
* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Mon Jan 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Mon Jun 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Wed Oct 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Sat Nov 19 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt2
- updated build dependencies

* Wed Oct 26 2011 Alexey Tourbin <at@altlinux.ru> 0.13-alt1
- 0.11 -> 0.13

* Wed May 26 2010 Alexey Tourbin <at@altlinux.ru> 0.11-alt1
- 0.09 -> 0.11

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.09-alt1
- initial revision, for DBIx::Class
