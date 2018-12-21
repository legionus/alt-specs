## SPEC file for Perl module XML::AutoWriter
## Used in SVK

Name: perl-XML-AutoWriter
Version: 0.40
Release: alt3

Summary: provides DTD based XML output
Summary(ru_RU.UTF-8): вывод данных в формате XML соглано описанию DTD

License: GPL or Artistic
Group: Development/Perl

%define real_name XML-AutoWriter
URL: http://search.cpan.org/~perigrin/XML-AutoWriter

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

Source: %real_name-%version.tar
Patch0: %real_name-0.04-alt-Makefile.patch
Patch1: %real_name-0.04-debian-UNIVERSAL.patch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel


# Automatically added by buildreq on Sun Nov 28 2010
BuildRequires: perl-Module-Install perl-XML-Parser

%description
This package contains several Perl modules to provide simple 
generation of valid XML code using given DTD description. 

%description -l ru_RU.UTF-8
Данный пакет содержит несколько модулей  Perl,  предоставляющих
возможность простого создания действительных (valid) документов
XML, с использованием имеющихся определений DTD.

%prep
%setup -q -n %real_name-%version
%patch0
%patch1 -p 1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES
%perl_vendor_privlib/XML/AutoWriter*
%perl_vendor_privlib/XML/Doctype*
%perl_vendor_privlib/XML/ValidWriter*

%changelog
* Sat Dec 12 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.40-alt3
- Fix for Perl 5.22.0

* Tue Sep 11 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.40-alt2
- Fix build with Perl 5.16.1

* Sat Nov 27 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.40-alt1
- New version 0.4

* Thu Aug 09 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.39-alt2
- Fix typos in package description

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.39-alt1
- Initial build for ALT Linux
- New version 0.39

* Tue May 24 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.38-alt0.1
- Build for new perl-5.8.7

* Sat Mar 05 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.38-alt0
- Initial release
