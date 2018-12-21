%define _unpackaged_files_terminate_build 1
#
#   - FCGI-ProcManager -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module FCGI-ProcManager
%define m_distro FCGI-ProcManager
%define m_name FCGI::ProcManager
%define m_author_id GBJK
%def_enable test

Name: perl-FCGI-ProcManager
Version: 0.28
Release: alt1

Summary: %m_name - A perl-based FastCGI process manager

License: LGPL
Group: Development/Perl
Url: http://search.cpan.org/dist/FCGI-ProcManager/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source0: http://www.cpan.org/authors/id/A/AR/ARODLAND/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Mon Nov 09 2009 (-bi)
BuildRequires: perl-devel

%description
FCGI::ProcManager is used to serve as a FastCGI process manager.  By
re-implementing it in perl, developers can more finely tune performance in
their web applications, and can take advantage of copy-on-write semantics
prevalent in UNIX kernel process management.  The process manager should
be invoked before the caller''s request loop

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/FCGI*
%doc COPYING README ChangeLog TODO

%changelog
* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Thu Sep 22 2011 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Nov 09 2009 Michael Bochkaryov <misha@altlinux.ru> 0.19-alt1
- 0.19 version

* Sat Sep 13 2008 Michael Bochkaryov <misha@altlinux.ru> 0.18-alt2
- fix directory ownership violation
- spec file cleanup

* Sun Apr 20 2008 Michael Bochkaryov <misha@altlinux.ru> 0.18-alt1
- 0.18 version

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 0.17-alt1
- first build for ALT Linux Sisyphus
