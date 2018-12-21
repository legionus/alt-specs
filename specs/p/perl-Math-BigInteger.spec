%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(DynaLoader.pm) perl(Exporter.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# $Revision: 1.45 $, $Date: 2011/10/10 18:18:13 $
#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Math
%define		pnam	BigInteger
Summary:	Math::BigInteger - arbitrary length integer extension module for Perl
Summary(pl.UTF-8):	Math::BigInteger - moduł rozszerzenia liczb całkowitych dowolnej długości
Name:		perl-Math-BigInteger
Version:	1.01
Release:	alt4
# if used in a product, Systemics should be given attribution
License:	free use, distributable
Group:		Development/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a4aa79e070f3f5f8e7f01443fdc03b8e
Patch0:		%{name}-Fputc_to_fputc.patch
URL:		http://search.cpan.org/dist/Math-BigInteger/
BuildRequires:	perl-devel 
Source44: import.info

%description
Math::BigInteger module gives access to Eric Young's bignum library.
This provides a faster alternative to the Math::BigInt library.

%description -l pl.UTF-8
Moduł Math::BigInteger umożliwia dostęp do biblioteki bignum Erica
Younga. Jest to szybsza alternatywa dla biblioteki Math::BigInt.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}
%patch0 -p0

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{optflags}"

%{?with_tests:%{__make} test}

%install

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%files
%doc README COPYRIGHT
%{perl_vendor_archlib}/Math/BigInteger.pm
%{perl_vendor_archlib}/Math/BigInteger.pod
%dir %{perl_vendor_archlib}/auto/Math/BigInteger
%{perl_vendor_archlib}/auto/Math/BigInteger/BigInteger.*

%changelog
* Fri Jun 29 2018 Igor Vlasenko <viy@altlinux.ru> 1.01-alt4
- fixed unpackaged files

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt3.1
- rebuild with new perl 5.20.1

* Fri Aug 30 2013 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt3
- built for perl 5.18

* Tue Sep 04 2012 Vladimir Lettiev <crux@altlinux.ru> 1.01-alt2
- rebuilt for perl-5.16

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_7
- converted from PLD by srpmconvert script

