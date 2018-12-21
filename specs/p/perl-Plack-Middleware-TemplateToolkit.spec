%define dist Plack-Middleware-TemplateToolkit
%def_without test

Name: perl-%dist
Version: 0.28
Release: alt1

Summary: Middleware to allow your Plack-based application to serve files processed through Template Toolkit (TT).
License: GPL or Artistic
Group: Development/Perl
Url: %CPAN %dist

BuildArch: noarch
Source: http://www.cpan.org/authors/id/L/LL/LLAP/Plack-Middleware-TemplateToolkit-%{version}.tar.gz

BuildRequires: perl-Plack perl-Plack-Middleware-Debug perl-Template

%description
%name

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/*
%doc README example

%changelog
* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Mon Mar 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1
- automated CPAN update

* Fri Oct 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Mon Feb 20 2012 Eugene Prokopiev <enp@altlinux.ru> 0.25-alt1
- first build for Sisyphus

