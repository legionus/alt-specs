#
#   - RunApp -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --name RunApp --version 0.13 http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/RunApp-0.13.tar.gz
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module RunApp
%define m_distro RunApp
%define m_name RunApp
%define m_author_id unknown
%define _enable_test 1

Name: perl-RunApp
Version: 0.13
Release: alt2.1

Summary: a module for streamlining applications / services startup.


License: Artistic
Group: Development/Perl
Url: http://www.cpan.org

Packager: Igor Vlasenko <viy@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/C/CL/CLKAO/%m_distro-%version.tar.gz

# Automatically added by buildreq on Fri Jun 01 2007
BuildRequires: perl-App-Control perl-devel perl-Template perl-YAML

%description
%summary

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%exclude %perl_vendor_archlib

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Wed Sep 03 2008 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2
- removed perl dir ownership

* Fri Jun 01 2007 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- first build for ALT Linux Sisyphus

