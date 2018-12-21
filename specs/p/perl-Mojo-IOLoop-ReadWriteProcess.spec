%define _unpackaged_files_terminate_build 1

Name: perl-Mojo-IOLoop-ReadWriteProcess
Version: 0.23
Release: alt1
Summary: Execute external programs or internal code blocks as separate process
License: Artistic-1.0 or GPL-1.0+
Group: Development/Perl
Url: http://search.cpan.org/dist/Mojo-IOLoop-ReadWriteProcess/
Source0: http://www.cpan.org/authors/id/M/MU/MUDLER/Mojo-IOLoop-ReadWriteProcess-%{version}.tar.gz
BuildArch: noarch

BuildRequires: perl-devel
BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Mojolicious.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(Mojo/Base.pm)
BuildRequires: perl(Mojo/File.pm)

Requires: perl(Mojolicious.pm)

%description
Mojo::IOLoop::ReadWriteProcess is yet another process manager.

%prep
%setup -q -n Mojo-IOLoop-ReadWriteProcess-%{version}
%ifnarch %ix86 x86_64
# following test may fail on some architectures
rm -f t/12_mocked_container.t
%endif

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendorlib/Mojo/IOLoop*
%doc Changes LICENSE README.md

%changelog
* Tue Aug 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Wed Aug 08 2018 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 0.20-alt1
- initial build for ALT
