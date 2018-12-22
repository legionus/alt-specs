%define dist Authen-Smb
Name: perl-%dist
Version: 0.91
Release: alt5.1.1.1.1

Summary: Perl extension to authenticate against an SMB server
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
Authen::Smb allows you to authenticate a user against an NT domain.
You can specify both a primary and a backup server to use for
authentication.  The NT names of the machines should be used for
specifying servers.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/Authen
%perl_vendor_archlib/Authen

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.91-alt5.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.91-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.91-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.91-alt5.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.91-alt5
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.91-alt4
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.91-alt3
- rebuilt for perl-5.14

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 0.91-alt2.1.0.1
- rebuilt with perl 5.12

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 0.91-alt2.1.0
- Automated rebuild.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.91-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Thu Sep 04 2003 Konstantin Timoshenko <kt@altlinux.ru> 0.91-alt2
- add buildreq

* Thu Nov 28 2002 Konstantin Timoshenko <kt@altlinux.ru> 0.91-alt1
- First AltLinux release
