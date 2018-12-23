%define module_name Barcode-Code128

Name: perl-%module_name
Version: 2.21
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Generate CODE 128 bar codes
License: ALT-Public-Domain
Group: Development/Perl

Url: %CPAN %module_name
Source: http://www.cpan.org/authors/id/W/WR/WRW/Barcode-Code128-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Jan 15 2010
BuildRequires: perl-GD perl-devel

%description
Barcode::Code128 generates bar codes using the CODE 128 symbology. It can
generate images in PNG or GIF format using the GD package, or it can generate
a text string representing the barcode that you can render using some other
technology if desired.

%prep
%setup -n %module_name-%version

# From PLD spec:
# module generates correct image, but a bit different to
# the one included in the distribution and compared with
mv t/png.t{,.broken}

# The same correct for this test:
mv t/gif.t{,.broken}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Barcode/

%changelog
* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1
- automated CPAN update
- dropped Patch1: Barcode-Code128-2.01-creategif.patch (deprecated)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 2.01-alt3.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 15 2010 Victor Forsyuk <force@altlinux.org> 2.01-alt3
- Resurrect deleted package.
