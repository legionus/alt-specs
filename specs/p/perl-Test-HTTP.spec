%def_without test
%define module_version 0.18
%define module_name Test-HTTP
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Carp.pm) perl(Class/Field.pm) perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(Filter/Simple.pm) perl(LWP.pm) perl(LWP/UserAgent.pm) perl(Test/Builder/Module.pm) perl(Test/More.pm) perl(Text/Balanced.pm)
# END SourceDeps(oneline)
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.18
Release: alt2
Summary: Testing for HTTP services
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/L/LU/LUKEC/%module_name-%module_version.tar.gz
BuildArch: noarch

%description
the Test::HTTP manpage is designed to make it easier to write tests which are mainly.about HTTP-level things, such as REST-type services.

Each `Test::HTTP' object can contain state about a current request and its
response.  This allows convenient shorthands for sending requests, checking
status codes, headers, and message bodies.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/T*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt2
- build for Sisyphus (required for perl update)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- initial import by package builder

