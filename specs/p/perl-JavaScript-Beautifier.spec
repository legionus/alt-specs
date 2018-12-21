%define _unpackaged_files_terminate_build 1
%def_with plugin

Name: perl-JavaScript-Beautifier
Version: 0.25
Release: alt1

Summary: JavaScript::Beautifier - Beautify Javascript (beautifier for javascript)
Group: Development/Perl
License: Perl

Url: %CPAN JavaScript-Beautifier
Source: %name-%version.tar

# main br
BuildRequires: perl-devel perl-Module-Build perl-Pod-Parser
%if_with plugin
BuildRequires: perl(File/Slurp/Tiny.pm) perl(IPC/Run3.pm) perl(Moo.pm) perl(Try/Tiny.pm)
%endif

BuildArch: noarch
%description
%summary

%prep
%setup -q

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md LICENSE Changes
%_bindir/js_beautify.pl
%_man1dir/js_beautify.*
%perl_vendor_privlib/JavaScript/Beautifier*
%perl_vendor_privlib/JavaScript/Packer1.pm
%if_with plugin
%perl_vendor_privlib/Code/TidyAll/Plugin/JSBeautifier*
%endif
%doc Changes

%changelog
* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Wed Apr 25 2018 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Thu Apr 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Thu Mar 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1
- automated CPAN update

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1
- automated CPAN update

* Fri Oct 21 2011 Vladimir Lettiev <crux@altlinux.ru> 0.17-alt1
- initial build
