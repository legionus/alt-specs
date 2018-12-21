Name: perl-Git-Repository
Version: 1.323
Release: alt1

Summary: Git::Repository - Perl interface to Git repositories
Group: Development/Perl
License: Perl

Url: %CPAN Git-Repository
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel perl-System-Command perl-Module-Build git-core perl(Git/Version/Compare.pm) perl(Test/Requires/Git.pm) perl(namespace/clean.pm)

%description
%summary

%prep
%setup -q

%build
git config --global user.email "hasher@example.com"
git config --global user.name "Hasher Bot"
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Git/Repository*
%perl_vendor_privlib/Test/Git.pm
%doc Changes README

%changelog
* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 1.323-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 1.322-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 1.321-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.320-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.319-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 1.318-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.317-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1.316-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.315-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.312-alt1
- automated CPAN update

* Sat Jun 28 2014 Igor Vlasenko <viy@altlinux.ru> 1.311-alt1
- automated CPAN update

* Tue Aug 06 2013 Vladimir Lettiev <crux@altlinux.ru> 1.307-alt1
- 1.307

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 1.26-alt1
- 1.25 -> 1.26

* Wed Apr 11 2012 Vladimir Lettiev <crux@altlinux.ru> 1.25-alt1
- 1.22 -> 1.25

* Mon Sep 19 2011 Vladimir Lettiev <crux@altlinux.ru> 1.22-alt1
- 1.20 -> 1.22

* Fri Jun 17 2011 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt1
- New version 1.20

* Thu Jun 02 2011 Vladimir Lettiev <crux@altlinux.ru> 1.18-alt1
- initial build
