# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Data/Dumper.pm) perl(Exporter.pm) perl(Fcntl.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(File/Temp.pm) perl(FileHandle.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(MIME/Base64.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(PerlIO.pm) perl(Socket.pm) perl(Test/Deep.pm) perl(Text/Diff.pm) perl(YAML.pm) perl(YAML/Tiny.pm) perl(base.pm) perl(overload.pm) perl(threads/shared.pm) perl-podlators
# END SourceDeps(oneline)
BuildRequires: perl(DBD/SQLite.pm)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Test-Fixture-DBIC-Schema
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt1_8

Summary:    Load fixture data to storage
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBIx/Class.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Filter/Util/Call.pm)
BuildRequires: perl(Kwalify.pm)
BuildRequires: perl(inc/Module/Install.pm)
BuildRequires: perl(Params/Validate.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Requires.pm)
BuildRequires: perl(YAML/Syck.pm)
BuildArch:  noarch
Source44: import.info

%description
Test::Fixture::DBIC::Schema is fixture data loader for DBIx::Class::Schema.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml  README
%perl_vendor_privlib/*


%changelog
* Fri Oct 13 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_8
- update by mgaimport

* Mon Sep 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_7
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_6
- update by mgaimport

* Wed Feb 17 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_5
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_4
- update by mgaimport

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_2
- update by mgaimport

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- update by mgaimport

* Sat Jul 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1_1
- mageia import by cas@ requiest

