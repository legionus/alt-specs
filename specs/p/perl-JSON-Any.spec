%define _unpackaged_files_terminate_build 1
%define dist JSON-Any
Name: perl-%dist
Version: 1.39
Release: alt1

Summary: Wrapper Class for the various JSON classes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETHER/JSON-Any-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Tue Nov 15 2011
BuildRequires: perl-JSON perl-JSON-DWIW perl-JSON-PP perl-Pod-Escapes perl-YAML-Syck perl-devel perl(Test/Requires.pm) perl(Test/Without/Module.pm) perl(Test/Fatal.pm) perl(Test/Warnings.pm) perl(namespace/clean.pm)

%description
This module tries to provide a coherent API to bring together the various
JSON modules currently on CPAN. This module will allow you to code to any
JSON API and have it work regardless of which JSON module is actually
installed.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/JSON

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.39-alt1
- automated CPAN update

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.36-alt1
- automated CPAN update

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Tue May 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.33-alt1
- automated CPAN update

* Wed Nov 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.30-alt1
- automated CPAN update

* Tue Nov 15 2011 Alexey Tourbin <at@altlinux.ru> 1.29-alt2
- rebuilt as plain src.rpm

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Apr 09 2010 Alexey Tourbin <at@altlinux.ru> 1.22-alt1
- 1.21 -> 1.22

* Sat Oct 03 2009 Michael Bochkaryov <misha@altlinux.ru> 1.21-alt1
- 1.21 version

* Sat Sep 06 2008 Michael Bochkaryov <misha@altlinux.ru> 1.17-alt1
- 1.17 version
- fix directory ownership violation

* Mon May 26 2008 Michael Bochkaryov <misha@altlinux.ru> 1.16-alt1
- first build for ALT Linux Sisyphus
