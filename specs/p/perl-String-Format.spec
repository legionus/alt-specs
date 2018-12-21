## SPEC file for Perl module String-Format

Name: perl-String-Format
Version: 1.18
Release: alt1

Summary: Perl module for sprintf-like string formatting

License: %perl_license
Group: Development/Perl

%define real_name String-Format
URL: http://search.cpan.org/~darren/String-Format/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar
BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses perl-devel

%description
Perl module String::Format provides a sprintf-style formatting
capabilities with arbitrary format definitions.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%exclude /.perl.req
%perl_vendor_privlib/String/Format*

%changelog
* Sun Mar 04 2018 Nikolay A. Fetisov <naf@altlinux.org> 1.18-alt1
- New version

* Mon Jan 07 2013 Nikolay A. Fetisov <naf@altlinux.ru> 1.17-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.16-alt1
- New version 1.16

* Mon May 07 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.14-alt1
- Initial build for ALT Linux Sisyphus

