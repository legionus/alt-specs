%define dist Eval-Closure
Name: perl-%dist
Version: 0.14
Release: alt1

Summary: Safely and cleanly create closures via string eval
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/D/DO/DOY/Eval-Closure-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 18 2011
BuildRequires: perl-PadWalker perl-Test-Fatal perl-Test-Output perl-Test-Requires perl-Test-Script

%description
String eval is often used for dynamic code generation. For instance, Moose
uses it heavily, to generate inlined versions of accessors and constructors,
which speeds code up at runtime by a significant amount. String eval is not
without its issues however - it's difficult to control the scope it's used
in (which determines which variables are in scope inside the eval), and it
can be quite slow, especially if doing a large number of evals.

This module attempts to solve both of those problems. It provides an
eval_closure function, which evals a string in a clean environment, other
than a fixed list of specified variables. It also caches the result of the
eval, so that doing repeated evals of the same source, even with a different
environment, will be much faster (but note that the description is part of
the string to be evaled, so it must also be the same (or non-existent)
if caching is to work properly).

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Eval

%changelog
* Sun Jun 05 2016 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Mon Sep 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.08-alt1
- 0.06 -> 0.08
- fixed build with perl-5.16

* Fri Nov 18 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt2
- rebuilt to disable dependency on Perl::Tidy

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- initial build for ALT Linux Sisyphus
