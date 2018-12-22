%define _unpackaged_files_terminate_build 1
%define module_name Lingua-EN-Numbers-Ordinate

Name: perl-%module_name
Version: 1.04
Release: alt1

Summary: Go from cardinal number (3) to ordinal ("3rd")
Summary(ru_RU.UTF8): Преобразование количественных чисел (3) в порядковые (3rd)
Group: Development/Perl
URL: http://interglacial.com/~sburke
License: GPL-1.0-only or Artistic
Source: http://www.cpan.org/authors/id/N/NE/NEILB/Lingua-EN-Numbers-Ordinate-%{version}.tar.gz
Buildarch: noarch
AutoReqProv: yes, perl
BuildRequires: perl-devel

%description
There are two kinds of numbers in English -- cardinals (1, 2, 3...), 
and ordinals (1st, 2nd, 3rd...). This library provides functions for 
giving the ordinal form of a number, given its cardinal value.

%description -l ru_RU.UTF8
В английском языке есть два типа числительных - количественные (1, 2, 3...)
и порядковые (1st, 2nd, 3rd...). Библиотека предоставляет функции получения
порядковой формы числа из его количественного значения. 

%prep
%setup -q -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Lingua*

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Mar 26 2005 Vyacheslav Dikonov <slava@altlinux.ru> 1.02-alt1
- ALTLinux build
