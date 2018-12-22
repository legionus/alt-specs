# BEGIN SourceDeps(oneline):
BuildRequires: perl(Module/Build/Tiny.pm) perl-devel
# END SourceDeps(oneline)
%define module Source-Bundle

Name: perl-%module
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL-1.0-only or Artistic
Source: %module-%version.tar
Url: http://search.cpan.org/dist/%module

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
#doc README
%perl_vendor_privlib/Source*

%changelog
* Sun Jan 08 2017 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build for Sisyphus
