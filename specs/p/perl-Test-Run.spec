%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Benchmark.pm) perl(Carp.pm) perl(Config.pm) perl(Exporter.pm) perl(Fatal.pm) perl(Moose/Exporter.pm) perl(POSIX.pm) perl(Time/HiRes.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define upstream_name    Test-Run
%define upstream_version 0.0304

Name:       perl-%{upstream_name}
Version:    0.0304
Release:    alt1

Summary:    Named sprintf according to the
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:    http://www.cpan.org/authors/id/S/SH/SHLOMIF/Test-Run-%{version}.tar.gz

BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(IPC/System/Simple.pm)
BuildRequires: perl(List/MoreUtils.pm)
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(MRO/Compat.pm)
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Moose.pm)
BuildRequires: perl(MooseX/StrictConstructor.pm)
BuildRequires: perl(Scalar/Util.pm)
BuildRequires: perl(TAP/Parser.pm)
BuildRequires: perl(Test/Harness.pm)
BuildRequires: perl(Test/Trap.pm)
BuildRequires: perl(Text/Sprintf/Named.pm)
BuildRequires: perl(UNIVERSAL/require.pm)
BuildArch:  noarch
Source44: import.info

%description
The construct

  use if CONDITION, MODULE => ARGUMENTS;

has no effect unless 'CONDITION' is true. In this case the effect is the
same as of

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
%makeinstall_std

%files
%doc Changes DONE META.json META.yml  NOTES TODO examples
%perl_vendor_privlib/*

%changelog
* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.0304-alt1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.0303-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.0302-alt1
- automated CPAN update

* Sat Jan 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.0126-alt3_3
- moved to Sisyphus

* Tue Oct 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.0126-alt2_3
- mga update

* Fri Sep 13 2013 Cronbuild Service <cronbuild@altlinux.org> 0.0126-alt2_2
- rebuild to get rid of unmets

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.0126-alt1_2
- mgaimport update

* Mon Jul 29 2013 Igor Vlasenko <viy@altlinux.ru> 0.0126-alt1_1
- converted for ALT Linux by srpmconvert tools

