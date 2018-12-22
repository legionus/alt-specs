%define _unpackaged_files_terminate_build 1
#
#   - Path::Class -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module Path-Class
%define m_distro Path-Class
%define m_name Path::Class
%define m_author_id unknown
%def_enable test

Name: perl-Path-Class
Version: 0.37
Release: alt1

Summary: Cross-platform path specification manipulation

License: Artistic and GPL-1.0-only
Group: Development/Perl
Url: http://search.cpan.org/dist/Path-Class/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/K/KW/KWILLIAMS/Path-Class-%{version}.tar.gz

# Automatically added by buildreq on Tue Apr 13 2010 (-bi)
BuildRequires: perl-Module-Build

%description
Path::Class is a module for manipulation of file and directory
specifications (strings describing their locations, like
'/home/ken/foo.txt' or 'C:\Windows\Foo.txt') in a cross-platform
manner. It supports pretty much every platform Perl runs on,
including Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2, and
NetWare.

The well-known module File::Spec also provides this service, but
it's sort of awkward to use well, so people sometimes avoid it,
or use it in a way that won't actually work properly on
platforms significantly different than the ones they've tested
their code on.

%prep
%setup -q -n %m_distro-%version
# We don't have File::Spec::Win32/OS2/Mac
rm t/02-foreign.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Path*

%changelog
* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.36-alt1
- automated CPAN update

* Mon Sep 15 2014 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.34-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Tue Sep 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Tue Apr 13 2010 Alexey Tourbin <at@altlinux.ru> 0.18-alt1
- 0.16 -> 0.18

* Tue Nov 18 2008 Michael Bochkaryov <misha@altlinux.ru> 0.16-alt2
- fix directory ownership violation

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 0.16-alt1
- first build for ALT Linux Sisyphus

