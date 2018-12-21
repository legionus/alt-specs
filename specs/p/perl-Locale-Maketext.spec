%define dist Locale-Maketext
Name: perl-%dist
Version: 1.28
Release: alt1

Summary: A framework for localization
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TO/TODDR/Locale-Maketext-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Feb 04 2011
BuildRequires: perl-I18N-LangTags perl-Test-Pod

%description
Locale::Maketext is a framework for software localization;
it provides the tools for organizing and accessing the bits
of text and text-processing code for producing localized
applications.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Locale*

%changelog
* Fri Jul 29 2016 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Sun Jul 03 2016 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Fri Feb 04 2011 Alexey Tourbin <at@altlinux.ru> 1.17-alt1
- 1.13 -> 1.17

* Sun Aug 10 2008 Alexey Tourbin <at@altlinux.ru> 1.13-alt1
- 1.12 -> 1.13

* Thu Apr 24 2008 Alexey Tourbin <at@altlinux.ru> 1.12-alt1
- 1.10 -> 1.12

* Tue Apr 10 2007 Alexey Tourbin <at@altlinux.ru> 1.10-alt1
- 1.09 -> 1.10

* Sun Dec 19 2004 Alexey Tourbin <at@altlinux.ru> 1.09-alt1
- initial revision (split perl-i18n)
