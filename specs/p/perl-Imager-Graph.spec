## SPEC file for Perl module Imager::Graph

%define real_name Imager-Graph

Name: perl-Imager-Graph
Version: 0.12
Release: alt1

Summary: producing Graphs using the Imager library

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/~tonyc/Imager-Graph/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Sep 14 2014
# optimized out: perl-devel
BuildRequires: perl-Imager

%description
Perl module Imager::Graph is intended to produce good looking
graphs with a minimum effort on the part of the user. 

Currently only the pie graph class, Imager::Graph::Pie, 
is provided.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README TODO Changes
%exclude /.perl.req
%perl_vendor_privlib/Imager/Graph*

%changelog
* Sat May 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.12-alt1
- New version

* Sun Sep 14 2014 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt1
- New version

* Sat Aug 10 2013 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt2
- Fix POD formating

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.10-alt1
- New version

* Fri Nov 04 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt2
- Fix build with Imager > 0.84

* Sun Nov 28 2010 Nikolay A. Fetisov <naf@altlinux.ru> 0.09-alt1
- New version

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sun Oct 18 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.07-alt1
- New version

* Sat May 24 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.06-alt1
- New version

* Sun Mar 02 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.05-alt1
- Initial build for ALT Linux Sisyphus
