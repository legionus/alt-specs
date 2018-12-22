Name: perl-PPerl
Version: 0.25
Release: alt4.1.1.1.1

Summary: Make perl scripts persistent in memory
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: http://search.cpan.org/dist/PPerl/
Source: PPerl-%version.tar.gz

Patch0: PPerl-0.25-alt-djbish.patch
Patch1: PPerl-0.25-alt-umask.patch
Patch2: PPerl-0.25-alt-Makefile.patch
Patch3: PPerl-0.25-pperl_euid.patch
Patch4: pperl-0.25-64bit.patch
Patch5: PPerl-0.25-misc_fix.patch
Patch6: PPerl-0.25-alt-logfile_help.patch
Patch7: PPerl-0.25-alt-test14.patch

# Automatically added by buildreq on Wed Aug 08 2007
BuildRequires: libdb4-devel libgdbm-devel perl-DBM perl-devel

%description
This program turns ordinary perl scripts into long running daemons, making
subsequent executions extremely fast. It forks several processes for each
script, allowing many proceses to call the script at once.

%prep
%setup -q -n PPerl-%version
%patch0
%patch1
%patch2
%patch3
%patch4 -p1
%patch5
%patch6
%patch7
mv t/13pid.t t/13.pid.t.failed

# Tests used deprecated in 5.12 goto operator
rm t/06exit_die.t
rm t/09taint.t
rm t/10tie.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%_bindir/pperl
%perl_vendor_archlib/PPerl*
%perl_vendor_autolib/PPerl

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt4.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt4.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.25-alt4.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt4.1
- rebuild with new perl 5.20.1

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt3
- rebuilt for perl-5.16
- temporary removed failed test

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 0.25-alt2.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.25-alt2.1
- rebuilt with perl 5.12

* Thu Jul 16 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt2
- Fix build with perl-5.8.9-alt3

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt1
- Initial build for ALT Linux Sisyphus

* Wed Aug 08 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.25-alt0
- Rebuild on current Sisyphus
- Adding current patches from rt.cpan.org

* Mon Jan 10 2005 Nikolay A. Fetisov <naf@naf.net.ru> 0.25-naf1
- First build

