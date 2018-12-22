# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/EOL.pm) perl(Test/NoTabs.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBIx/Class/InflateColumn/Object/Enum.pm) perl(Hash/Merge/Simple.pm) perl(DBIx/Class/TimeStamp.pm) perl(DBD/SQLite.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Tapper-Reports-API
%define upstream_version 5.0.5

%{?perl_default_filter}

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_1

Summary:    Tapper - Remote network API for result evaluation
License:    GPL-1.0-or-later or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Tapper/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class/C3.pm)
BuildRequires: perl(Cwd.pm)
BuildRequires: perl(Data/Dumper.pm)
BuildRequires: perl(DateTime/Format/SQLite.pm)
BuildRequires: perl(Data/Serializer.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Slurp.pm)
BuildRequires: perl(Log/Log4perl.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/Daemonize.pm)
BuildRequires: perl(Net/Server/Fork.pm)
BuildRequires: perl(Tapper/Config.pm)
BuildRequires: perl(Tapper/Model.pm)
BuildRequires: perl(Tapper/Reports/DPath/Mason.pm)
BuildRequires: perl(Tapper/Reports/DPath/TT.pm)
BuildRequires: perl(Tapper/Schema/TestTools.pm)
BuildRequires: perl(Test/Deep.pm)
BuildRequires: perl(Test/Fixture/DBIC/Schema.pm)
BuildRequires: perl(Test/MockModule.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(parent.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(subs.pm)
BuildRequires: perl(warnings.pm)
BuildArch:  noarch
Source44: import.info

%description
This package provides Tapper's Remote network API for result evaluation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.json META.yml  README
%{perl_vendor_privlib}/*
/usr/bin/tapper-reports-api
/usr/bin/tapper-reports-api-daemon
/usr/share/man/man1/tapper-reports-api-daemon.1*
/usr/share/man/man1/tapper-reports-api.1*


%changelog
* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 5.0.5-alt1_1
- update by mgaimport

* Thu Apr 07 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.5-alt1
- automated CPAN update

* Mon Mar 21 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.3-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 5.0.0-alt1
- automated CPAN update

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_6
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_3
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1_2
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 4.1.2-alt1
- automated CPAN update

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 4.1.0-alt1_1
- mageia import by cas@ requiest

