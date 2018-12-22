%define _unpackaged_files_terminate_build 1
%define dist List-Compare
Name: perl-%dist
Version: 0.53
Release: alt1

Summary: Compare elements of two or more lists
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JK/JKEENAN/List-Compare-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Apr 28 2010
BuildRequires: perl-devel

%description
List::Compare is a simple, object-oriented implementation of very
common Perl code used to determine interesting relationships between
two lists at a time.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/List*

%changelog
* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.53-alt1
- automated CPAN update

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 0.52-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 0.49-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.41-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.39-alt1
- automated CPAN update

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.38-alt1
- automated CPAN update

* Wed Apr 28 2010 Alexey Tourbin <at@altlinux.ru> 0.37-alt1
- 0.32 -> 0.37

* Sat Sep 24 2005 Alexey Tourbin <at@altlinux.ru> 0.32-alt1
- 0.29 -> 0.32
- manual pages not packaged (use perldoc)

* Mon May 17 2004 Alexey Tourbin <at@altlinux.ru> 0.29-alt1
- initial revision
