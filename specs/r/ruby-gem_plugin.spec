%def_disable check

%define pkgname gem_plugin

Name: ruby-%pkgname
Version: 0.2.3
Release: alt2.3

Summary: Gem Based Plugin System
Group: Development/Ruby
License: MIT
Url: http://rubyforge.org/projects/mongrel/

BuildArch: noarch

Provides: %_datadir/%pkgname

Source: %pkgname-%version.tar
Patch: %pkgname-%version-%release.patch

# Automatically added by buildreq on Wed Aug 27 2008 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%add_findreq_skiplist %_datadir/%pkgname/gem_plugin/*

%description
GemPlugin is a system that lets your users install gems and
lets you load them as additional features to use in your
software.  It originated from the Mongrel project but proved
useful enough to break out into a separate project.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -q -n %pkgname-%version
%patch -p1
%update_setup_rb

%build
%ruby_config
%ruby_build

%install
mkdir -p %buildroot%_datadir/%pkgname/gem_plugin
%ruby_install
cp -dpR resources %buildroot%_datadir/%pkgname/gem_plugin/
%rdoc lib/

%check
%ruby_test_unit -Ilib test

%files
%doc CHANGELOG README
%_bindir/*
%dir %_datadir/%pkgname
%_datadir/%pkgname/gem_plugin
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%ruby_ri_sitedir/GemPlugin*

%changelog
* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.2.3-alt2.3
- Rebuild with new Ruby autorequirements.

* Fri Mar 21 2014 Led <led@altlinux.ru> 0.2.3-alt2.2
- disabled %%check

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.2.3-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Fri May 15 2009 Alexey I. Froloff <raorn@altlinux.org> 0.2.3-alt2
- Rebuilt with Ruby 1.9

* Wed Aug 27 2008 Sir Raorn <raorn@altlinux.ru> 0.2.3-alt1
- Built for Sisyphus

