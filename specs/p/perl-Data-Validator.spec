%define _unpackaged_files_terminate_build 1
%define module_version 1.07
%define module_name Data-Validator
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Benchmark.pm) perl(CPAN/Meta.pm) perl(CPAN/Meta/Prereqs.pm) perl(ExtUtils/MakeMaker.pm) perl(Module/Build.pm) perl(Moose.pm) perl(MooseX/Params/Validate.pm) perl(Mouse.pm) perl(Mouse/Role.pm) perl(Mouse/Util.pm) perl(Mouse/Util/TypeConstraints.pm) perl(MouseX/Types/URI.pm) perl(Params/Validate.pm) perl(Smart/Args.pm) perl(Test/More.pm) perl(Test/Mouse.pm) perl(Test/Requires.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 1.07
Release: alt1
Summary: Rule based validator on type constraint system
Group: Development/Perl
License: perl
URL: https://github.com/gfx/p5-Data-Validator

Source: http://www.cpan.org/authors/id/G/GF/GFUJI/Data-Validator-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc LICENSE Changes README.md example
%perl_vendor_privlib/D*

%changelog
* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.07-alt1
- automated CPAN update

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2
- uploaded to Sisyphus as Scalar-Does dependency

* Mon Dec 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1
- regenerated from template by package builder

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 1.03-alt1
- initial import by package builder

