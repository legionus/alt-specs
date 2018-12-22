# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname archive-tar-minitar

Name: ruby-%pkgname
Version: 0.5.2
Release: alt1.2

Summary: Library and command-line utility to deal with POSIX tar(1) archive files
Group: Development/Ruby
License: MIT or Ruby
Url: http://rubyforge.org/projects/ruwiki/

BuildArch: noarch

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Mon Aug 03 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
Archive::Tar::Minitar is a pure-Ruby library and command-line utility that
provides the ability to deal with POSIX tar(1) archive files. The
implementation is based heavily on Mauricio Ferna'ndez's implementation in
rpa-base, but has been reorganised to promote reuse in other projects.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:tests tests/tc*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc README
%_bindir/minitar
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%dir %ruby_ri_sitedir/Archive
%dir %ruby_ri_sitedir/Archive/Tar
%ruby_ri_sitedir/Archive/Tar/Minitar
%ruby_ri_sitedir/Archive/Tar/PosixHeader

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.5.2-alt1.2
- Rebuild with new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.5.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Aug 03 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.2-alt1
- Built for Sisyphus

