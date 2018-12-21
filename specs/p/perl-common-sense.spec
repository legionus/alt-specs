%define _unpackaged_files_terminate_build 1
%define module common-sense

Name: perl-%module
Version: 3.74
Release: alt1

Summary: "Common sense" Perl defaults
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/common-sense-%{version}.tar.gz

#BuildArch: noarch

# Automatically added by buildreq on Thu Apr 08 2010
BuildRequires: perl-devel

%description
This module implements some sane defaults for Perl programs, as defined by two
typical (or not so typical - use your common sense) specimens of Perl coders:

 use strict qw(vars subs);
 use feature qw(say state switch);
 no warnings;

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_archlib/common

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 3.74-alt1
- automated CPAN update

* Mon Jun 02 2014 Igor Vlasenko <viy@altlinux.ru> 3.73-alt1
- automated CPAN update

* Mon Sep 16 2013 Igor Vlasenko <viy@altlinux.ru> 3.72-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 3.6-alt1
- automated CPAN update

* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 3.5-alt1
- 3.5

* Thu Jan 27 2011 Victor Forsiuk <force@altlinux.org> 3.4-alt1
- 3.4

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3.3-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Tue Jul 06 2010 Victor Forsiuk <force@altlinux.org> 3.3-alt1
- 3.3

* Tue Jun 22 2010 Victor Forsiuk <force@altlinux.org> 3.2-alt1
- 3.2

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 3.1-alt1
- 3.1

* Fri Dec 25 2009 Victor Forsyuk <force@altlinux.org> 3.0-alt1
- 3.0

* Fri Dec 11 2009 Victor Forsyuk <force@altlinux.org> 2.03-alt1
- 2.03

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 2.01-alt1
- Initial build.
