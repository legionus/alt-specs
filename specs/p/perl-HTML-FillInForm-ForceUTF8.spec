%define _unpackaged_files_terminate_build 1
BuildRequires: perl(Module/Build.pm)
%define module_version 0.03
%define module_name HTML-FillInForm-ForceUTF8
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Encode.pm) perl(ExtUtils/MakeMaker.pm) perl(HTML/FillInForm.pm) perl(HTML/Parser.pm) perl(Test/More.pm) perl(base.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.03
Release: alt1
Summary: FillInForm with utf8 encoding
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/K/KA/KAZEBURO/HTML-FillInForm-ForceUTF8-%{version}.tar.gz
BuildArch: noarch

%description
HTML::FillInForm::ForceUTF8 is a subclass of HTML::FillInForm that forces utf8 flag on html and parameters..This allows you to prevent filling garbled result.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README.md Changes
%perl_vendor_privlib/H*

%changelog
* Mon May 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt2
- build for Sisyphus (required for perl update)

* Mon Oct 07 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- initial import by package builder

