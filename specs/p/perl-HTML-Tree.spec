%define _unpackaged_files_terminate_build 1
%define dist HTML-Tree
Name: perl-%dist
Version: 5.07
Release: alt1

Summary: Perl modules for HTML syntax tree processing
License: GPL-1.0-only or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/K/KE/KENTNL/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Sep 26 2012
BuildRequires: perl-Module-Build perl-Test-Fatal perl-libwww

%description
This package contains a suite of modules for representing, creating,
and extracting information from HTML syntax trees

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	Changes README
	%_bindir/htmltree
	%_man1dir/htmltree.*
%dir	%perl_vendor_privlib/HTML
	%perl_vendor_privlib/HTML/*.pm
%dir	%perl_vendor_privlib/HTML/Element
	%perl_vendor_privlib/HTML/Element/*.pm
%dir	%perl_vendor_privlib/HTML/Tree
%doc	%perl_vendor_privlib/HTML/Tree/*.pod

%changelog
* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 5.07-alt1
- automated CPAN update

* Fri Aug 11 2017 Igor Vlasenko <viy@altlinux.ru> 5.06-alt1.1
- rebuild with new perl

* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 5.06-alt1
- automated CPAN update

* Mon Apr 11 2016 Igor Vlasenko <viy@altlinux.ru> 5.03-alt2
- build w/o HTML-Format

* Wed Sep 26 2012 Alexey Tourbin <at@altlinux.ru> 5.03-alt1
- 4.2 -> 5.03
- requires LWP::UserAgent

* Fri Apr 22 2011 Alexey Tourbin <at@altlinux.ru> 4.2-alt1
- 4.1 -> 4.2

* Wed Dec 22 2010 Alexey Tourbin <at@altlinux.ru> 4.1-alt1
- 3.23 -> 4.1
- packaged /usr/bin/htmltree

* Tue Nov 14 2006 Alexey Tourbin <at@altlinux.ru> 3.23-alt1
- 3.21 -> 3.23

* Tue Aug 08 2006 Alexey Tourbin <at@altlinux.ru> 3.21-alt1
- 3.20 -> 3.21

* Wed Jun 07 2006 Alexey Tourbin <at@altlinux.ru> 3.20-alt1
- 3.18 -> 3.20

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 3.18-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Fri Oct 03 2003 Alexey Tourbin <at@altlinux.ru> 3.18-alt1
- 3.18

* Thu Sep 04 2003 Alexey Tourbin <at@altlinux.ru> 3.17-alt2
- fixed tests that fail because of recent HTML::Parser changes

* Tue Mar 18 2003 Stanislav Ievlev <inger@altlinux.ru> 3.17-alt1
- Initial release for Sisyphus
