%define _unpackaged_files_terminate_build 1
Name: perl-CPAN-Perl-Releases
Version: 3.84
Release: alt1

Summary: Mapping Perl releases on CPAN to the location of the tarballs
Group: Development/Perl
License: perl

Url: %CPAN CPAN-Perl-Releases
Source: %name-%version.tar

BuildArch: noarch
BuildRequires: perl-devel

%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/CPAN/Perl/Releases*
%doc Changes LICENSE README

%changelog
* Thu Dec 13 2018 Igor Vlasenko <viy@altlinux.ru> 3.84-alt1
- automated CPAN update

* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 3.80-alt1
- automated CPAN update

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 3.78-alt1
- automated CPAN update

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 3.76-alt1
- automated CPAN update

* Mon Jul 02 2018 Igor Vlasenko <viy@altlinux.ru> 3.68-alt1
- automated CPAN update

* Tue Jun 26 2018 Igor Vlasenko <viy@altlinux.ru> 3.66-alt1
- automated CPAN update

* Wed Jun 20 2018 Igor Vlasenko <viy@altlinux.ru> 3.64-alt1
- automated CPAN update

* Wed Jun 13 2018 Igor Vlasenko <viy@altlinux.ru> 3.60-alt1
- automated CPAN update

* Wed May 23 2018 Igor Vlasenko <viy@altlinux.ru> 3.58-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 3.56-alt1
- automated CPAN update

* Sun Apr 15 2018 Igor Vlasenko <viy@altlinux.ru> 3.54-alt1
- automated CPAN update

* Thu Apr 05 2018 Igor Vlasenko <viy@altlinux.ru> 3.52-alt1
- automated CPAN update

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.50-alt1
- automated CPAN update

* Thu Feb 22 2018 Igor Vlasenko <viy@altlinux.ru> 3.48-alt1
- automated CPAN update

* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 3.42-alt1
- automated CPAN update

* Sun Oct 01 2017 Igor Vlasenko <viy@altlinux.ru> 3.38-alt1
- automated CPAN update

* Wed May 10 2017 Igor Vlasenko <viy@altlinux.ru> 3.14-alt1
- automated CPAN update

* Fri Feb 17 2017 Igor Vlasenko <viy@altlinux.ru> 3.08-alt1
- automated CPAN update

* Sun Jan 15 2017 Igor Vlasenko <viy@altlinux.ru> 3.06-alt1
- automated CPAN update

* Tue Dec 20 2016 Igor Vlasenko <viy@altlinux.ru> 3.00-alt1
- automated CPAN update

* Fri Nov 18 2016 Igor Vlasenko <viy@altlinux.ru> 2.98-alt1
- automated CPAN update

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 2.94-alt1
- automated CPAN update

* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 2.88-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 2.78-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 2.60-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 2.58-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 2.48-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 2.42-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 2.38-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 2.02-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.00-alt1
- automated CPAN update

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1
- automated CPAN update

* Thu Jun 26 2014 Igor Vlasenko <viy@altlinux.ru> 1.76-alt1
- automated CPAN update

* Tue Sep 10 2013 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- 0.72 -> 1.42

* Wed Oct 10 2012 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt1
- initial build for ALTLinux

