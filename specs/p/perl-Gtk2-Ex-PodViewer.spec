## SPEC file for Perl module Gtk2::Ex:PodViewer
## Used in PodBrowser

Name: perl-Gtk2-Ex-PodViewer
Version: 0.18
Release: alt2

Summary: a Gtk2 widget for displaying POD documents

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~gbrown/Gtk2-Ex-PodViewer/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Gtk2-Ex-PodViewer
Source: http://search.cpan.org/CPAN/authors/id/G/GB/GBROWN/%real_name-%version.tar.gz
Patch0: Gtk2-Ex-PodViewer-0.16-alt-Gtk2_init.patch

AutoReqProv: perl, yes
BuildRequires(pre): fontconfig rpm-build-licenses
BuildRequires(pre): perl-Locale-gettext perl-Gtk2-Ex-Simple-List

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
# Automatically added by buildreq on Sun Nov 24 2013
# optimized out: perl-Encode perl-Pod-Escapes perl-Pod-Simple perl-podlators
BuildRequires: perl-Gtk2 perl-IO-stringy perl-Pod-Parser perl-devel

%description
Perl module Gtk2::Ex::PodViewer is a widget for rendering Perl 
POD documents. It is based on the Gtk2::TextView widget and 
uses Pod::Parser for manipulating POD data.


%prep
%setup  -n %real_name-%version
%patch0

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README
%exclude /.perl.req
%_bindir/podviewer
%_man1dir/podviewer*
%perl_vendor_privlib/Gtk2/Ex/PodViewer*

%changelog
* Sun Nov 24 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.18-alt2
- Updating BuildRequires

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.18-alt1
- New version 0.18

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.17-alt1
- New version 0.17

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt1
- Initial build for ALT Linux Sisyphus

* Thu Aug 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.16-alt0
- Initial build
