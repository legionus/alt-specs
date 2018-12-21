%define _unpackaged_files_terminate_build 1
#
#   - Class-Unload -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       Class::Unload
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Class-Unload
%define m_distro Class-Unload
%define m_name Class-Unload
%define m_author_id ILMARI
%define _enable_test 1

Name: perl-Class-Unload
Version: 0.11
Release: alt1

Summary: Unload a class

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Class-Unload/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/I/IL/ILMARI/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Tue Apr 27 2010
BuildRequires: perl-Class-Inspector perl-devel perl(Test/Requires.pm)

%description
Unloads the given class by clearing out its symbol table and removing it
from %%INC. If it has no sub-namespaces, also deletes the reference from
the parent namespace.

%prep
%setup -q -n %{module}-%{version}
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Apr 27 2010 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- 0.03 -> 0.06

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1.1
- NMU for unknown reason:
  the person above was too neglectant to add --changelog "- NMU: <reason>" option.

* Wed Jun 04 2008 Michael Bochkaryov <misha@altlinux.ru> 0.03-alt1
- 0.03

* Wed Apr 16 2008 Michael Bochkaryov <misha@altlinux.ru> 0.02-alt1
- first build for ALT Linux Sisyphus
