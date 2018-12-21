# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    LWP-Protocol-PSGI
%define upstream_version 0.10

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_2

Summary:    Override LWP's HTTP/HTTPS backend with your own PSGI applciation
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LWP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTTP/Message/PSGI.pm)
BuildRequires: perl(LWP.pm)
BuildRequires: perl(LWP/Protocol.pm)
BuildRequires: perl(Module/Build/Tiny.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Requires.pm)
BuildRequires: perl(parent.pm)
BuildArch:  noarch
Source44: import.info

%description
LWP::Protocol::PSGI is a module to hijack *any* code that uses the
LWP::UserAgent manpage underneath such that any HTTP or HTTPS requests can
be routed to your own PSGI application.

Because it works with any code that uses LWP, you can override various
WWW::*, Net::* or WebService::* modules such as the WWW::Mechanize manpage,
without modifying the calling code or its internals.

  use WWW::Mechanize;
  use LWP::Protocol::PSGI;

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor

./Build

%check
./Build test

%install
./Build install --destdir=%{buildroot}

%files
%doc Changes LICENSE META.json META.yml  README
%{perl_vendor_privlib}/*

%changelog
* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update by mgaimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- update by mgaimport

* Sat May 14 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- update by mgaimport

* Sat Mar 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1_1
- update by mgaimport

* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update by mgaimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_1
- update by mgaimport

* Fri Nov 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_2
- update by mgaimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_1
- build for Sisyphus

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.04-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_1
- converted for ALT Linux by srpmconvert tools

