%define module Tk-Splash
%def_without test

Name: perl-%module
Version: 0.16
Release: alt1

Summary: A perl/Tk module for creating splash screens
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/S/SR/SREZIC/Tk-Splash-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Thu Mar 06 2008
BuildRequires: perl-Tk perl-devel

%description
This is Tk::Splash, a perl/Tk module for creating splash screens.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Tk/*

%changelog
* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.14-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Mar 06 2008 Victor Forsyuk <force@altlinux.org> 0.14-alt1
- Initial build.
