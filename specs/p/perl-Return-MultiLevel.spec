%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Test/More.pm) perl(parent.pm) perl(Data/Munge.pm) perl(Test/Fatal.pm)
# END SourceDeps(oneline)
%define module_name Return-MultiLevel
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.05
Release: alt1
Summary: return across multiple call levels
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/M/MA/MAUKE/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
%summary

%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/R*

%changelog
* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Tue Sep 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- automated CPAN update

* Wed Jun 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt2
- moved to Sisyphus

* Wed Sep 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- initial import by package builder

