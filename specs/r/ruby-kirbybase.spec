# vim: set ft=spec: -*- rpm-spec -*-

%define pkgname kirbybase

Name: ruby-%pkgname
Version: 2.6.1
Release: alt1

Summary: Small, plain-text, dbms written in Ruby
Group: Development/Ruby
License: MIT or Ruby
Url: http://rubyforge.org/projects/kirbybase/

Packager: Ruby Maintainers Team <ruby@packages.altlinux.org>

BuildArch: noarch

Source: %pkgname-%version.tar

# Automatically added by buildreq on Thu Jul 02 2009 (-bi)
BuildRequires: rpm-build-ruby ruby-test-unit ruby-tool-rdoc ruby-tool-setup

%description
A small, plain-text, dbms written in Ruby.  It can be used either embedded 
or client/server.

%package doc
Summary: Documentation files for %name
Group: Documentation

%description doc
Documentation files for %name

%prep
%setup -n %pkgname-%version
%update_setup_rb

%build
%ruby_config
%ruby_build
%ruby_test_unit -Ilib:test test/ts_*.rb

%install
%ruby_install
%rdoc lib/

%files
%doc README
%_bindir/*
%ruby_sitelibdir/*
%rubygem_specdir/*

%files doc
%doc examples images kirbybaserubymanual.html
%ruby_ri_sitedir/KirbyBase*

%changelog
* Thu Jul 19 2018 Andrey Cherepanov <cas@altlinux.org> 2.6.1-alt1
- New version.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.6-alt2.2
- Rebuild with new Ruby autorequirements.

* Wed Dec 05 2012 Led <led@altlinux.ru> 2.6-alt2.1
- Rebuilt with ruby-1.9.3-alt1

* Mon Nov 29 2010 Alexey I. Froloff <raorn@altlinux.org> 2.6-alt2
- Fix build with Ruby 1.9.2

* Thu Jul 02 2009 Alexey I. Froloff <raorn@altlinux.org> 2.6-alt1
- Built for Sisyphus

