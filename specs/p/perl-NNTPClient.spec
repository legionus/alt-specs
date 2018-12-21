%define module_name NNTPClient

Name: perl-NNTPClient
Version: 0.37
Release: alt3.1
License: distributable

Group: Development/Perl
Summary: NNTPClient module for perl (News)
Url: http://www.cpan.org

BuildArch: noarch
#Requires: perl >= 5.00503

Packager: Denis Smirnov <mithraen@altlinux.ru>

Source: NNTPClient-0.37.tar.bz2

# Automatically added by buildreq on Sun Nov 10 2002
BuildRequires: perl-devel

%description
NNTPClient module for perl

%prep
%setup -q -n %module_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README demos
%perl_vendor_privlib/N*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.37-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Dec 11 2008 Denis Smirnov <mithraen@altlinux.ru> 0.37-alt3
- cleanup spec

* Thu Dec 04 2008 Denis Smirnov <mithraen@altlinux.ru> 0.37-alt2
- fix build

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.37-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Sun Nov 10 2002 Sergey V Turchin <zerg@altlinux.ru> 0.37-alt1
- build for ALT
- cleanup spec

* Thu Feb 17 2000 Tim Powers <timp@redhat.com>
- Spec file was autogenerated.
