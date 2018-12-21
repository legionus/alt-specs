#
#   - Module::Starter::Plugin::TT2 -
#   This spec file was automatically generated by cpan2rpm [ver: 2.027]
#   (ALT Linux revision)
#   The following arguments were used:
#       --debug Module::Starter::Plugin::TT2
#   For more information on cpan2rpm please visit: http://perl.arix.com/
#

%define module Module-Starter-Plugin-TT2
%define m_distro Module-Starter-Plugin-TT2
%define m_name Module::Starter::Plugin::TT2
%define m_author_id RJBS
%define _enable_test 1

Name: perl-Module-Starter-Plugin-TT2
Version: 0.125
Release: alt1

Summary: TT2 templates for Module::Starter::Template

License: Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Module-Starter-Plugin-TT2/

Packager: Michael Bochkaryov <misha@altlinux.ru>

BuildArch: noarch
Source: http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/%m_distro-%version.tar.gz

# Automatically added by buildreq on Mon May 11 2009 (-bi)
BuildRequires: perl-Module-Starter perl-Template perl-Test-Pod perl-Test-Pod-Coverage

%description
This Module::Starter plugin is intended to be loaded after
Module::Starter::Plugin::Template.  It implements the "renderer" and "render"
methods, required by the Template plugin.  The methods are implemented with
Template Toolkit.

This module's distribution includes a directory, "templates/dir", and a file
"templates/inline" that contain stock templates for use with the InlineStore
and DirStore plugins.  The module itself contains default templates in its data
section.

%prep
%setup -q -n %m_distro-%version
%build
%perl_vendor_build

%install
%perl_vendor_install
rm -rf %buildroot%perl_vendor_man3dir/

%files
%perl_vendor_privlib/Module/*

%changelog
* Mon May 11 2009 Michael Bochkaryov <misha@altlinux.ru> 0.125-alt1
- initial build for ALT Linux Sisyphus

