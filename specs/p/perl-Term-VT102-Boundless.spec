# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Term-VT102-Boundless
%define upstream_version 0.05

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    A L<Term::VT102> that grows automatically to
License:    GPL-1.0-or-later or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Term/VT102.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/use/ok.pm)
BuildArch:  noarch
Source44: import.info

%description
This is a subclass of the Term::VT102 manpage that will grow the virtual
screen to accomodate arbitrary width and height of text.

The behavior is more similar to the buffer of a scrolling terminal emulator
than to a real terminal, making it useful for output displays in scrolling
media.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml 
%perl_vendor_privlib/*

%changelog
* Tue Oct 30 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update by mgaimport

* Wed Oct 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_7
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- update by mgaimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- update by mgaimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- mageia import by cas@ requiest

