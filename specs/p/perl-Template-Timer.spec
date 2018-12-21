#
#   - Template::Timer -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#

%define module Template-Timer
%define m_distro Template-Timer
%define m_name Template::Timer
%define m_author_id unknown
%def_enable test

Name: perl-Template-Timer
Version: 1.00
Release: alt1.1

Summary: %m_name - Rudimentary profiling for Template Toolkit

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Template-Timer/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://www.cpan.org/authors/id/P/PE/PETDANCE/Template-Timer-1.00.tar.gz

# Automatically added by buildreq on Sat Sep 06 2008 (-bi)
BuildRequires: perl-Template perl-Test-Pod

%description
Template::Timer provides inline timings of the template processing
througout your code.  It's an overridden version of Template::Context
that wraps the "process()" and "include()" methods.

%prep
%setup -q -n %m_distro-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Template*
%doc Changes README

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1
- automated CPAN update

* Sat Sep 06 2008 Michael Bochkaryov <misha@altlinux.ru> 0.04-alt2
- spec file cleanup
- fix directory ownership violation

* Wed Mar 21 2007 Sir Raorn <raorn@altlinux.ru> 0.04-alt1
- Built for Sisyphus

