%define dist IO-File-String
Name: perl-%dist
Version: 0.11
Release: alt2

Summary: load/save whole file as single string
License: GPL or Artistic
Group: Development/Perl
Packager: Boris Savelev <boris@altlinux.org>

URL: %CPAN %dist
Source: http://search.cpan.org/CPAN/authors/id/D/DA/DANPEDER/%dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Mar 16 2009
BuildRequires: perl-Test-Easy perl-devel

%description
Simple interface to enable load/save the whole file as single scalar string.
It is subclass of IO::File so that all methods are inherited (including the 'new' method).

%prep
%setup -q -n %dist-%version

cat > t/00-01_use.t <<'EOF'
use Test::More tests => 1;
require_ok( 'IO::File::String' );
EOF

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README
%perl_vendor_privlib/IO/File/*

%changelog
* Sat Jan 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt2
- fixed build

* Mon Mar 16 2009 Boris Savelev <boris@altlinux.org> 0.11-alt1
- initial build
